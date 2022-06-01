"""This module is the entry point"""

# Standard library imports
import sys

# Third party imports
from PyQt5 import QtCore

# Local application imports
from ui.main_ui import UiZipPer
from controller.controller import Controller
from model.archiver import Archiver
from fbs_runtime.application_context.PyQt5 import ApplicationContext

BASE_CONTEXT = ApplicationContext()


class Main:
    """A class that gathers the main components of the application into one"""

    def __init__(self):
        """
        Initializing main components
        """
        self._window_UI = UiZipPer()
        self._archiver = Archiver()
        self._controller = Controller(self._window_UI, self._archiver, BASE_CONTEXT)

        self._thread = QtCore.QThread()
        self._controller.moveToThread(self._thread)

        self._window_UI.show()
        self._thread.start()


if __name__ == "__main__":
    main = Main()
    exit_code = BASE_CONTEXT.app.exec()
    sys.exit(exit_code)
