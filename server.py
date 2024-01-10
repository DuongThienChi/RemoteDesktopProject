import socket
import cv2
import pynput
from pynput.mouse import Button as but, Controller
import numpy as np
import threading
import pyautogui
import keyboard 
import win32api
import pickle
import tkinter.messagebox as mess
import os
import time
import struct
from pynput import keyboard
class Server:
    def __init__(self):
        self.x_res,self.y_res = int(pyautogui.size()[0]), int(pyautogui.size()[1])
        self.width,self.height = int(pyautogui.size()[0]), int(pyautogui.size()[1])
        self.host = ""
        self.my_host = "26.86.28.22" #socket.gethostbyname(socket.gethostname())
        self.running = False
        self.port = 4444
        self.server_socket = None
        self.screen_quality = 45
        self.mouse = Controller()
        self.server_host = None
    def handle_error(self, error):
        mess.showerror(title = "Error",
                             message = error)
        print("Closing connection")
        self.running = False
    def receive_client_ip(self): #nhan dia chi ip client
        server_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       # server_host.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server_host.bind((self.my_host, self.port))
            server_host.settimeout(10)
            server_host.listen()
            conn, addr = server_host.accept()
            self.host = conn.recv(1024)
            self.host = str(self.host.decode("utf-8"))
            conn.close()
            server_host.close()
        except socket.timeout as e:
                server_host.close()
                self.handle_error(e)
    def recv_size_window(self):   #nhan kich thuoc cua so
        try:
            server_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            server_host.bind((self.my_host, self.port))
            server_host.listen()
            conn, addr = server_host.accept()
            size = conn.recv(1024).decode("utf-8")
            size = size.split(' ')
            self.x_res,self.y_res = int(size[0]),int(size[1])
            print(self.x_res,self.y_res)
            conn.close()
            server_host.close()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError,TimeoutError) as e:
                self.handle_error(e)
    
    def get_frame(self):  #chụp màn hình
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (self.x_res,self.y_res), interpolation=cv2.INTER_AREA)
        return frame
    def send_display(self):   #gởi màn hình
        socket_screen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #dùng TCP để gởi màn hình
        socket_screen.connect((self.host,self.port))
        while self.running: #
            frame = self.get_frame()
            result, frame = cv2.imencode('.jpg', frame,[int(cv2.IMWRITE_JPEG_QUALITY), self.screen_quality])
            data = pickle.dumps(frame, 0)
            size = len(data)
            try:
                socket_screen.sendall(struct.pack('>L', size) + data)
            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError,TimeoutError) as e:
                self.handle_error(e)
                break
        socket_screen.close()
    def get_keyboard(self,key):
        controller = keyboard.Controller()
        if key['type'] == 'down':
            controller.press(key['key'])
        else:
            controller.release(key['key'])
    def recv_control(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #dùng UDP để nhận chuột
        self.server_socket.bind((self.my_host,self.port))
        hold = 0
        header = struct.calcsize('Q')
        data = b''
        while self.running:
            try:
                while len(data) < header:
                    data += self.server_socket.recv(1024)
                mess_size = struct.unpack('Q',data[:header])[0]
                data = data[header:]
                while len(data) < mess_size:
                    data += self.server_socket.recv(1024)
                resquest = data[:mess_size]
                data = data[mess_size:]
                key = pickle.loads(resquest)
                if(key['type_data'] == 'mouse'):
                    if(key['data']!=""):
                        datagram = key['data']
                        datagram = datagram.split()
                        if(len(datagram) == 3):
                            if(datagram[0] == 'mouse_move'):
                                x,y = int(int(datagram[1])*self.width/self.x_res), int(int(datagram[2])*self.height/self.y_res)
                                win32api.SetCursorPos((x,y))
                            elif(datagram[0] == 'left_click_and_hold' and hold==0):
                                pyautogui.mouseDown()
                                hold = 1
                            elif(datagram[0] == 'left_release' and hold ==1):
                                pyautogui.mouseUp()
                                hold=0
                            elif(datagram[0] == 'left_double_click'):
                                pyautogui.doubleClick()
                            elif(datagram[0] == 'right_click'):
                                pyautogui.rightClick()
                            elif(datagram[0] == 'middle_click'):
                                pyautogui.middleClick()
                        elif(len(datagram) == 2):
                            if(datagram[0] == 'scroll' and datagram[1] == 'up'):
                                self.mouse.scroll(0,1)
                            elif(datagram[0] == 'scroll' and datagram[1] == 'down'):
                                self.mouse.scroll(0,-1)    
                else:
                    self.get_keyboard(key)
            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError,TimeoutError) as e:
                self.handle_error(e)
                break
        self.server_socket.close()
    def start_server(self):
        self.receive_client_ip()
        print(self.host)
        self.running=True 
        self.recv_size_window ()
        print(self.width, self.height)
        t2= threading.Thread(target = self.recv_control) #nhận chuột va phim
        t1= threading.Thread(target = self.send_display) #gởi màn hình
        t1.daemon = True
        t2.daemon = True
        t2.start()
        t1.start()
        t2.join()
        t1.join()
# if __name__ == "__main__":
#     server_run = Server()
#     server_run.start_server()