from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from h3project.StudentList import student_list
from h3project.StudentClass import student

#student_list = {(sami, sami1384): student(sami, sami1384)}
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Name = None
        self.Pass = None
        self.Re_pass =None
        
        Dialog.setObjectName("sigh-in")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.Lname = QtWidgets.QLabel(Dialog)
        self.Lname.setObjectName("Lname")
        self.verticalLayout.addWidget(self.Lname)
        
        self.Iname = QtWidgets.QLineEdit(Dialog)
        self.Iname.setText("")
        self.Iname.setObjectName("Iname")
        self.verticalLayout.addWidget(self.Iname)
        
        self.Lpass = QtWidgets.QLabel(Dialog)
        self.Lpass.setObjectName("Lpass")
        self.verticalLayout.addWidget(self.Lpass)
        
        self.Ipass = QtWidgets.QLineEdit(Dialog)
        self.Ipass.setText("")
        self.Ipass.setObjectName("Ipass")
        self.verticalLayout.addWidget(self.Ipass)

        
        self.Lrepass = QtWidgets.QLabel(Dialog)
        self.Lrepass.setObjectName("Lrepass")
        self.verticalLayout.addWidget(self.Lrepass)
        self.Irepass = QtWidgets.QLineEdit(Dialog)
        self.Irepass.setText("")
        self.Irepass.setObjectName("Irepass")
        self.verticalLayout.addWidget(self.Irepass)
        
        self.Ucreate = QtWidgets.QPushButton(Dialog)
        self.Ucreate.setAutoFillBackground(True)
        self.Ucreate.setObjectName("Ucreate")
        self.verticalLayout.addWidget(self.Ucreate)
        
        self.sigh_in = QtWidgets.QPushButton(Dialog)
        self.sigh_in.setObjectName("sigh_in")
        self.verticalLayout.addWidget(self.sigh_in)

        self.retranslateUi(Dialog)

        
        print(self)
        self.Ucreate.clicked.connect(self.set_check)
        print(self)
        self.Ucreate.clicked.connect(self.Irepass.clear)
        self.Ucreate.clicked.connect(self.Ipass.clear)
        self.Ucreate.clicked.connect(self.Iname.clear)

    
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("sigh-in", "sigh-in"))
        self.Lname.setText(_translate("sigh-in", "username"))
        self.Iname.setPlaceholderText(_translate("sigh-in", "name"))
        self.Lpass.setText(_translate("sigh-in", "password"))
        self.Ipass.setPlaceholderText(_translate("sigh-in", "password"))
        self.Lrepass.setText(_translate("sigh-in", "re-enter password"))
        self.Irepass.setPlaceholderText(_translate("sigh-in", "re-password"))
        self.Ucreate.setText(_translate("sigh-in", "create"))
        self.sigh_in.setText(_translate("sigh-in", "sigh-in"))

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

            
            if self.res == True:
                student_list[self.Name, self.Pass] = student(self.Name, self.Pass)
                Dialog.close()
                # in the next step we should connect to the main window page
            

            
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    sys.exit(app.exec_())
