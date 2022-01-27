"""This module is the entry point"""

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from src.main.python.ui.zip_per_ui import UiZipPer
from src.main.python.controller.controller import Controller
from src.main.python.model.base import BASE_CONTEXT
import sys

WAITING_TIME = 1000  # How long the app waits after shutdown to switch to the home screen (ms)


class Main:
    """A class that gathers the main components of the application into one"""

    def __init__(self):
        self._thread = QtCore.QThread()
        self._controller = Controller()
        self._controller.moveToThread(self._thread)
        self._timer = QTimer()

        self._window_UI = UiZipPer(self._controller)
        self._window_UI.show()

        self._thread.start()
        self._init_slots()

    def _init_slots(self):
        self._controller.finished.connect(self._get_controller_result)
        self._timer.timeout.connect(self._open_main_page)

    def _get_controller_result(self):
        self._timer.start(WAITING_TIME)

    def _open_main_page(self):
        self._window_UI.open_main_window_after_shutdown()
        self._timer.stop()


if __name__ == "__main__":
    main = Main()
    exit_code = BASE_CONTEXT.app.exec()
    sys.exit(exit_code)
