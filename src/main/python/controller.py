"""This module controls the whole process, it performs file conversion"""
from pathlib import Path
from PyQt5 import QtCore
from file_convertor import FileConvertor

# Operation mode
CREATE_ZIP_WITH_COMPRESS = 1
CREATE_ZIP_NOT_COMPRESS = 2
UNZIP = 3

PERCENT_COUNT = int


# TODO Division by zero

class Controller(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    percent_count = QtCore.pyqtSignal(PERCENT_COUNT)

    def __init__(self):
        super(Controller, self).__init__()
        self._convertor = FileConvertor()
        self._slots()

    def _slots(self):
        self._convertor.process_percent.connect(self._show_count_percent)

    def _show_count_percent(self, percent):
        self.percent_count.emit(percent)

    def run(self, file_list: list, operation_mode, directory, name):
        """
        Method that is executed in another thread, converting files
        """
        print(operation_mode, directory, name)
        if operation_mode == CREATE_ZIP_WITH_COMPRESS:
            self._convertor.zip_convert(file_list, Path("None"), "Aboba", compression=True)
        elif operation_mode == CREATE_ZIP_NOT_COMPRESS:
            pass
        else:
            pass
            # self._convertor.unzip_archive("D:/test_folder/Aboba.zip", None, "aboba")  # Unpack Zip
        self.finished.emit()

        #   # Convert to zip
        # self._convertor.unzip_archive("C:/test_folder/Aboba.zip", None)  # Unpack Zip
        # TODO Change here
