from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from instr import *
class TestWin(QWidget):
    def __init__(self):
        QWidget().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
            self.vline = QVBoxLayout()
            self.l1 = QLabel("Индекс Руфье:")
            self.vline.addWidget(self.l1,alignment = Qt.AlignCenter)
            self.l2 = QLabel("Работоспособность")
            self.vline.addWidget(self.l1,alignment = Qt.AlignCenter)