from pathlib import Path
from PyQt5 import QtCore


class Controller(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self):
        super(Controller, self).__init__()

    def run(self, file_list: list):
        for i in range(1000000):
            print(i)
        print(file_list)
        self.finished.emit()
