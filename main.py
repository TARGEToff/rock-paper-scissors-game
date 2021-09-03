from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked(type):
    print(type)

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
    rockBtn.clicked.connect(lambda: clicked("rock"))
    paperBtn = QtWidgets.QPushButton(win)
    paperBtn.setText("Paper")
    paperBtn.move(195, 80)
    paperBtn.clicked.connect(lambda: clicked("paper"))
    scissorsBtn = QtWidgets.QPushButton(win)
    scissorsBtn.setText("Scissors")
    scissorsBtn.move(305, 80)
    scissorsBtn.clicked.connect(lambda: clicked("scissors"))

    win.show()
    sys.exit(app.exec_())


window()