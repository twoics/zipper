"""This module is the entry point"""

# Standard library imports
import sys

# Third party imports
from PyQt5 import QtCore

# Local application imports
from ui.zip_per_ui import UiZipPer
from controller.controller import Controller
from model.base import BASE_CONTEXT
from controller.file_convertor import Archiver


class Main:
    """A class that gathers the main components of the application into one"""

    def __init__(self):
        self._window_UI = UiZipPer()
        self._archiver = Archiver()
        self._controller = Controller(self._window_UI, self._archiver)

        self._thread = QtCore.QThread()
        self._controller.moveToThread(self._thread)

        self._window_UI.show()
        self._thread.start()


if __name__ == "__main__":
    main = Main()
    exit_code = BASE_CONTEXT.app.exec()
    sys.exit(exit_code)
