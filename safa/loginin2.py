# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginin2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from organizer import Ui_organizer as Ui_organizer
from  usher import Ui_Form as cancel



class Ui_login(QtWidgets.QDialog):
    def logincheck(self):
        username =self.username_2.text()
        password = self.password.text()
        if username== "admin" and password== "123":
            self.enterlogin()
        else:
            QtWidgets.QMessageBox.warning(self,"error","Username or Password is not correct",QtWidgets.QMessageBox.Ok)

    def enterlogin(self):
        # self.login=Window()
        # self.login.showMaximized()
        self.window = QtWidgets.QWidget()
        self.ui = Ui_organizer()
        self.ui.setupUi(self.window)

        self.window.show()


    def closeusher(self):
            self.window = QtWidgets.QWidget()
            self.ui = cancel()
            self.ui.setupUi(self.window)
            self.closeusher(self.window)

    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(500, 314)
        self.stackedWidget = QtWidgets.QStackedWidget(login)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -20, 691, 411))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-image: url(:/newPrefix/imagelogin.jpg);\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_25 = QtWidgets.QLabel(self.page_3)
        self.label_25.setGeometry(QtCore.QRect(180, 170, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page_3)
        self.label_26.setGeometry(QtCore.QRect(180, 200, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.username_2 = QtWidgets.QLineEdit(self.page_3)
        self.username_2.setGeometry(QtCore.QRect(290, 170, 121, 20))
        font = QtGui.QFont()
        font.setFamily("PT Simple Bold Ruled")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.username_2.setFont(font)
        self.username_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.username_2.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.username_2.setObjectName("username_2")
        self.password = QtWidgets.QLineEdit(self.page_3)
        self.password.setEnabled(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(290, 200, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.login_2 = QtWidgets.QPushButton(self.page_3)
        self.login_2.setGeometry(QtCore.QRect(210, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login_2.setFont(font)
        self.login_2.setObjectName("login_2")
        self.cancel = QtWidgets.QPushButton(self.page_3)
        self.cancel.setGeometry(QtCore.QRect(350, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.welcome = QtWidgets.QLabel(self.page_3)
        self.welcome.setGeometry(QtCore.QRect(50, 30, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.cancel.clicked.connect(self.closeusher)
        self.login_2.clicked.connect(self.logincheck)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label_25.setText(_translate("login", "Username"))
        self.label_26.setText(_translate("login", "Password"))
        self.login_2.setText(_translate("login", "log in"))
        self.cancel.setText(_translate("login", "cancel"))
        self.welcome.setText(_translate("login", "Welcome To Our Company"))
import login
#import new 1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
