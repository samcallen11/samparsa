# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\h3project\namayeshgah\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.append('D:\\h3project\\namayeshgah')
import datetime
today = datetime.datetime.today().weekday()
today = (today + 2) % 7

print(today, 'today')


from Main import me
print('salam')
me.ToDo = me.Class[today]




from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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

        C3Text = me.ToDo[2]
        self.C3 = QtWidgets.QPushButton(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(410, 340, 81, 23))
        self.C3.setFlat(True)
        self.C3.setObjectName("C3")

        C4Text = me.ToDo[3]
        self.C4 = QtWidgets.QPushButton(self.centralwidget)
        self.C4.setGeometry(QtCore.QRect(500, 340, 81, 23))
        self.C4.setFlat(True)
        self.C4.setObjectName("C4")

        C6Text = me.ToDo[5]
        self.C6 = QtWidgets.QPushButton(self.centralwidget)
        self.C6.setGeometry(QtCore.QRect(690, 340, 81, 23))
        self.C6.setFlat(True)
        self.C6.setObjectName("C6")

        C5Text = me.ToDo[4]
        self.C5 = QtWidgets.QPushButton(self.centralwidget)
        self.C5.setGeometry(QtCore.QRect(590, 340, 81, 23))
        self.C5.setFlat(True)
        self.C5.setObjectName("C5")
        
        C2Text = me.ToDo[1]
        self.C2 = QtWidgets.QPushButton(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(330, 340, 71, 23))
        self.C2.setFlat(True)
        self.C2.setObjectName("C2")

        C1Text = me.ToDo[0]
        self.C1 = QtWidgets.QPushButton(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(240, 340, 81, 23))
        self.C1.setFlat(True)
        self.C1.setObjectName("C1")

        self.ToDoTW = QtWidgets.QTableView(self.centralwidget)
        self.ToDoTW.setGeometry(QtCore.QRect(230, 280, 551, 111))
        self.ToDoTW.setGridStyle(QtCore.Qt.CustomDashLine)
        self.ToDoTW.setSortingEnabled(True)
        self.ToDoTW.setObjectName("ToDoTW")

        self.Classes = QtWidgets.QPushButton(self.centralwidget)
        self.Classes.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.Classes.setObjectName("Classes")

        self.MRC = QtWidgets.QFrame(self.centralwidget)
        self.MRC.setGeometry(QtCore.QRect(230, 50, 261, 181))
        self.MRC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MRC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MRC.setObjectName("MRC")

        self.MRCTB = QtWidgets.QTextBrowser(self.MRC)
        self.MRCTB.setGeometry(QtCore.QRect(0, 40, 261, 141))
        self.MRCTB.setObjectName("MRCTB")

        self.MRCT = QtWidgets.QTextBrowser(self.MRC)
        self.MRCT.setGeometry(QtCore.QRect(0, 0, 261, 41))
        self.MRCT.setObjectName("MRCT")

        self.MRCSA = QtWidgets.QScrollArea(self.MRC)
        self.MRCSA.setGeometry(QtCore.QRect(20, 50, 221, 121))
        self.MRCSA.setWidgetResizable(True)
        self.MRCSA.setObjectName("MRCSA")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.MRCSA.setWidget(self.scrollAreaWidgetContents)
        self.MRCSA.raise_()
        self.MRCTB.raise_()
        self.MRCT.raise_()

        self.CN = QtWidgets.QFrame(self.centralwidget)
        self.CN.setGeometry(QtCore.QRect(520, 50, 261, 181))
        self.CN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CN.setObjectName("CN")

        self.CNTB = QtWidgets.QTextBrowser(self.CN)
        self.CNTB.setGeometry(QtCore.QRect(0, 40, 261, 151))
        self.CNTB.setObjectName("CNTB")

        self.CNT = QtWidgets.QTextBrowser(self.CN)
        self.CNT.setGeometry(QtCore.QRect(0, 0, 261, 41))
        self.CNT.setObjectName("CNT")

        self.CNSA = QtWidgets.QScrollArea(self.CN)
        self.CNSA.setGeometry(QtCore.QRect(20, 50, 221, 121))
        self.CNSA.setWidgetResizable(True)
        self.CNSA.setObjectName("CNSA")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 219, 119))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.CNSA.setWidget(self.scrollAreaWidgetContents_2)
        self.CNSA.raise_()

        self.CNTB.raise_()

        self.CNT.raise_()

        self.AN = QtWidgets.QFrame(self.centralwidget)
        self.AN.setGeometry(QtCore.QRect(20, 270, 161, 281))
        self.AN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AN.setObjectName("AN")

        self.ANTB = QtWidgets.QTextBrowser(self.AN)
        self.ANTB.setGeometry(QtCore.QRect(0, 40, 161, 241))
        self.ANTB.setObjectName("ANTB")

        self.ANT = QtWidgets.QTextBrowser(self.AN)
        self.ANT.setGeometry(QtCore.QRect(0, 0, 161, 41))
        self.ANT.setObjectName("ANT")

        self.ANSA = QtWidgets.QScrollArea(self.AN)
        self.ANSA.setGeometry(QtCore.QRect(20, 60, 131, 201))
        self.ANSA.setWidgetResizable(True)
        self.ANSA.setObjectName("ANSA")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 129, 199))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")

        self.ANSA.setWidget(self.scrollAreaWidgetContents_3)
        self.ANSA.raise_()

        self.ANTB.raise_()

        self.ANT.raise_()

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

        self.MRC.raise_()

        self.CN.raise_()

        self.AN.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Pedit.setText(_translate("MainWindow", "Edit"))
        self.ToDoTB.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">To Do</span></p></body></html>"))
        self.C3.setText(_translate("MainWindow", C3Text))
        self.C4.setText(_translate("MainWindow", C4Text))
        self.C6.setText(_translate("MainWindow", C6Text))
        self.C5.setText(_translate("MainWindow", C5Text))
        self.C2.setText(_translate("MainWindow", C2Text))
        self.C1.setText(_translate("MainWindow", C1Text))
        self.Classes.setText(_translate("MainWindow", "Classes"))
        self.MRCT.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">More Recent Class</span></p></body></html>"))
        self.CNT.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Classes News</span></p></body></html>"))
        self.ANT.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">App News</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
