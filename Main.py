from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import sys
sys.path.append('D:\\h3project\\sigh-out')
sys.path.append('D:\\h3project\\Info')

from PyQt5_sighout import Sign_out, so_window, student_list


from StudentClass import student
from StudentList import student_list


#print(student, student_list, Sign_out, Infor)






app = QtWidgets.QApplication(sys.argv)


print(so_window.next, 'next')

if so_window.sign_in_pressed == True:
    

    
    #connect to the sign_in window
    print('!')


    
elif so_window.next == True:
    me = student_list[so_window.Name, so_window.Pass]
    
    print()
    from Infoes import Info_window
    print('o')
    me.Fname = Info_window.Name
    me.Lname = Info_window.Family
    me.Username = Info_window.Uname
    me.School = Info_window.School
    me.Grade = Info_window.Grade
    me.Class = Info_window.Class
    me.RClass = Info_window.RClass
    me.Year = Info_window.Year
    me.Month = Info_window.Month
    me.Day = Info_window.Day
    me.Gender = Info_window.Gender
    
    print('Welcome', me.username_sign, me.Class, me.Fname, me.Lname)
    



# sigh out window
