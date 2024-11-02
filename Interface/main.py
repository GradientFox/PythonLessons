from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python")
        self.setBaseSize(QSize(800, 800))
        wd = QWidget(self)
        wd.setFocus()
        l = QVBoxLayout(wd)
        sc = QLabel()
        sr = QLabel()
        sc.setBaseSize(QSize(100, 100))
        sr.setBaseSize(QSize(200, 150))
        pal1 = QPalette()
        pal1.setColor(QPalette.Background, QColor('red'))
        sc.setPalette(pal1)
        l.addWidget(sc)
        l.addWidget(sr)
        wd.setLayout(l)
        self.setCentralWidget(wd)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()