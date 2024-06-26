#Nguyen Huu Ben
#Nguyen Duc Anh
#Duong Thien Chi
#Nguyen Tran Gia

from concurrent.futures import thread
from PyQt6 import QtCore, QtGui, QtWidgets
import socket
import threading
import server,client
import sys
import trace
import tkinter.messagebox as mess
import datetime
import tkinter as tk
from tkinter import filedialog
import time
import datetime
class Ui_Setting(object):
        def __init__(self):
                self.setting_window = None
                self.width = 1920
                self.height = 1080
                self.is_record = False
                self.directory_record_path = ""
                self.app = None
        def setupUi(self, Setting):
                Setting.setObjectName("Setting")
                Setting.resize(380, 249)
                Setting.setStyleSheet("background-color: rgb(245, 247, 250)")
                self.centralwidget = QtWidgets.QWidget(parent = Setting)
                self.centralwidget.setObjectName("centralwidget")
                self.record = QtWidgets.QRadioButton(parent = self.centralwidget)
                self.record.setGeometry(QtCore.QRect(40, 60, 311, 41))
                self.record.setStyleSheet("border: 0px;\n"
                "font: 25 12pt \"Inter Light\";\n"
                "color: rgb(0, 0, 0);")
                self.record.setObjectName("record")
                self.label_8 = QtWidgets.QLabel(parent = self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(40, 130, 81, 31))
                self.label_8.setStyleSheet("border: 0px;\n"
                "font: 25 13pt \"Inter Light\";\n"
                "color: rgb(0, 0, 0);")
                self.label_8.setObjectName("label_8")
                self.display = QtWidgets.QComboBox(parent = self.centralwidget)
                self.display.setGeometry(QtCore.QRect(150, 130, 161, 31))
                self.display.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
                "color: rgb(0, 0, 0);\n"
                "background-color: rgb(255, 255, 255);\n"
                "border-radius: 0px;\n"
                "font: 12 12pt \"Inter ExtraLight\";")
                self.display.setObjectName("display")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.display.addItem("")
                self.label_9 = QtWidgets.QLabel(parent = self.centralwidget)
                self.label_9.setEnabled(False)
                self.label_9.setGeometry(QtCore.QRect(5, 5, 161, 38))
                font = QtGui.QFont()
                font.setFamily("Inter Light")
                font.setPointSize(18)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(3)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("border: 0px;\n"
                "font: 25 18pt \"Inter Light\";\n"
                "color: rgb(0, 0, 0);\n"
                "")
                self.label_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label_9.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label_9.setLineWidth(0)
                self.label_9.setObjectName("label_9")
                self.ok = QtWidgets.QPushButton(parent = self.centralwidget)
                self.ok.setGeometry(QtCore.QRect(260, 190, 101, 31))
                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.ok.setFont(font)
                self.ok.setStyleSheet("QPushButton {\n"
                "    background-color: rgb(173, 173, 173);\n"
                "    color: rgb(0, 0, 0);\n"
                "    font: 16pt \"Inter\";\n"
                "    border-radius: 15px;\n"
                "}\n"
                "QPushButton:hover{\n"
                "    background-color: rgb(218, 218, 218);\n"
                "    color: rgb(0, 0, 0);\n"
                "    font: 16pt \"Inter\";\n"
                "    border-radius: 15px;\n"
                "}\n"
                "QPushButton:pressed{\n"
                "    padding-left: 5px;\n"
                "    padding-top: 5px;\n"
                "}")
                self.ok.setObjectName("ok")
                self.cancel = QtWidgets.QPushButton(parent = self.centralwidget)
                self.cancel.setGeometry(QtCore.QRect(140, 190, 101, 31))
                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.cancel.setFont(font)
                self.cancel.setStyleSheet("QPushButton {\n"
                "    background-color: rgb(173, 173, 173);\n"
                "    color: rgb(0, 0, 0);\n"
                "    font: 16pt \"Inter\";\n"
                "    border-radius: 15px;\n"
                "}\n"
                "QPushButton:hover{\n"
                "    background-color: rgb(218, 218, 218);\n"
                "    color: rgb(0, 0, 0);\n"
                "    font: 16pt \"Inter\";\n"
                "    border-radius: 15px;\n"
                "}\n"
                "QPushButton:pressed{\n"
                "    padding-left: 5px;\n"
                "    padding-top: 5px;\n"
                "}")
                self.cancel.setObjectName("cancel")
                Setting.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(parent = Setting)
                self.statusbar.setObjectName("statusbar")
                Setting.setStatusBar(self.statusbar)

                self.retranslateUi(Setting)
                QtCore.QMetaObject.connectSlotsByName(Setting)
                self.ok.clicked.connect(self.quit_OK)
                self.cancel.clicked.connect(self.quit_Cancel)

        def retranslateUi(self, Setting):
                _translate = QtCore.QCoreApplication.translate
                Setting.setWindowTitle(_translate("Setting", "Setting"))
                self.record.setText(_translate("Setting", "Record remote control"))
                self.label_8.setText(_translate("Setting", "Display"))
                self.display.setItemText(0, _translate("Setting", "1920 x 1080"))
                self.display.setItemText(1, _translate("Setting", "1680 x 1050"))
                self.display.setItemText(2, _translate("Setting", "1600 x 900"))
                self.display.setItemText(3, _translate("Setting", "1440 x 900"))
                self.display.setItemText(4, _translate("Setting", "1400 x 1050"))
                self.display.setItemText(5, _translate("Setting", "1366 x 768"))
                self.display.setItemText(6, _translate("Setting", "1360 x 768"))
                self.display.setItemText(7, _translate("Setting", "1280 x 1024"))
                self.display.setItemText(8, _translate("Setting", "1280 x 960"))
                self.display.setItemText(9, _translate("Setting", "1280 x 800"))
                self.display.setItemText(10, _translate("Setting", "1280 x 768"))
                self.display.setItemText(11, _translate("Setting", "1280 x 720"))
                self.display.setItemText(12, _translate("Setting", "1280 x 600"))
                self.label_9.setText(_translate("Setting", "SETTING"))
                self.ok.setText(_translate("Setting", "OK"))
                self.cancel.setText(_translate("Setting", "Cancel"))
        def open_setting_window(self):
                if self.setting_window is None:  
                        self.setting_window = QtWidgets.QMainWindow()
                        self.setupUi(self.setting_window)
                self.setting_window.show()

        def quit_OK(self):
                if self.setting_window is not None:
                        self.get_size_window()
                        self.is_record = self.record.isChecked()
                        if ( self.is_record):
                                file = filedialog.asksaveasfile(defaultextension = '.avi',
                                                                filetypes = [
                                                                        ("Video file", ".avi"),
                                                                        ("Text file", ".txt"),
                                                                        ("All files", ".*"),
                                                                        ])
                                if file is None:
                                        return
                                self.directory_record_path = file.name
                        self.setting_window.close()
                self.setting_window = None  
        def quit_Cancel(self):
                if self.setting_window is not None:  
                        self.setting_window.close()
                self.setting_window = None 
        def get_size_window(self):
                list = self.display.currentText().split(" ")
                self.width = (list[0])
                self.height = int(list[2])
class Ui_RemoteDesktop(object):
        def __init__(self):
                self.check_open_connect =False
                self.check_start_remote =False
                self.thread_client = None
                self.thread_server = None
                self.setting_window = Ui_Setting()
        def setupUi(self, RemoteDesktop):
                RemoteDesktop.setObjectName("RemoteDesktop")
                RemoteDesktop.resize(1009, 632)
                RemoteDesktop.setStyleSheet("background-color: rgb(245, 247, 250)")
                self.centralwidget = QtWidgets.QWidget(parent = RemoteDesktop)
                self.centralwidget.setObjectName("centralwidget")
                self.widget = QtWidgets.QWidget(parent = self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(30, 90, 469, 470))
                self.widget.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
        "background-color: rgb(230, 233, 237);\n"
        "border-radius: 10px;")
                self.widget.setObjectName("widget")
                self.label = QtWidgets.QLabel(parent = self.widget)
                self.label.setEnabled(False)
                self.label.setGeometry(QtCore.QRect(20, 30, 401, 38))
                font = QtGui.QFont()
                font.setFamily("Inter Light")
                font.setPointSize(18)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(3)
                self.label.setFont(font)
                self.label.setStyleSheet("border: 0px;\n"
        "font: 25 18pt \"Inter Light\";\n"
        "color: rgb(0, 0, 0);")
                self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label.setLineWidth(0)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(parent = self.widget)
                self.label_2.setGeometry(QtCore.QRect(34, 93, 138, 37))
                self.label_2.setStyleSheet("border: 0px;\n"
        "font: 25 13pt \"Inter Light\";\n"
        "color: rgb(0, 0, 0);")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(parent = self.widget)
                self.label_3.setGeometry(QtCore.QRect(34, 189, 116, 31))
                self.label_3.setStyleSheet("border: 0px;\n"
        "font: 25 13pt \"Inter Light\";\n"
        "color: rgb(0, 0, 0);")
                self.label_3.setObjectName("label_3")
                self.my_port = QtWidgets.QLineEdit(parent = self.widget)
                self.my_port.setGeometry(QtCore.QRect(34, 230, 309, 39))
                self.my_port.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;\n"
        "font: 12 12pt \"Inter ExtraLight\";")
                self.my_port.setObjectName("my_port")
                self.your_ip = QtWidgets.QLabel(parent = self.widget)
                self.your_ip.setGeometry(QtCore.QRect(34, 140, 309, 39))
                self.your_ip.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
        "border-radius: 0px;\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(255, 255, 255);\n"
        "font: 12 12pt \"Inter ExtraLight\";")
                self.your_ip.setObjectName("your_ip")
                self.open_connect = QtWidgets.QPushButton(parent = self.widget)
                self.open_connect.setGeometry(QtCore.QRect(34, 370, 251, 51))
                font = QtGui.QFont()
                font.setFamily("Inter ExtraBold")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(10)
                self.open_connect.setFont(font)
                self.open_connect.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(71, 112, 255);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 81 16pt \"Inter ExtraBold\";\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(82, 144, 255);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 81 16pt \"Inter ExtraBold\";\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    padding-left: 5px;\n"
        "    padding-top: 5px;\n"
        "}")
                self.open_connect.setObjectName("open_connect")
                self.label_9 = QtWidgets.QLabel(parent = self.centralwidget)
                self.label_9.setEnabled(False)
                self.label_9.setGeometry(QtCore.QRect(5, 5, 281, 38))
                font = QtGui.QFont()
                font.setFamily("Inter Light")
                font.setPointSize(18)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(3)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("border: 0px;\n"
        "font: 25 18pt \"Inter Light\";\n"
        "color: rgb(0, 0, 0);\n"
        "")
                self.label_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label_9.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label_9.setLineWidth(0)
                self.label_9.setObjectName("label_9")
                self.widget_2 = QtWidgets.QWidget(parent = self.centralwidget)
                self.widget_2.setGeometry(QtCore.QRect(510, 90, 469, 470))
                self.widget_2.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
        "background-color: rgb(230, 233, 237);\n"
        "border-radius: 10px;")
                self.widget_2.setObjectName("widget_2")
                self.label_5 = QtWidgets.QLabel(parent = self.widget_2)
                self.label_5.setEnabled(False)
                self.label_5.setGeometry(QtCore.QRect(20, 30, 431, 38))
                font = QtGui.QFont()
                font.setFamily("Inter Light")
                font.setPointSize(18)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(3)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("border: 0px;\n"
        "font: 25 18pt \"Inter Light\";\n"
        "color: rgb(0, 0, 0);")
                self.label_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label_5.setLineWidth(0)
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(parent = self.widget_2)
                self.label_6.setGeometry(QtCore.QRect(34, 93, 138, 37))
                self.label_6.setStyleSheet("border: 0px;\n"
        "font: 25 13pt \"Inter Light\";\n"
        "color: rgb(0, 0, 0);")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(parent = self.widget_2)
                self.label_7.setGeometry(QtCore.QRect(34, 189, 116, 31))
                self.label_7.setStyleSheet("border: 0px;\n"
        "font: 25 13pt \"Inter Light\";\n"
        "color: rgb(0, 0, 0);")
                self.label_7.setObjectName("label_7")
                self.connect = QtWidgets.QPushButton(parent = self.widget_2)
                self.connect.setGeometry(QtCore.QRect(34, 370, 251, 51))
                font = QtGui.QFont()
                font.setFamily("Inter ExtraBold")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(10)
                self.connect.setFont(font)
                self.connect.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(71, 112, 255);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 81 16pt \"Inter ExtraBold\";\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(82, 144, 255);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 81 16pt \"Inter ExtraBold\";\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    padding-left: 5px;\n"
        "    padding-top: 5px;\n"
        "}")
                self.connect.setObjectName("connect")
                self.server_ip = QtWidgets.QLineEdit(parent = self.widget_2)
                self.server_ip.setGeometry(QtCore.QRect(34, 140, 309, 39))
                self.server_ip.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;\n"
        "font: 12 12pt \"Inter ExtraLight\";")
                self.server_ip.setObjectName("server_ip")
                self.port_server = QtWidgets.QLineEdit(parent = self.widget_2)
                self.port_server.setGeometry(QtCore.QRect(34, 230, 309, 39))
                self.port_server.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius: 0px;\n"
        "font: 12 12pt \"Inter ExtraLight\";")
                self.port_server.setObjectName("port_server")
                self.Send_file = QtWidgets.QPushButton(parent = self.widget_2)
                self.Send_file.setGeometry(QtCore.QRect(250, 300, 160, 40))
                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.Send_file.setFont(font)
                self.Send_file.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(173, 173, 173);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 16pt \"Inter\";\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(218, 218, 218);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 16pt \"Inter\";\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    padding-left: 5px;\n"
        "    padding-top: 5px;\n"
        "}")
                self.Send_file.setObjectName("Send_file")
                self.Setting = QtWidgets.QPushButton(parent = self.widget_2)
                self.Setting.setGeometry(QtCore.QRect(34, 300, 160, 40))
                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.Setting.setFont(font)
                self.Setting.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(173, 173, 173);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 16pt \"Inter\";\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(218, 218, 218);\n"
        "    color: rgb(0, 0, 0);\n"
        "    font: 16pt \"Inter\";\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    padding-left: 5px;\n"
        "    padding-top: 5px;\n"
        "}")
                self.Setting.setObjectName("Setting")
                RemoteDesktop.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(parent = RemoteDesktop)
                self.statusbar.setObjectName("statusbar")
                RemoteDesktop.setStatusBar(self.statusbar)

                self.retranslateUi(RemoteDesktop)
                QtCore.QMetaObject.connectSlotsByName(RemoteDesktop)
                self.open_connect.clicked.connect(self.open_click)
                self.connect.clicked.connect(self.connect_click)
                self.Send_file.clicked.connect(self.sendfile_click)
        def sendfile_click(self):
                if self.check_start_remote:
                        self.app.start_sendfile()
                else: pass
        def open_click(self):
                if not self.check_open_connect:
                        self.start_connect()
                else:
                        self.close_connect()
                        self.open_connect.setText("Open Connect")
        def connect_click(self):
                if not self.check_start_remote:
                        self.start_remote()
                else:
                        self.close_remote()
                        self.connect.setText("Connect")

        def retranslateUi(self, RemoteDesktop):
                _translate = QtCore.QCoreApplication.translate
                RemoteDesktop.setWindowTitle(_translate("RemoteDesktop", "Remote Desktop"))
                self.label.setText(_translate("RemoteDesktop", "ALLOW REMOTE CONTROL"))
                self.label_2.setText(_translate("RemoteDesktop", "Your IP"))
                self.label_3.setText(_translate("RemoteDesktop", "Port"))
                self.my_port.setPlaceholderText(_translate("RemoteDesktop", "Enter Port"))
                self.your_ip.setText(_translate("RemoteDesktop", self.get_ip_address()))
                self.open_connect.setText(_translate("RemoteDesktop", "Open Connect"))
                self.label_9.setText(_translate("RemoteDesktop", "REMOTE DESKTOP"))
                self.label_5.setText(_translate("RemoteDesktop", "CONTROL REMOTE DESKTOP"))
                self.label_6.setText(_translate("RemoteDesktop", "Server IP"))
                self.label_7.setText(_translate("RemoteDesktop", "Port"))
                self.connect.setText(_translate("RemoteDesktop", "Connect"))
                self.server_ip.setPlaceholderText(_translate("RemoteDesktop", "Enter IP"))
                self.port_server.setPlaceholderText(_translate("RemoteDesktop", "Enter Port"))
                self.Send_file.setText(_translate("RemoteDesktop", "Send File"))
                self.Setting.setText(_translate("RemoteDesktop", "Setting"))
                self.Setting.clicked.connect(self.setting_window.open_setting_window)
        
        def start_connect(self):
                if not self.check_start_remote and not self.check_open_connect:
                        self.check_open_connect = True
                        self.run_server()
                        self.open_connect.setText("Close Connect")
                else:
                        mess.showerror(title = "Lỗi",
                                message = "Bạn không thể mở connect vì đang remote.")
                        
        def start_remote(self): 
                if not self.check_start_remote and not self.check_open_connect:
                        self.check_start_remote = True
                        self.run_client()
                        self.connect.setText("Close Connect")
                else:
                        mess.showerror(title = "Lỗi",
                                message = "Bạn không thể remote vì đang mở connect.")
        def kill_thread(self, app):
                self.app.running = False
        def close_connect(self):
                self.check_open_connect = False
                self.kill_thread(self.app)
        def close_remote(self):
                self.check_start_remote = False
                self.kill_thread(self.app)
        def thread_run_server(self):
                self.app = server.Server()
                self.app.port = int(self.my_port.text())
                self.app.start_server()
        def run_server(self):
                self.thread_server = threading.Thread(target=self.thread_run_server)
                self.thread_server.daemon = True
                self.thread_server.start()
        def thread_run_client(self):
                self.app = client.Client()
                self.app.host = self.server_ip.text()
                self.app.port = int(self.port_server.text())
                self.app.record = self.setting_window.is_record
                self.app.width_window = self.setting_window.width
                self.app.height_window = self.setting_window.height
                if ( self.app.record):
                         self.app.filename_record = self.setting_window.directory_record_path
                print( self.app.host,  self.app.port,  self.app.width_window,  self.app.height_window, self.app.record)
                print( self.app.filename_record)
                self.app.start_client()
        def run_client(self):
                self.thread_client =  threading.Thread(target=self.thread_run_client)
                self.thread_client.daemon = True
                self.thread_client.start()
        def get_ip_address(self):
                server_ip = socket.gethostbyname(socket.gethostname())
                return server_ip
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RemoteDesktop = QtWidgets.QMainWindow()
    ui = Ui_RemoteDesktop()
    ui.setupUi(RemoteDesktop)
    RemoteDesktop.show()
    sys.exit(app.exec())  
