from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random

def randomChoice(options=["rock", "paper", "scissors"]):
    return random.choice(options);


def clicked(userChoice, computerChoice):
    print(userChoice, computerChoice)

    if userChoice == computerChoice:
        print("tie")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(600, 300, 500, 200)
    win.setWindowTitle("Rock paper scissors")

    title = QtWidgets.QLabel(win)
    title.setText("Rock paper scissors")
    title.move(200, 30)

    rockBtn = QtWidgets.QPushButton(win)
    rockBtn.setText("Rock")
    rockBtn.move(85, 80)
    rockBtn.clicked.connect(lambda: clicked("rock", randomChoice()))
    paperBtn = QtWidgets.QPushButton(win)
    paperBtn.setText("Paper")
    paperBtn.move(195, 80)
    paperBtn.clicked.connect(lambda: clicked("paper", randomChoice()))
    scissorsBtn = QtWidgets.QPushButton(win)
    scissorsBtn.setText("Scissors")
    scissorsBtn.move(305, 80)
    scissorsBtn.clicked.connect(lambda: clicked("scissors", randomChoice()))

    win.show()
    sys.exit(app.exec_())


window()