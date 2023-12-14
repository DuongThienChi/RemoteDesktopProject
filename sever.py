import socket
import os
import mss,sys
import tkinter.messagebox as mess
from threading import Thread
local = sys.argv[0]
local = local.split("\\")
filename = local[len(local)-1]



class Server:
    def __init__(self):
        self.mouse = Controller()
        self.my_host = self.get_ip_address()
        self.your_host = ""
        self.port = 5500
        self.server_control = None
        self.id_client = ("",0)
        self.filename = ""
    def get_ip_address(self):
        my_host = socket.gethostbyname(socket.gethostname())
        return my_host
    def recive_client_host(self):
        try:
            server_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            server_host.bind((self.my_host, self.port))
            self.your_host = server_host.recv(1024)
            self.your_host = str(self.your_host.decode("utf-8"))
            server_host.close()
        except:
            mess.showerror(title="Lỗi",
                             message="Kết nối thất bại!")
            os.system("taskkill /f /im "+filename)
    def recive_control(self):
        try: 
            server_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_host.bind((self.my_host, self.my_port))
        except:
            mess.showerror(title="Lỗi",
                             message="Kết nối thất bại!")
            os.system("taskkill /f /im "+filename)
            
if __name__ == '__main__':
         
        

