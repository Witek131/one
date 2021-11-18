#coding: utf-8
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

    def mousePressEvent(self, event):
        self.coords.setText(f"Координаты:{event.x()}, {event.y()}")
        if (event.button() == Qt.LeftButton):
            self.btn.setText("Левая")
        elif (event.button() == Qt.RightButton):
            self.btn.setText("Правая")
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

        self.btn = QLabel(self)
        self.btn.setText("Никакая")
        self.btn.move(30, 50)

    def mousePressEvent(self, event):
        self.coords.setText(f"Координаты:{event.x()}, {event.y()}")
        if (event.button() == Qt.LeftButton):
            self.btn.setText("Левая")
        elif (event.button() == Qt.RightButton):
            self.btn.setText("Правая")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())