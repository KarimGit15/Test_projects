from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget,QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton
from random import *


app = QApplication([])
main_win = QWidget() # Окно
main_win.resize(400, 200)
 
rand = randint(1, 5)
rand = str(rand)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText("Ты выиграл!")
    victory_win.exec_()


def show_lose():
    victory_win = QMessageBox()
    victory_win.setText("Ты проиграл!")
    victory_win.exec_()



main_win.setWindowTitle("Испытай удачу !")

v_line = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

# Кнопки
button_1 = QPushButton(str(1))
button_2 = QPushButton(str(2))
button_3 = QPushButton(str(3))
button_4 = QPushButton(str(4))
button_5 = QPushButton(str(5))

buttons = [button_1, button_2, button_3, button_4, button_5] #Список
shuffle(buttons) #перемешивание элементов списка
buttons[0].clicked.connect(show_win)
buttons[1].clicked.connect(show_lose)
buttons[2].clicked.connect(show_lose)
buttons[3].clicked.connect(show_lose)
buttons[4].clicked.connect(show_lose)



#Расстановка по линиям
layoutH1.addWidget(button_1, alignment = Qt.AlignCenter)
layoutH1.addWidget(button_2, alignment = Qt.AlignCenter)
layoutH2.addWidget(button_3, alignment = Qt.AlignCenter)
layoutH3.addWidget(button_4, alignment = Qt.AlignCenter)
layoutH3.addWidget(button_5, alignment = Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)


main_win.show()
app.exec_()