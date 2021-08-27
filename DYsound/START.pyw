import random
import pygame
import math
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from pygame import mixer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(640, 402)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.182, y1:0.102409, x2:1, y2:1, stop:0.113636 rgba(0, 62, 79, 147), stop:0.306818 rgba(28, 14, 68, 156));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-130, -40, 1031, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("2HYI.gif"))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 310, 641, 80))
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget) #Начиная отсюда list
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 121, 311))
        self.listWidget.setStyleSheet("font: 75 italic 8pt \"MS Sans Serif\";\n"
"color: rgb(121, 92, 121);")
        self.listWidget.setObjectName("listWidget")     
        MainWindow.setCentralWidget(self.centralwidget) 
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow): 
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Player", "Player"))


class MainWindow(QMainWindow, Ui_MainWindow,):                 
    def __init__(self):                         
        super().__init__()
        
        self.setupUi(self)     
                           
        self.listWidget.clear()
        self.listWidget.itemClicked.connect(self.onClicked) 
        
        self.pushbutton_close = QPushButton('✖', self)

        self.pushbutton_stop = QPushButton('✘', self)
        
        self.pushbutton_pause = QPushButton('■', self)
        
        self.pushbutton_remove = QPushButton('⏵', self)

        self.btn = QPushButton('FILE', self)

    
        self.itemlist = ['ВыборПапкиНаFile']
        self.listWidget.addItems(self.itemlist)

        self.pushbutton_close.clicked.connect(self.close)
        self.pushbutton_close.setStyleSheet("background-color: rgb(255, 51, 11);color: rgb(255, 255, 255);")
        self.pushbutton_close.move(200,500)
        self.pushbutton_close.setGeometry(560, 0, 40, 20)
        
        self.pushbutton_stop.clicked.connect(self.clickstop)
        self.pushbutton_stop.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.113636 rgba(0, 62, 79, 147), stop:0.306818 rgba(28, 14, 68, 156));background-color: rgb(130, 68, 206);")
        self.pushbutton_stop.move(200,500)
        self.pushbutton_stop.setGeometry(0, 290, 40, 20)
        
        self.pushbutton_pause.clicked.connect(self.clickpause)
        self.pushbutton_pause.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.113636 rgba(0, 62, 79, 147), stop:0.306818 rgba(28, 14, 68, 156));background-color: rgb(130, 68, 206);")
        self.pushbutton_pause.move(200,500)
        self.pushbutton_pause.setGeometry(38, 290, 40, 20)
        
        self.pushbutton_remove.clicked.connect(self.clickremove)
        self.pushbutton_remove.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.113636 rgba(0, 62, 79, 147), stop:0.306818 rgba(28, 14, 68, 156));background-color: rgb(130, 68, 206);")
        self.pushbutton_remove.move(200,500)
        self.pushbutton_remove.setGeometry(0, 290, 40, 20)

        self.btn.clicked.connect(self.update_dir)
        self.btn.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.113636 rgba(0, 62, 79, 147), stop:0.306818 rgba(28, 14, 68, 156));background-color: rgb(130, 68, 206);")
        self.btn.move(200,500)
        self.btn.setGeometry(600, 0, 40, 20)
        
        self.pushbutton_stop.hide()
        self.pushbutton_remove.hide()
        self.pushbutton_pause.hide()
        
        self.listWidget.itemClicked.connect(self.onClicked)

    def onClicked(self, item):
        try:
            path_file = item.data(QtCore.Qt.UserRole)
            with open(path_file, 'r') as file:
                self.pushbutton_remove.hide()
                self.pushbutton_stop.show()
                self.pushbutton_pause.show()
            
                pygame.init()
                name = item.text()
                pygame.mixer.music.load(name)
                pygame.mixer.music.play(1)
        except Exception:
            self.pushbutton_stop.hide()
            self.pushbutton_pause.hide()
            self.pushbutton_remove.hide()
            print('Error file')

    def close(self):
        exit()
    
    def clickstop(self):
        try:
            self.pushbutton_stop.hide()
            self.pushbutton_pause.hide()
            self.pushbutton_remove.hide()
            pygame.mixer.music.stop()
            pygame.quit()
        except Exception:
            pass
    
    def clickpause(self):
        try:
            self.pushbutton_pause.hide()
            self.pushbutton_remove.show()
            
            pygame.mixer.music.pause()
        except Exception:
            pass
    
    def clickremove(self):
        try:
            self.pushbutton_pause.show()
            self.pushbutton_remove.hide()
            
            pygame.mixer.music.unpause()
        except Exception:
            pass
        
    def closeEvent(self, event):
        try:
            pygame.mixer.music.stop()
            pygame.quit()
        except Exception:
            pass
        finally:
            pygame.quit()




    def update_dir(self): 
        directory = QFileDialog.getExistingDirectory(
            self,
            "QFileDialog.getExistingDirectory()",
            '.'
        )
        if directory:
            _list = [ file for file in os.listdir(f"{directory}") if file.endswith(".mp3") ] #/*.txt")]
            if not _list:
                return
            self.listWidget.clear()
            for i, item in enumerate(_list):
                self.listWidget.addItem(item)
                item_data = os.path.join(directory, item).replace('\\', '/')
                self.listWidget.item(i).setData(QtCore.Qt.UserRole, item_data)            

      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())