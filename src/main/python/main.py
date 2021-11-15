import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow
from ZipPerUI import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.ui.rarPack.clicked.connect(self.tmp_open_second_window)
        self.ui.zipPack.clicked.connect(self.tmp_open_second_window)
        self.ui.unpack.clicked.connect(self.tmp_open_second_window)
        self.ui.convert.clicked.connect(self.tmp_open_second_window)
        self.ui.pushButton.clicked.connect(self.tmp_open_main_window)

    def tmp_open_second_window(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def tmp_open_main_window(self):
        self.ui.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec()  # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)
