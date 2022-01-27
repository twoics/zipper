"""This module controls the whole process, it performs file conversion"""
from pathlib import Path
from PyQt5 import QtCore
from typing import List
from src.main.python.controller.file_convertor import FileConvertor

# Operation mode
CREATE_ZIP_WITH_COMPRESS = 1
CREATE_ZIP_NOT_COMPRESS = 2
UNZIP = 3

PERCENT_COUNT = int
PATH_LIST = List[Path]


class Controller(QtCore.QObject):
    """This class represents the main logic control controller"""
    # A signal is sent to the main when the inverter finishes running
    finished = QtCore.pyqtSignal()
    # A signal is sent to the UI during work each time the amount of work done has been updated.
    percent_count = QtCore.pyqtSignal(PERCENT_COUNT)

    def __init__(self):
        super(Controller, self).__init__()
        self._convertor = FileConvertor()
        self._init_slots()

    def run(self, file_list: PATH_LIST, operation_mode: int, directory: Path, name: str) -> QtCore.pyqtSignal():
        """
        Method that is executed in another thread, converting files
        :param file_list: List of file paths
        :param operation_mode: Type of work (Creating an archive, extracting from an archive)
        :param directory: Directory where the result will be saved
        :param name: Name of the result folder/archive name
        :return: Send signal when the inverter finishes running
        """
        if operation_mode == CREATE_ZIP_WITH_COMPRESS:
            self._convertor.zip_convert(file_list, directory, name, compression=True)
        elif operation_mode == CREATE_ZIP_NOT_COMPRESS:
            self._convertor.zip_convert(file_list, directory, name, compression=False)
        else:
            self._convertor.unzip_archives(file_list, directory, name)
        self.finished.emit()

    def _init_slots(self) -> None:
        self._convertor.process_percent.connect(self._emit_count_percent)

    def _emit_count_percent(self, percent) -> QtCore.pyqtSignal():
        self.percent_count.emit(percent)
