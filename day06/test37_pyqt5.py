# date : 20240205
# file : test37_pyqt5.py
# desc : pyqt5 이벤트 만들기 (signal)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        btn01 = QPushButton('Click', self)
        btn01.setGeometry(50, 100, 100, 40)
        btn01.clicked.connect(self.btn1_clicked) # 버튼 클릭하면(Signal) 버튼01_클릭ed2 함수 실행 시키겠다.

        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('Button Event!!')
        self.show()

    def btn1_clicked(self):
        QMessageBox.about(self, 'Button Click', 'You Clicked Button!!')

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self,'종료 확인','종료하실?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
if __name__ == '__main__': # main entry 확인 조건 추가 
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()