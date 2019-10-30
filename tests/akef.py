# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from sqlfun import checklogin as ch1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(150, 260, 75, 41))
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbtn.setWhatsThis("exit the program")
        self.loginbtn.setAutoFillBackground(False)
        self.loginbtn.setAutoDefault(False)
        self.loginbtn.setDefault(False)
        self.loginbtn.setFlat(False)
        self.loginbtn.setObjectName("loginbtn")
        self.cancelbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(290, 260, 75, 41))
        self.cancelbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelbtn.setWhatsThis("")
        self.cancelbtn.setAutoFillBackground(False)
        self.cancelbtn.setAutoDefault(False)
        self.cancelbtn.setDefault(False)
        self.cancelbtn.setFlat(False)
        self.cancelbtn.setObjectName("cancelbtn")
        self.usernamelabel = QtWidgets.QLabel(self.centralwidget)
        self.usernamelabel.setGeometry(QtCore.QRect(300, 120, 71, 41))
        self.usernamelabel.setObjectName("usernamelabel")
        self.passwordlabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordlabel.setGeometry(QtCore.QRect(290, 170, 61, 41))
        self.passwordlabel.setObjectName("passwordlabel")
        self.usernameedit = QtWidgets.QLineEdit(self.centralwidget)

        self.usernameedit.setGeometry(QtCore.QRect(170, 130, 113, 21))
        self.usernameedit.setText(" user name")
        self.usernameedit.setObjectName("usernameedit")
        self.passworedit = QtWidgets.QLineEdit(self.centralwidget)
        self.passworedit.setGeometry(QtCore.QRect(170, 180, 113, 20))
        self.passworedit.setText("")
        self.passworedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passworedit.setObjectName("passworedit")
        self.cancelbtn.raise_()
        self.usernamelabel.raise_()
        self.passwordlabel.raise_()
        self.usernameedit.raise_()
        self.passworedit.raise_()
        self.loginbtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.cancelbtn.clicked.connect(MainWindow.close)
        self.loginbtn.clicked.connect(self.clickMethod)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginbtn.setText(_translate("MainWindow", "log in"))
        self.cancelbtn.setText(_translate("MainWindow", "cancel"))
        self.usernamelabel.setText(_translate("MainWindow", "שם משתמש :"))
        self.passwordlabel.setText(_translate("MainWindow", "סיסמה :"))

    def clickMethod(self):
        ch1(self.usernameedit.text(),int(self.passworedit.text()))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
