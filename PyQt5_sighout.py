from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *











import sys
sys.path.append('D:\\h3project')

from StudentList import student_list
from StudentClass import student





#student_list = {(sami, sami1384): student(sami, sami1384)}
class Sign_out(object):
    def __init__(self, Sigh_out_window):
        #app = QtWidgets.QApplication(sys.argv)


        
        self.Name = None
        self.Pass = None
        self.Re_pass =None
        self.sign_in_checked = False
        self.next = False
        
        Sigh_out_window.setObjectName("Sigh_out")
        Sigh_out_window.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Sigh_out_window)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.Lname = QtWidgets.QLabel(Sigh_out_window)
        self.Lname.setObjectName("Lname")
        self.verticalLayout.addWidget(self.Lname)
        
        self.Iname = QtWidgets.QLineEdit(Sigh_out_window)
        self.Iname.setText("")
        self.Iname.setObjectName("Iname")
        self.verticalLayout.addWidget(self.Iname)
        
        self.Lpass = QtWidgets.QLabel(Sigh_out_window)
        self.Lpass.setObjectName("Lpass")
        self.verticalLayout.addWidget(self.Lpass)
        
        
        self.Ipass = QtWidgets.QLineEdit(Sigh_out_window)
        self.Ipass.setText("")
        self.Ipass.setObjectName("Ipass")
        self.Ipass.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.verticalLayout.addWidget(self.Ipass)

        
        self.Lrepass = QtWidgets.QLabel(Sigh_out_window)
        self.Lrepass.setObjectName("Lrepass")
        self.verticalLayout.addWidget(self.Lrepass)
        self.Irepass = QtWidgets.QLineEdit(Sigh_out_window)
        self.Irepass.setText("")
        self.Irepass.setObjectName("Irepass")
        self.Irepass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.Irepass)
        
        self.Ucreate = QtWidgets.QPushButton(Sigh_out_window)
        self.Ucreate.setAutoFillBackground(True)
        self.Ucreate.setObjectName("Ucreate")
        self.verticalLayout.addWidget(self.Ucreate)
        
        self.sigh_in = QtWidgets.QPushButton(Sigh_out_window)
        self.sigh_in.setObjectName("sigh_in")
        self.verticalLayout.addWidget(self.sigh_in)

        self.retranslateUi(Sigh_out_window)

        
        print(self)
        self.Ucreate.clicked.connect(self.set_check)
        print(self)
        self.Ucreate.clicked.connect(self.Irepass.clear)
        self.Ucreate.clicked.connect(self.Ipass.clear)
        self.Ucreate.clicked.connect(self.Iname.clear)

        self.sigh_in.clicked.connect(self.sign_in_pressed)
        QtCore.QMetaObject.connectSlotsByName(Sigh_out_window)
        #sys.exit(app.exec_())
    def retranslateUi(self, Sigh_out_window):
        _translate = QtCore.QCoreApplication.translate
        Sigh_out_window.setWindowTitle(_translate("Sigh_out", "Sigh_out"))
        self.Lname.setText(_translate("Sigh_out", "username"))
        self.Iname.setPlaceholderText(_translate("Sigh_out", "name"))
        self.Lpass.setText(_translate("Sigh_out", "password"))
        self.Ipass.setPlaceholderText(_translate("Sigh_out", "password"))
        self.Lrepass.setText(_translate("Sigh_out", "re-enter password"))
        self.Irepass.setPlaceholderText(_translate("Sigh_out", "re-password"))
        self.Ucreate.setText(_translate("Sigh_out", "create"))
        self.sigh_in.setText(_translate("Sigh_out", "Sigh_out"))

    def set_check(self):
        msg = QMessageBox()
        
        self.Name = self.Iname.text()
        self.Pass = self.Ipass.text()
        self.Re_pass = self.Irepass.text()
        self.res = False
        
       
        if self.Pass != self.Re_pass:
            msg.setIcon(QMessageBox.Critical)
            
            self.res = False
            self.text = 'your re-enter password is incorrect'
            msg.setStyleSheet("QLabel{ color: red}")
            
        elif (self.Name, self.Pass) in student_list:
            msg.setIcon(QMessageBox.Information)
            
            self.res = False
            self.text = 'choise another name or password'
            msg.setStyleSheet("QLabel{ color: red}")
            
        elif self.Name != '' and self.Pass != '':
            
            msg.setIcon(QMessageBox.Information)
            
            self.res = True
            self.text = 'you sighend up succesfuly'
            msg.setStyleSheet("QLabel{ color: green}")

        if self.Name != '' and self.Pass != '':
            msg.setText(self.text)
            
            msg.show()
            msg.exec_()

            print('4')            
            if self.res == True:

                self.next = True
                print(
                    1
                    )
                student_list[self.Name, self.Pass] = student(self.Name, self.Pass)
                print('0')
                Sigh_out_window.close()
                
                # in the next step we should connect to the main window page
            
    def sign_in_pressed(self):
        self.sign_in_checked = True
        Sigh_out_window.close()
            
    
    

import sys
app = QtWidgets.QApplication(sys.argv)
Sigh_out_window = QtWidgets.QDialog()
so_window = Sign_out(Sigh_out_window)
Sigh_out_window.show()
        
app.exec_()
