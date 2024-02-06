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
        # add 이미지 .scaledToWidth(800) => 큰해상도를 800으로 고정
        pixmap = QPixmap('./image/dog1.jpg').scaledToWidth(800)
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(self)
        lblSize.setFont(QFont('맑은고딕', 15)) # Font + Font Size
        lblSize.setStyleSheet('Color: #3333FF')
        lblSize.setText(f'{pixmap.width()}x{pixmap.height()}')
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로중앙정렬 | 세로 중앙정렬
        # kitty.jpg의 width heigth

        vbox = QVBoxLayout(self) # QtDesigner VerticalLayout 위젯 생성
        vbox.addWidget(lblImage) # VL에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # Form에 VL 추가와 동일

        lblSize.setSizeIncrement(200,50)
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setWindowIcon(QIcon('./image/iot.png'))
        self.setWindowTitle('Image Viewer')
        rect = QRect(300, 300, 300, 300) # x, y, w, hs
        self.setGeometry(rect) # 같은 이름의 함수를 여러개 선언해놓고 입맛에 맞게 골라 쓰는 BR(overloading)
        # self.setGeometry(300, 300, 300, 300)
        self.show() # showFullScreen 모니터 꽉 채워서 출력
        self.setCenter()

    def setCenter(self): #윈도우 앱을 화면에 정중앙에 위치  
        gm = self.frameGeometry() #윈도우 앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_react = app.desktop().screenGeometry()
    width, height = screen_react.width(), screen_react.height()
    print(width, 'x', height) # 활용도 높음
    inst = winApp()
    # inst.show()
    # inst.showFullscreen() -> 모니터를 꽉채워서 출력
    sys.exit(app.exec_()) # 종료시 리소스 변환등 효율
