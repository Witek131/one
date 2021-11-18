import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from UI1 import Ui_MainWindow


class DBSample(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect("films_db.sqlite")
        self.setupUi(self)
        self.pushButton.clicked.connect(self.select_data)

        # По умолчанию будем выводить все данные из таблицы films
        def select_data(self):
            try:
                reg = 'select * from films where {}=={}'.format(self.params.get(self.comon
                ' '))
                # Получим результат запроса,
                # который ввели в текстовое поле
                query = self.textEdit.toPlainText()
                res = self.connection.cursor().execute(query).fetchall()
                # Заполним размеры таблицы
                self.tableWidget.setColumnCount(5)
                self.tableWidget.setRowCount(0)
                # Заполняем таблицу элементами
                for i, row in enumerate(res):
                    self.tableWidget.setRowCount(
                        self.tableWidget.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(str(elem)))

        def select_data(self):

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = DBSample()
        ex.show()
        sys.exit(app.exec())
