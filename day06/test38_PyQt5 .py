# date : 20240205
# file : test38_pyqt5.py
# desc : Qt디자이너 만든 UI 연동

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui',self) #QtDesinger에서 만든 UI를 load

    def closeEvent(self, QCloseEvent) -> None: # X버튼 종료확인
        re = QMessageBox.question(self,'종료 확인','종료하실?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        

    
if __name__ == '__main__':
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()