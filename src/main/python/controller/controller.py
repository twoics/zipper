"""This module controls the whole process, it performs file conversion"""

# Standard library imports
from typing import List
from pathlib import Path

# Third party imports
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer

# Local application imports
from src.main.python.ui.ui_abstract import IView
from src.main.python.controller.abstract_archiver import IArchiver

# Operation mode
CREATE_ZIP_WITH_COMPRESS = 1
CREATE_ZIP_NOT_COMPRESS = 2
UNZIP = 3

PERCENT_COUNT = int
PATH_LIST = List[Path]

# How long the application waits after completing the task to switch to the home screen (ms)
WAITING_TIME = 1000


class Controller(QtCore.QObject):
    """This class represents the main logic control controller"""

    def __init__(self, view: IView, model: IArchiver):
        super(Controller, self).__init__()

        # Init ui and logic
        self._view = view
        self._convertor = model

        # Init main signals from view and logic
        self._start_processing_signal = view.get_processing_signal()
        self._process_signal = model.get_process_signal()

        # A timer that starts when the files processing is finished,
        # when it expires, the main application window will open
        self._timer = QTimer()

        self._init_slots()

    def run(self, file_list: PATH_LIST, operation_mode: int, directory: Path, name: str) -> None:
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
        else:  # UNZIP
            self._convertor.unzip_archives(file_list, directory, name)
        self._timer.start(WAITING_TIME)

    def _reset_all(self) -> None:
        """
        Resets the UI, clearing the
        fields and returns the start page
        :return: None
        """
        self._view.reset_ui()
        self._timer.stop()

    def _init_slots(self) -> None:
        """
        Initializing signal slots
        :return: None
        """
        self._process_signal.connect(self._view.set_progress_value)

        self._start_processing_signal.connect(self.run)

        # When the timer expires, reset everything and open the main window
        self._timer.timeout.connect(self._reset_all)
