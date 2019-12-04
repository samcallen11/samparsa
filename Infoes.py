# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\h3project\Info\Info_Pages.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
Months = {
         '1':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 31],
         '2':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
         '3':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',' 26', '27', '28', '29', '30', '31'],
         '4':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',' 26', '27', '28', '29', '30', '31'],
         '5':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
         '6':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
         '7':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
         '8':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
         '9':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
         '10':['1','2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
         '11':['1','2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
         '12':['1','2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']}

school_info = {'..':{'':[""]}, "Allameh Helli 3": {'7':['101', '102', '103', '104'], '8':['201', '202'], '9':['301', '302', '303']}}

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Infor(object):
    def __init__(self, window):
        self.next = False
        window.setObjectName("Information")
        window.resize(402, 424)
        
        self.Fname = QtWidgets.QLineEdit(window)
        self.Fname.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.Fname.setObjectName("Fname")
        
        self.Info = QtWidgets.QLabel(window)
        self.Info.setGeometry(QtCore.QRect(20, 10, 291, 51))

        font = QtGui.QFont()
        font.setPointSize(28)
        self.Info.setFont(font)
        self.Info.setObjectName("Info")

        self.Lname = QtWidgets.QLineEdit(window)
        self.Lname.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.Lname.setObjectName("Lname")

        self.Uname = QtWidgets.QLineEdit(window)
        self.Uname.setGeometry(QtCore.QRect(20, 100, 241, 20))
        self.Uname.setObjectName("Uname")

        self.Rclass = QtWidgets.QComboBox(window)
        self.Rclass.setGeometry(QtCore.QRect(20, 210, 111, 22))
        self.Rclass.setEditable(False)
        self.Rclass.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.Rclass.setFrame(True)
        self.Rclass.setObjectName("Rclass")
        self.Rclass.addItem("")
        self.Rclass.addItem("")
        self.Rclass.addItem("")
        self.Rclass.addItem("")
        self.Rclass.addItem("")
        self.Rclass.addItem("")
        self.Rclass.addItem("")

        self.LRclass = QtWidgets.QLabel(window)
        self.LRclass.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.LRclass.setObjectName("LRclass")

        self.LBirh = QtWidgets.QLabel(window)
        self.LBirh.setGeometry(QtCore.QRect(20, 236, 51, 20))
        self.LBirh.setStyleSheet("")
        self.LBirh.setObjectName("LBirh")

        self.Year = QtWidgets.QLineEdit(window)
        self.Year.setGeometry(QtCore.QRect(20, 260, 51, 20))
        self.Year.setText("")
        self.Year.setObjectName("Year")

        self.Bslash = QtWidgets.QLabel(window)
        self.Bslash.setGeometry(QtCore.QRect(76, 260, 21, 21))
        self.Bslash.setObjectName("Bslash")

        self.Bslash_2 = QtWidgets.QLabel(window)
        self.Bslash_2.setGeometry(QtCore.QRect(145, 260, 16, 21))
        self.Bslash_2.setObjectName("Bslash_2")

        self.Fbox = QtWidgets.QCheckBox(window)
        self.Fbox.setGeometry(QtCore.QRect(20, 300, 70, 17))
        self.Fbox.setChecked(True)
        self.Fbox.setObjectName("Fbox")

        self.Mbox = QtWidgets.QCheckBox(window)
        self.Mbox.setGeometry(QtCore.QRect(100, 300, 70, 17))
        self.Mbox.setChecked(False)
        self.Mbox.setObjectName("Mbox")
        

        self.Roles = QtWidgets.QCheckBox(window)
        self.Roles.setGeometry(QtCore.QRect(20, 330, 211, 17))
        self.Roles.setObjectName("Roles")

        self.sigh_up = QtWidgets.QPushButton(window)
        self.sigh_up.setGeometry(QtCore.QRect(150, 370, 75, 41))
        self.sigh_up.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"selection-background-color: rgb(78, 255, 84);")
        self.sigh_up.setObjectName("sigh_up")

        

        self.MonthL = QtWidgets.QComboBox(window)
        self.MonthL.setGeometry(QtCore.QRect(90, 260, 51, 20))
        self.MonthL.setObjectName("Month")
        
        self.DayL = QtWidgets.QComboBox(window)
        self.DayL.setGeometry(QtCore.QRect(160, 260, 51, 20))
        self.DayL.setObjectName("DayL")


        for month in Months:
            self.MonthL.addItem(month)
            
        for day in Months['1']:
            day = str(day)
            self.DayL.addItem(day)

        self.MonthL.currentTextChanged[str].connect(self.activ_month)
        
        
        self.SchoolL = QtWidgets.QComboBox(window)
        self.SchoolL.setGeometry(QtCore.QRect(20, 130, 111, 22))
        self.SchoolL.setObjectName("SchoolL")


        self.GradeL = QtWidgets.QComboBox(window)
        self.GradeL.setGeometry(QtCore.QRect(150, 130, 111, 22))
        self.GradeL.setObjectName("GradeL")
        
        
        self.ClassesL = QtWidgets.QComboBox(window)
        self.ClassesL.setGeometry(QtCore.QRect(20, 160, 241, 22))
        self.ClassesL.setObjectName("ClassesL")


        for school in school_info:
            self.SchoolL.addItem(school)

        for grade in school_info['..']:
            self.GradeL.addItem(grade)
            
        for i in school_info['..'][grade]:
            self.ClassesL.addItem(i)

        
        self.SchoolL.activated[str].connect(self.on_combo_activated_1)
        self.GradeL.activated[str].connect(self.on_combo_activated_2)



        self.retranslateUi(window)
        
        self.Fbox.clicked.connect(self.Mbox.toggle)
        self.Mbox.clicked.connect(self.Fbox.toggle)

        self.sigh_up.clicked.connect(self.checkIt)
        

        QtCore.QMetaObject.connectSlotsByName(window)

        window.setTabOrder(self.Fname, self.Lname)
        window.setTabOrder(self.Lname, self.Uname)
        window.setTabOrder(self.Uname, self.SchoolL)
        window.setTabOrder(self.SchoolL, self.GradeL)
        window.setTabOrder(self.GradeL, self.ClassesL)
        window.setTabOrder(self.ClassesL, self.Rclass)
        window.setTabOrder(self.Rclass, self.Year)
        window.setTabOrder(self.Year, self.MonthL)
        window.setTabOrder(self.MonthL, self.DayL)
        window.setTabOrder(self.DayL, self.Fbox)
        window.setTabOrder(self.Fbox, self.Mbox)
        window.setTabOrder(self.Mbox, self.Roles)
        window.setTabOrder(self.Roles, self.sigh_up)

        
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate

        window.setWindowTitle(_translate("Information", "Information"))

        self.Fname.setPlaceholderText(_translate("Information", "First name"))

        self.Info.setText(_translate("Information", "Your information"))

        self.Lname.setPlaceholderText(_translate("Information", "Last name"))

        self.Uname.setPlaceholderText(_translate("Information", "Username"))

        self.LRclass.setText(_translate("Information", "Research Class"))

        self.LBirh.setText(_translate("Information", "Birthday"))

        self.Year.setPlaceholderText(_translate("Information", "Year"))

        self.Bslash.setText(_translate("Information", "/"))

        self.Bslash_2.setText(_translate("Information", "/"))

        self.Fbox.setText(_translate("Information", "Female"))

        self.Mbox.setText(_translate("Information", "Male"))

        self.Roles.setText(_translate("Information", "I ma agree with the roles"))

        self.sigh_up.setText(_translate("Information", "sigh-up"))

        
        self.Rclass.setCurrentText(_translate("Information", "Biology"))
        self.Rclass.setItemText(0, _translate("Information", "Biology"))
        self.Rclass.setItemText(1, _translate("Information", "Chemistry"))
        self.Rclass.setItemText(2, _translate("Information", "Computer"))
        self.Rclass.setItemText(3, _translate("Information", "Filmmaking"))
        self.Rclass.setItemText(4, _translate("Information", "Mechatronic"))
        self.Rclass.setItemText(5, _translate("Information", "Physics"))
        self.Rclass.setItemText(6, _translate("Information", "I do not have"))

        
    def on_combo_activated_1(self):
        self.GradeL.clear()
        self.School = self.SchoolL.currentText()
        self.GradeL.addItems(school_info[self.School])
        self.on_combo_activated_2()
        
    def on_combo_activated_2(self):
        self.ClassesL.clear()
        self.Grade = self.GradeL.currentText()
        self.ClassesL.addItems(school_info[self.School][self.Grade])

    def activ_month(self):
        self.month = self.MonthL.currentText()
        self.DayL.clear()


        
        self.validM = Months[self.month]

       
        for i in self.validM:
            
            
            self.DayL.addItem(i)
        
    def checkIt(self):
       
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("QLabel{ color: green}")
        self.MSGtext = 'You set your information succesfuly!'


       
        if not self.Roles.isChecked():
           
    
            msg.setIcon(QMessageBox.Critical)
               
            msg.setStyleSheet("QLabel{ color: red}")
            
            self.MSGtext = 'You did not check the Roles'
            
       
        

        
        if not self.Fname.text() == '':
            self.Name = self.Fname.text()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("QLabel{ color: red}")
            self.MSGtext = 'You did not write your name'

     
        if not self.Lname.text() == '':
            self.Family = self.Lname.text()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("QLabel{ color: red}")
            self.MSGtext = 'You did not write your family name'

        
        if not self.Uname.text() == '':  
            self.Username = self.Uname.text()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("QLabel{ color: red}")
            self.MSGtext = 'You did not write your username'
     
        if not self.SchoolL.currentText() == '..':
            self.School = self.SchoolL.currentText()
            self.Grade = self.GradeL.currentText()
            self.Class = self.ClassesL.currentText()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("QLabel{ color: red}")
            self.MSGtext = 'You did not choice your school'
       
        
        self.RClass = self.Rclass.currentText()
        
        if not self.Year.text() == '':
            t = self.Year.text()
            
            self.year = self.Year.text()
            self.Month = self.MonthL.currentText()
            self.Day = self.DayL.currentText()

        
            if not t.isdigit():   
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet("QLabel{ color: red}")
                self.MSGtext = 'Plz choice a integear for the year option'
        else:
            
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("QLabel{ color: red}")
            self.MSGtext = 'You did not choose your year'

        
        if self.Mbox.isChecked():
            self.Gender = 'Man'
        else:
            self.Gender = 'Woman'
    
        
        msg.setText(self.MSGtext)
        msg.show()
        msg.exec_()
        if self.MSGtext == 'You set your information succesfuly!':
            self.next  = True
            window.close()
        


import sys
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QDialog()
Info_window = Infor(window)
    
window.show()
app.exec_()
