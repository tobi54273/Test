from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Тест Руфье")
main_win.resize(1200,1000)
vline = QVBoxLayout()


name = QLabel("Введите ФИО")
namefield = QLineEdit("")



age = QLabel("Полных лет:")
agefield = QLineEdit("")



quest1 = QLabel("Ложитесь на спину и замерьте пульс за 15 секунд. Нажмите кнопку 'Начать новый тест', чтобы запустить таймер. Результат запишите в окошко")
start_quest1 = QPushButton("Начать новый тест")
res_quest1 = QLineEdit("результат")



quest2 = QLabel("Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку 'Начать делать приседания'")
start_quest2 = QPushButton("Начать делать приседания")
res_quest2 = QLineEdit("результат")


quest3 = QLabel("Ложитесь на спину и замерьте пульс за первые 15 секунд минуты, затем за последние 15 секунд. Нажмите на кнопку 'Начать финальный тест'")
start_quest3 = QPushButton("Начать финальный тест")
res_quest3 = QLineEdit("результат")


final = QPushButton("Отправить результаты")
vline.addWidget(name,alignment = Qt.AlignLeft)
vline.addWidget(name,alignment = Qt.AlignLeft)
vline.addWidget(namefield,alignment = Qt.AlignLeft)
vline.addWidget(age,alignment = Qt.AlignLeft)
vline.addWidget(agefield,alignment = Qt.AlignLeft)
vline.addWidget(quest1,alignment = Qt.AlignLeft)
vline.addWidget(start_quest1,alignment = Qt.AlignLeft)
vline.addWidget(res_quest1,alignment = Qt.AlignLeft)
vline.addWidget(quest2,alignment = Qt.AlignLeft)
vline.addWidget(start_quest2,alignment = Qt.AlignLeft)
vline.addWidget(res_quest2,alignment = Qt.AlignLeft)
vline.addWidget(quest3,alignment = Qt.AlignLeft)
vline.addWidget(start_quest3,alignment = Qt.AlignLeft)
vline.addWidget(res_quest3,alignment = Qt.AlignLeft)
main_win.setLayout(vline)
main_win.show()
name.show()
app.exec_()
