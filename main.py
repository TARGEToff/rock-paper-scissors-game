from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random

def randomChoice(options=["rock", "paper", "scissors"]):
    return random.choice(options);


def clicked(userChoice, computerChoice, label):
    winners = {
        "rock": {
            "rock": "Tie",
            "paper": "You lost",
            "scissors": "You won",
        },
        "paper": {
            "rock": "You won",
            "paper": "Tie",
            "scissors": "You lost",
        },
        "scissors": {
            "rock": "You lost",
            "paper": "You won",
            "scissors": "Tie",
        },
    }

    winner = winners[userChoice][computerChoice]
    label.setText(winner)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(600, 300, 500, 200)
    win.setWindowTitle("Rock paper scissors")

    title = QtWidgets.QLabel(win)
    title.setText("Rock paper scissors")
    title.move(200, 30)
    winner = QtWidgets.QLabel(win)
    winner.move(225, 120)
    winner.setAlignment(Qt.AlignVCenter)

    rockBtn = QtWidgets.QPushButton(win)
    rockBtn.setText("Rock")
    rockBtn.move(85, 80)
    rockBtn.clicked.connect(lambda: clicked("rock", randomChoice(), winner))
    paperBtn = QtWidgets.QPushButton(win)
    paperBtn.setText("Paper")
    paperBtn.move(195, 80)
    paperBtn.clicked.connect(lambda: clicked("paper", randomChoice(), winner))
    scissorsBtn = QtWidgets.QPushButton(win)
    scissorsBtn.setText("Scissors")
    scissorsBtn.move(305, 80)
    scissorsBtn.clicked.connect(lambda: clicked("scissors", randomChoice(), winner))

    win.show()
    sys.exit(app.exec_())


window()