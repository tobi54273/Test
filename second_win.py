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
        self.name = QLabel("Введите ФИО")
        self.namefield = QLineEdit("")
        self.age = QLabel("Полных лет:")
        self.agefield = QLineEdit("")
        self.quest1 = QLabel("Ложитесь на спину и замерьте пульс за 15 секунд. Нажмите кнопку 'Начать новый тест', чтобы запустить таймер. Результат запишите в окошко")
        self.start_quest1 = QPushButton("Начать новый тест",self)
        self.res_quest1 = QLineEdit("результат")
        self.quest2 = QLabel("Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку 'Начать делать приседания'")
        self.start_quest2 = QPushButton("Начать делать приседания",self)
        self.res_quest2 = QLineEdit("результат")
        self.quest3 = QLabel("Ложитесь на спину и замерьте пульс за первые 15 секунд минуты, затем за последние 15 секунд. Нажмите на кнопку 'Начать финальный тест'")
        self.start_quest3 = QPushButton("Начать финальный тест",self)
        self.res_quest3 = QLineEdit("результат")
        self.final = QPushButton("Отправить результаты",self)
        self.vline.addWidget(self.name,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.namefield,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.age,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.agefield,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.quest1,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.start_quest1,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.res_quest1,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.quest2,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.start_quest2,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.res_quest2,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.quest3,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.start_quest3,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.res_quest3,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.final,alignment = Qt.AlignLeft)





