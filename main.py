import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False

        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.flag = False

    def draw(self, qp):
        for i in range(random.randint(1, 10)):
            qp.setPen(QPen(QColor(random.randint(0, 255), random.randint(0, 255),
                                  random.randint(0, 155)), 10, Qt.SolidLine))
            rad = random.randint(10, 100)
            cor_X = random.randint(0, 740)
            cor_Y = random.randint(0, 510)
            qp.drawEllipse(cor_X, cor_Y, rad, rad, )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    ex.show()
    sys.exit(app.exec())
