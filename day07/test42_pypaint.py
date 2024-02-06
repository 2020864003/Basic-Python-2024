# date : 20240206
# file : test42_pypaint.py
# desc : 그림판

import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class winApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI() 
        self.initSignal()


    def initUI(self): # 화면 초기화
        uic.loadUi('./day07/pyPaint.ui', self)
        self.setWindowIcon(QIcon('./image/iot.png'))
        self.setWindowTitle('Drawing Painting')
        # canvas 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;')
        self.btn_blue.setStyleSheet('background:blue;')
        self.btn_red.setStyleSheet('background:red;')
        
        self.show()
        self.setCenter()

    def initSignal(self): # 동작 초기화
        self.btn_black.clicked.connect(self.btnBlackClicked)
        self.btn_blue.clicked.connect(self.btnBlueClicked)
        self.btn_red.clicked.connect(self.btnRedClicked)
        self.btn_clear.clicked.connect(self.btnClearClicked)
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSavedCliced)

    def btnLoadClicked(self):
        image = QFileDialog.getOpenFileName(None, 'Image Load', '', 'Image File(*.jpg; *.png)')
        imagePath = image[0]
        # print(imagePath)
        pixmap = QPixmap(imagePath).scaledToHeight(381) # 파일경로에 있는 이미지를 읽어서 객체에 업로드
    
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # image를 라벨 크기 맞추기
    
    def btnSavedCliced(self):
        filePath, _ = QFileDialog.getSaveFileName(self,'Image Save', '', 'Image File(*.jpg; *.png)') 
        # print(filePath)
        if filePath == '' :
            return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)

    def buttonClicked(self):
        btn_val = self.sender().objectName()
        print(btn_val)
        if btn_val == 'btn_black': # Black Button Click
            self.brushColor = Qt.black
        elif btn_val == 'btn_red': # Red Button Click
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue': # Blue Button Click
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear':
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)


    def btnBlackClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_black
        print(btn_val)
        self.brushColor = Qt.black

    def btnBlueClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_blue
        print(btn_val)
        self.brushColor = Qt.blue

    def btnRedClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_red
        print(btn_val)    
        self.brushColor = Qt.red

    def btnClearClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_clear
        print(btn_val)   # btn_clear
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)
        # print('All Erase')


    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap()) # 
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update() # 화면 Update


    def setCenter(self): #윈도우 앱을 화면에 정중앙에 위치  
        gm = self.frameGeometry() #윈도우 앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = winApp()
    sys.exit(app.exec_())