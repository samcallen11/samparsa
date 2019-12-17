


from PyQt5 import QtCore, QtGui, QtWidgets


class Class_window(QtWidgets.QMainWindow):
    def __init__(self, teachers):
        print('1')
        QtWidgets.QWidget.__init__(self)
        print(2)
        self.setObjectName("self")
        self.resize(800, 600)
        self.setAnimated(True)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.SessionL = QtWidgets.QLabel(self.centralwidget)
        self.SessionL.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.SessionL.setObjectName("SessionL")

        self.NewsL = QtWidgets.QLabel(self.centralwidget)
        self.NewsL.setGeometry(QtCore.QRect(210, 10, 47, 21))
        self.NewsL.setObjectName("NewsL")

        self.InfoL = QtWidgets.QLabel(self.centralwidget)
        self.InfoL.setGeometry(QtCore.QRect(500, 10, 131, 20))
        self.InfoL.setObjectName("InfoL")

        self.ITB = QtWidgets.QTextBrowser(self.centralwidget)
        self.ITB.setGeometry(QtCore.QRect(500, 40, 256, 221))
        self.ITB.setObjectName("ITB")

        self.TeacherL = QtWidgets.QLabel(self.centralwidget)
        self.TeacherL.setGeometry(QtCore.QRect(520, 60, 47, 13))
        self.TeacherL.setObjectName("TeacherL")
        
        
        self.SnL = QtWidgets.QLabel(self.centralwidget)
        self.SnL.setGeometry(QtCore.QRect(580, 220, 121, 16))
        self.SnL.setObjectName("SnL")

        self.StudnetN = QtWidgets.QLabel(self.centralwidget)
        self.StudnetN.setGeometry(QtCore.QRect(580, 170, 101, 41))
        self.StudnetN.setObjectName("StudnetN")

        self.NLW = QtWidgets.QListWidget(self.centralwidget)
        self.NLW.setGeometry(QtCore.QRect(210, 40, 256, 221))
        self.NLW.setObjectName("NLW")

        self.SLW = QtWidgets.QListWidget(self.centralwidget)
        self.SLW.setGeometry(QtCore.QRect(10, 40, 141, 481))
        self.SLW.setObjectName("SLW")
        self.ILW = QtWidgets.QListWidget(self.centralwidget)

        self.ILW.setGeometry(QtCore.QRect(500, 90, 256, 81))
        self.ILW.setObjectName("ILW")

        for i in teachers:
            self.create_widget(self.ILW, i)

        self.SLW.raise_()

        self.SessionL.raise_()

        self.NewsL.raise_()

        self.InfoL.raise_()

        self.ITB.raise_()

        self.TeacherL.raise_()

        self.SnL.raise_()

        self.StudnetN.raise_()

        self.NLW.raise_()

        self.ILW.raise_()

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))

        self.menubar.setObjectName("menubar")

        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)

        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        
    def create_widget(self, w, text):
        itemN = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        widgetText = QtWidgets.QLabel(text)
        #widgetButton = QtWidgets.QPushButton("Push Me")
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(widgetText)
        #widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()

        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())

        w.addItem(itemN)
        w.setItemWidget(itemN, widget)

        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.SessionL.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:14pt;\">Sessions</span></p></body></html>"))
        self.NewsL.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:14pt;\">News</span></p></body></html>"))
        self.InfoL.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:14pt;\">Information</span></p></body></html>"))
        self.TeacherL.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:10pt;\">Techers</span></p></body></html>"))
        self.SnL.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:10pt;\">Number of student</span></p></body></html>"))
        self.StudnetN.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">0</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QMainWindow()
    ui = Class_window(self, ['hassan'])
    
    self.show()
    sys.exit(app.exec_())
