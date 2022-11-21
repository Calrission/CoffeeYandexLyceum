from PyQt5.QtWidgets import QApplication, QMainWindow
from sys import argv, exit
from PyQt5 import uic


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        pass


if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec())
