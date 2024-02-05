# date : 20240205
# file : test37_pyqt5.py
# desc : pyqt5 이벤트 만들기 (signal)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        btn01 = QPushButton('Click', self)
        btn01.setGeometry(50, 100, 100, 40)

        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('Button Event!!')
        self.show()


loop = QApplication(sys.argv)
instance = qtwin_exam()
loop.exec_()