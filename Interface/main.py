from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])
app.setApplicationName("Hello, world!")
window = QWidget()

window.show()
app.exec()