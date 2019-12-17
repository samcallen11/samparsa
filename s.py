# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\h3project\namayeshgah\Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append('D:\\h3project\\namayeshgah')
sys.path.append('D:\\h3project\\namayeshgah\\Class')
import datetime
today = datetime.datetime.today().weekday()
today = (today + 2) % 7
from ClassClass import Classes
from class_window import Class_window
from Main import me



me.ToDo = Classes[me.Class][today]

from PyQt5 import QtCore, QtGui, QtWidgets


class MWindow(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        
        self.setObjectName("self")
        self.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.Photo = QtWidgets.QFrame(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(20, 50, 161, 181))
        self.Photo.setAutoFillBackground(True)
        self.Photo.setStyleSheet("border-color: rgb(156, 234, 255);")
        self.Photo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Photo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Photo.setObjectName("Photo")

        self.PTB = QtWidgets.QTextBrowser(self.Photo)
        self.PTB.setGeometry(QtCore.QRect(0, 0, 161, 181))
        self.PTB.setStyleSheet("border-color: rgb(131, 187, 255);")
        self.PTB.setObjectName("PTB")

        self.Pphoto = QtWidgets.QLabel(self.Photo)
        self.Pphoto.setGeometry(QtCore.QRect(30, 30, 111, 91))
        self.Pphoto.setAutoFillBackground(False)
        self.Pphoto.setText("")
        self.Pphoto.setPixmap(QtGui.QPixmap("C:/Users/Win7/Documents/image PyQt5.png"))
        self.Pphoto.setObjectName("Pphoto")

        self.Pedit = QtWidgets.QPushButton(self.Photo)
        self.Pedit.setGeometry(QtCore.QRect(40, 140, 75, 23))
        self.Pedit.setObjectName("Pedit")

        self.ToDoTB = QtWidgets.QTextBrowser(self.centralwidget)
        self.ToDoTB.setGeometry(QtCore.QRect(235, 280, 541, 41))
        self.ToDoTB.setObjectName("ToDoTB")
        
        self.C3Text = me.ToDo[2].Name   
        self.C3 = QtWidgets.QPushButton(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(410, 340, 81, 23))
        self.C3.setFlat(True)
        self.C3.setObjectName("C3")
        self.C3.clicked.connect(lambda: self.class_click(me.ToDo[2], me))

        self.C4Text = me.ToDo[3].Name
        self.C4 = QtWidgets.QPushButton(self.centralwidget)
        self.C4.setGeometry(QtCore.QRect(500, 340, 81, 23))
        self.C4.setFlat(True)
        self.C4.setObjectName("C4")
        self.C4.clicked.connect(lambda: self.class_click(me.ToDo[3], me))
        

        self.C6Text = me.ToDo[5].Name
        self.C6 = QtWidgets.QPushButton(self.centralwidget)
        self.C6.setGeometry(QtCore.QRect(690, 340, 81, 23))
        self.C6.setFlat(True)
        self.C6.setObjectName("C6")
        self.C6.clicked.connect(lambda: self.class_click(me.ToDo[5], me))
        

        self.C5Text = me.ToDo[4].Name
        self.C5 = QtWidgets.QPushButton(self.centralwidget)
        self.C5.setGeometry(QtCore.QRect(590, 340, 81, 23))
        self.C5.setFlat(True)
        self.C5.setObjectName("C5")
        self.C5.clicked.connect(lambda: self.class_click(me.ToDo[4], me))
        

        self.C2Text = me.ToDo[1].Name
        self.C2 = QtWidgets.QPushButton(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(330, 340, 71, 23))
        self.C2.setFlat(True)
        self.C2.setObjectName("C2")
        self.C2.clicked.connect(lambda: self.class_click(me.ToDo[1], me))
        
        self.C1Text = me.ToDo[0].Name
        self.C1 = QtWidgets.QPushButton(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(240, 340, 81, 23))
        self.C1.setFlat(True)
        self.C1.setObjectName("C1")
        self.C1.clicked.connect(lambda: self.class_click(me.ToDo[0], me))
        
        self.ToDoTW = QtWidgets.QTableView(self.centralwidget)
        self.ToDoTW.setGeometry(QtCore.QRect(230, 280, 551, 111))
        self.ToDoTW.setGridStyle(QtCore.Qt.CustomDashLine)
        self.ToDoTW.setSortingEnabled(True)
        self.ToDoTW.setObjectName("ToDoTW")

        self.Classes = QtWidgets.QPushButton(self.centralwidget)
        self.Classes.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.Classes.setObjectName("Classes")

        self.MRCT = QtWidgets.QTextBrowser(self.centralwidget)
        self.MRCT.setGeometry(QtCore.QRect(230, 50, 261, 41))
        self.MRCT.setObjectName("MRCT")

        self.CNT = QtWidgets.QTextBrowser(self.centralwidget)
        self.CNT.setGeometry(QtCore.QRect(530, 50, 251, 41))
        self.CNT.setObjectName("CNT")

        self.ANT = QtWidgets.QTextBrowser(self.centralwidget)
        self.ANT.setGeometry(QtCore.QRect(20, 280, 161, 41))
        self.ANT.setObjectName("ANT")

        self.ApLW = QtWidgets.QListWidget(self.centralwidget)
        self.ApLW.setGeometry(QtCore.QRect(20, 320, 161, 251))
        self.ApLW.setObjectName("ApLW")
    
        self.MLW = QtWidgets.QListWidget(self.centralwidget)
        self.MLW.setGeometry(QtCore.QRect(230, 90, 261, 141))
        self.MLW.setObjectName("MLW")        
        
        self.CLW = QtWidgets.QListWidget(self.centralwidget)
        self.CLW.setGeometry(QtCore.QRect(530, 90, 251, 141))
        self.CLW.setObjectName("CLW")

        self.SeeAll = QtWidgets.QPushButton(self.centralwidget)
        self.SeeAll.setGeometry(QtCore.QRect(690, 290, 75, 23))
        self.SeeAll.setObjectName("SeeAll")


        
        # Create widget
        self.create_widget(self.MLW)
        self.create_widget(self.MLW)
        print('hi')
        self.ToDoTW.raise_()

        self.Photo.raise_()

        self.ToDoTB.raise_()

        self.C3.raise_()

        self.C4.raise_()


        self.C6.raise_()

        self.C5.raise_()


        self.C2.raise_()

        self.C1.raise_()

        self.Classes.raise_()

        self.MRCT.raise_()

        self.CNT.raise_()

        self.ANT.raise_()

        self.ApLW.raise_()

        self.MLW.raise_()

        self.CLW.raise_()

        self.SeeAll.raise_()

        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self)

        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    def create_widget(self, w):
        itemN = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        widgetText = QtWidgets.QLabel("I love PyQt!")
        widgetButton = QtWidgets.QPushButton("Push Me")
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(widgetText)
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()

        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())

        w.addItem(itemN)
        w.setItemWidget(itemN, widget)



    def class_click(self, Nclass, me):
        
        me.NowClass = Nclass
        
        self.switch_window.emit()
    def set_me(self):
        global me
        return me



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.Pedit.setText(_translate("self", "Edit"))
        self.ToDoTB.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">To Do</span></p></body></html>"))

        self.C3.setText(_translate("self", self.C3Text))
        self.C4.setText(_translate("self", self.C4Text))
        self.C6.setText(_translate("self", self.C5Text))
        self.C5.setText(_translate("self", self.C5Text))
        self.C2.setText(_translate("self", self.C2Text))
        self.C1.setText(_translate("self", self.C1Text))

        self.Classes.setText(_translate("self", "Classes"))
        self.MRCT.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">More Recent Class</span></p></body></html>"))
        self.CNT.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Classes News</span></p></body></html>"))
        self.ANT.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">App News</span></p></body></html>"))
        self.SeeAll.setText(_translate("self", "See All"))


                                                     


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QMainWindow()
    ui = MWindow(self)
    
    
    self.show()
    sys.exit(app.exec_())
