import os
from PyQt5 import QtCore, QtGui, QtWidgets

def button(): #Wow! Оно работает
    exit()

class Ui_DYsound(object):                    #StackOverFlow, deviant art, Хабр, ответы mail.ru, Спасибо!
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DYsound")
        MainWindow.resize(720, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -330, 2051, 1061))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(button)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.113636 rgba(42, 252, 199, 39), stop:0.295455 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 330, 221, 71))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.113636 rgba(42, 252, 199, 39), stop:0.295455 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 250, 221, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pikapika.png"))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(390, 370, 101, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 99)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DYsvp", "DYsvp"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>2021.OpenCode DAxYA</p><p>My VK - <span style=\" text-decoration: underline; color:#381605;\">https://vk.com/ssuccessconnected</span></p><p><a name=\"f11jnc6b-NjfiRgp\"/><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:13px; color:#000000;\">I</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:13px; color:#000000;\"> created this program just for fun </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:13px; font-weight:600; text-decoration: underline; color:#1e5518;\">LOL</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DYsound()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

os.system('')