# date : 20240206
# file : test41_pyqt.py
# desc : 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class winApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI() 

    def initUI(self):
        lblSize = QLabel(self)
        lblSize.setText('Sample')
        lblSize.setSizeIncrement(200,50)
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setWindowIcon(QIcon('./image/iot.png'))
        self.setWindowTitle('Image Viewer')
        self.setGeometry(300, 300, 300, 300)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_react = app.desktop().screenGeometry()
    width, height = screen_react.width(), screen_react.height()
    print(width, 'x', height) # 활용도 높음
    inst = winApp()
    inst.show()
    sys.exit(app.exec_()) # 종료시 리소스 변환등 효율
