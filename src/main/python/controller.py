"""This module controls the whole process, it performs file conversion"""
from pathlib import Path
from PyQt5 import QtCore
from file_convertor import FileConvertor


# TODO Division by zero

class Controller(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self):
        super(Controller, self).__init__()
        self._convertor = FileConvertor()
        self._slots()

    def _slots(self):
        self._convertor.process_percent.connect(self._show_count_percent)

    def _show_count_percent(self, percent):
        print(percent)

    def run(self, file_list: list):
        """
        Method that is executed in another thread, converting files
        """
        # self.convertor.zip_convert(file_list, Path("None"), "Aboba")  # Convert to zip
        self._convertor.unzip_archive("D:/C_Project/7_Laba.zip", None)  # Unpack Zip
        self.finished.emit()
