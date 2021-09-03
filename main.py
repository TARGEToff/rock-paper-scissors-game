from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(600, 300, 500, 400)
    win.setWindowTitle("Rock paper scissors")

    title = QtWidgets.QLabel(win)
    title.setText("Rock paper scissors")
    title.move(200, 30)


    win.show()
    sys.exit(app.exec_())


window()