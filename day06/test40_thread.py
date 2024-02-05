# date : 20240205
# file : test40_Thread.py
# desc : Qt에서 Thread 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class BackWorker(QThread): #PyQt에서 스레드 클래스 상속
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent # BackWorker 에 사용할 멤버 변수

    def run(self) -> None: # Thread 실행
        # Thread 동작할 내용
        maxVal = 100
        self.parent.pgbTask.setValue(0) # 프로그레스바 0에서 시작
        self.parent.pgbTask.setRange(0, maxVal-1) # 0~100
        for i in range(maxVal): # 0 ~ 100
           print_str = f'No Thread 출력 > {i}'
           print(print_str)
           self.txbLog.append(print_str)
           self.pgbTask.setValue(i)
    
    