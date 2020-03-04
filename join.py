# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'join.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_institute = QtWidgets.QLabel(self.centralwidget)
        self.label_institute.setGeometry(QtCore.QRect(30, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_institute.setFont(font)
        self.label_institute.setObjectName("label_institute")
        self.entry_institute = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_institute.setGeometry(QtCore.QRect(220, 60, 301, 31))
        self.entry_institute.setObjectName("entry_institute")
        self.label_class_name = QtWidgets.QLabel(self.centralwidget)
        self.label_class_name.setGeometry(QtCore.QRect(30, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_class_name.setFont(font)
        self.label_class_name.setObjectName("label_class_name")
        self.entry_class_name = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_class_name.setGeometry(QtCore.QRect(150, 130, 371, 31))
        self.entry_class_name.setObjectName("entry_class_name")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(40, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.entry_password = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_password.setGeometry(QtCore.QRect(150, 189, 371, 31))
        self.entry_password.setObjectName("entry_password")
        self.submit_butt = QtWidgets.QPushButton(self.centralwidget)
        self.submit_butt.setGeometry(QtCore.QRect(200, 270, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submit_butt.setFont(font)
        self.submit_butt.setObjectName("submit_butt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submit(self):
        self.password = self.entry_password.text()
        self.name = self.entry_class_name.text()
        self.institute = self.entry_institute.text()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_institute.setText(_translate("MainWindow", "educational Institute"))
        self.entry_institute.setPlaceholderText(_translate("MainWindow", "name"))
        self.label_class_name.setText(_translate("MainWindow", "class name"))
        self.entry_class_name.setPlaceholderText(_translate("MainWindow", "name"))
        self.label_password.setText(_translate("MainWindow", "password"))
        self.entry_password.setPlaceholderText(_translate("MainWindow", "password"))
        self.submit_butt.setText(_translate("MainWindow", "submit"))
        self.submit_butt.clicked.connect(self.submit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
