# date : 20240206
# file : test42_pypaint.py
# desc : 그림판

import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class winApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI() 
        self.initSignal()


    def initUI(self):
        uic.loadUi('./day07/pyPaint.ui', self)
        self.setWindowIcon(QIcon('./image/iot.png'))
        self.setWindowTitle('Drawing Painting')
        self.show()
        self.setCenter()

    def initSignal(self):
        self.btn_black.clicked.connect(self.btnBlackClicked)
        self.btn_blue.clicked.connect(self.btnBlueClicked)
        self.btn_red.clicked.connect(self.btnRedClicked)
        self.btn_clear.clicked.connect(self.btnClearClicked)


    def btnBlackClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_black
        print(btn_val)

    def btnBlueClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_blue
        print(btn_val)

    def btnRedClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_red
        print(btn_val)    
    
    def btnClearClicked(self):
        print('All Erase')


    def setCenter(self): #윈도우 앱을 화면에 정중앙에 위치  
        gm = self.frameGeometry() #윈도우 앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = winApp()
    sys.exit(app.exec_())