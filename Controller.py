import PyQt5
from PyQt5 import QtWidgets, QtCore

from s import MWindow
import sys
sys.path.append('D:\\h3project\\namayeshgah\\Class')
from class_window import Class_window
class Controller:

    def __init__(self):
        pass

    def show_login(self):
        
        self.sw = MWindow()
        
        self.sw.switch_window.connect(self.show_main)
        self.sw.show()
        
    def show_main(self):
        
        
        
        print(1)
        me = self.sw.set_me()
        print(2)
        self.cw = Class_window(me.NowClass.Teachers)
        print(3)
        self.sw.close()
        print(4)
        self.cw.show()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

  
        
