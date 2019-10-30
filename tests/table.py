# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableview.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class Ui_TableWindow(object):
    def setupUi(self, TableWindow):
        TableWindow.setObjectName("TableWindow")
        TableWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TableWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(620, 120, 75, 41))
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.refreshButton.setCheckable(False)
        self.refreshButton.setChecked(False)
        self.refreshButton.setObjectName("refreshButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(620, 240, 75, 41))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.backButton.setObjectName("backButton")
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("new.db")
        db.open()
        model = QSqlTableModel(None, db)
        model.setTable("users")
        model.select()
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(70, 40, 431, 311))
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(model)
        self.tableView.show()
        TableWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TableWindow)
        self.statusbar.setObjectName("statusbar")
        TableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TableWindow)
        self.backButton.clicked.connect(TableWindow.close)
        self.refreshButton.clicked.connect(self.mymethod)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def mymethod(self):
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("new.db")
            db.open()
            model = QSqlTableModel(None, db)
            model.setTable("users")
            model.select()
            self.tableView.setModel(model)
            self.tableView.show()


    def retranslateUi(self, TableWindow):
        _translate = QtCore.QCoreApplication.translate
        TableWindow.setWindowTitle(_translate("TableWindow", "MainWindow"))
        self.refreshButton.setText(_translate("TableWindow", "refresh"))
        self.backButton.setText(_translate("TableWindow", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TableWindow = QtWidgets.QMainWindow()
    ui = Ui_TableWindow()
    ui.setupUi(TableWindow)
    TableWindow.show()
    sys.exit(app.exec_())
