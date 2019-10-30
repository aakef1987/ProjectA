# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(140, 360, 75, 41))
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbtn.setWhatsThis("")
        self.loginbtn.setAutoFillBackground(False)
        self.loginbtn.setAutoDefault(False)
        self.loginbtn.setDefault(False)
        self.loginbtn.setFlat(False)
        self.loginbtn.setObjectName("loginbtn")
        self.cancelbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(300, 360, 75, 41))
        self.cancelbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelbtn.setWhatsThis("")
        self.cancelbtn.setAutoFillBackground(False)
        self.cancelbtn.setAutoDefault(False)
        self.cancelbtn.setDefault(False)
        self.cancelbtn.setFlat(False)
        self.cancelbtn.setObjectName("cancelbtn")
        self.usernamelabel = QtWidgets.QLabel(self.centralwidget)
        self.usernamelabel.setGeometry(QtCore.QRect(100, 120, 61, 31))
        self.usernamelabel.setObjectName("usernamelabel")
        self.passwordlabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordlabel.setGeometry(QtCore.QRect(100, 180, 47, 13))
        self.passwordlabel.setObjectName("passwordlabel")
        self.usernameedit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameedit.setGeometry(QtCore.QRect(200, 130, 113, 21))
        self.usernameedit.setObjectName("usernameedit")
        self.passworedit = QtWidgets.QLineEdit(self.centralwidget)
        self.passworedit.setGeometry(QtCore.QRect(200, 180, 113, 20))
        self.passworedit.setObjectName("passworedit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginbtn.setText(_translate("MainWindow", "log in"))
        self.cancelbtn.setText(_translate("MainWindow", "cancel"))
        self.usernamelabel.setText(_translate("MainWindow", "user name"))
        self.passwordlabel.setText(_translate("MainWindow", "password"))
        self.usernameedit.setText(_translate("MainWindow", "user name"))
        self.passworedit.setText(_translate("MainWindow", "password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
