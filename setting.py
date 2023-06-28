import sys
from setting_ui import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

class setting(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()

        self.setupUi(self)

        self.show()


app = QApplication(sys.argv)
window = setting()

window.setWindowFlags(Qt.FramelessWindowHint)


sys.exit(app.exec())

