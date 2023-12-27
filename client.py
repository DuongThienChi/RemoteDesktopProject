import socket
import pyautogui
from threading import Thread
import threading
import cv2
import struct
from pynput import keyboard
import pickle
import tkinter.messagebox as mess
import numpy as np
import os
import time
class Client:
    def __init__(self):
        self.host=""
        self.my_host = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.click_count = 0
        self.client_socket = None
        self.window = "APPSocket"
        self.focus_window = False
    def send_size_window(self):  #goi kich thuoc cua so
        width= input("Choose size width of window: ")
        height= input("Choose size height of window: ")
        try:
            client_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_host.connect((self.host,self.port))
            client_host.send(f"{width} {height}".encode("utf-8"))
            client_host.close()
        except:
            mess.showerror(title="Lỗi",
                             message="Client Kết nối thất bại!")
    def send_client_ip(self): #goi dia chi ip client
        try:
            client_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_host.connect((self.host,self.port))
            client_host.send(self.my_host.encode("utf-8"))
            client_host.close()
        except:
            mess.showerror(title="Lỗi",
                             message="Client Kết nối thất bại!")
    def send_mouse(self,data): #gởi dữ liệu chuột
        message =  {
            'type_data': 'mouse',
            'data': data
        }
        mess = pickle.dumps(message)
        packet = struct.pack('Q',len(mess)) + mess
        self.client_socket.sendall(packet)
    def mouse_event(self,event, x, y, flags,param): #Lắng nghe chuột
            if event == cv2.EVENT_MOUSEMOVE:
                message=f'mouse_move {x} {y}'
                self.send_mouse(message)
            elif event == cv2.EVENT_LBUTTONDOWN:
                self.click_count = 1
                message = f'left_click_and_hold {x} {y}'
                self.send_mouse(message)
            elif event == cv2.EVENT_LBUTTONUP:
                if self.click_count == 1:
                    message = f'left_release {x} {y}' 
                    self.send_mouse(message)
                    self.click_count = 0
            elif event == cv2.EVENT_LBUTTONDBLCLK:
                message = f'left_double_click {x} {y}'
                self.send_mouse(message)
            elif event == cv2.EVENT_RBUTTONDOWN:
                message = f'right_click {x} {y}'
                self.send_mouse(message)
            elif event == cv2.EVENT_MBUTTONDOWN:
                message = f'middle_click {x} {y}'
                self.send_mouse(message)
            elif event == cv2.EVENT_MOUSEWHEEL:
                if flags > 0:
                   self.send_mouse('scroll up')
                else:
                    self.send_mouse('scroll down')
                    #client

    def send_key(self,key):
        message = pickle.dumps(key)
        packet = struct.pack('Q',len(message)) + message
        self.client_socket.sendall(packet)
        
    def on_press(self,key):
        data = {
            'type_data' : 'key',
            'type' : 'down',
            'key' : key
        }
        if(self.focus_window):
            self.send_key(data)
        
    def on_release(self,key):
        data = {
            'type_data' : 'key',
            'type' : 'up',
            'key' : key
        }
        if(self.focus_window):
            self.send_key(data)
    def listen_keyboard(self):
        while True:
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()
    def revceive_screen(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #nhận màn hình
        server_socket.bind((self.my_host, self.port))
        server_socket.listen()
        connection, address = server_socket.accept()
        payload_size = struct.calcsize('>L')
        data = b""
        while True:
            try:
                break_loop = False
                while len(data) < payload_size:
                    received = connection.recv(4096)
                    if received == b'':
                        connection.close()
                        break_loop = True
                        break
                    data += received
                if break_loop:
                    break
                packed_msg_size = data[:payload_size]
                
                data = data[payload_size:]
                
                msg_size = struct.unpack(">L", packed_msg_size)[0]
                while len(data) < msg_size:
                    data += connection.recv(4096)
                    
                frame_data = data[:msg_size]
                data = data[msg_size:]
                
                frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                cv2.namedWindow(self.window, cv2.WINDOW_NORMAL)
                cv2.resizeWindow(self.window,frame.shape[1], frame.shape[0])
                
                cv2.imshow(self.window, frame) #show màn hình
                if (pyautogui.getActiveWindowTitle() == self.window):
                    self.focus_window = True
                else:
                    self.focus_window = False
                cv2.setMouseCallback(self.window, self.mouse_event)  #gởi chuột
                cv2.waitKey(1)
            except:
                connection.close()
                cv2.destroyAllWindows()
                break
            # if cv2.waitKey(1): 
            #     connection.close()
            #     cv2.destroyAllWindows()
            #     break
    def start_client(self):
        self.host=input("Enter host: ")
        self.send_client_ip()
        self.send_size_window()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #dùng UDP để gởi chuột
        self.client_socket.connect((self.host, self.port))
        t1=threading.Thread(target=self.revceive_screen) #nhận màn hình
        t2= threading.Thread(target=self.listen_keyboard) 
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        self.client_socket.close()
if __name__ == "__main__":
    client = Client()
    client.start_client()
    