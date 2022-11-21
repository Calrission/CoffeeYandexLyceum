from PyQt5.QtWidgets import QApplication, QMainWindow
from sys import argv, exit
from PyQt5 import uic
import sqlite3


def push_query_db_decorator(fun):
    def push_query_db(*args):
        with sqlite3.connect("coffee.db") as conn:
            cursor = conn.cursor()
            return fun(*args, cursor=cursor, conn=conn)

    return push_query_db


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        pass

    @push_query_db_decorator
    def insert_data_to_table_view(self, cursor: sqlite3.Cursor, conn: sqlite3.Connection):
        pass


if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec())
