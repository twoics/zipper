"""This module is the entry point, and represents the application logic"""
from PyQt5 import QtCore
from zip_per_ui import UiZipPer
from controller import Controller
from base import BASE_CONTEXT
import sys


class Main:
    def __init__(self):
        self._thread = QtCore.QThread()
        self._controller = Controller()
        self._controller.moveToThread(self._thread)

        self._window_UI = UiZipPer(self._controller)
        self._window_UI.show()

        self._thread.start()
        self._slots()

    def _slots(self):
        self._controller.finished.connect(self._get_controller_result)

    def _get_controller_result(self):
        # self._window_UI.open_main_page()
        print("Done")


if __name__ == "__main__":
    main = Main()
    exit_code = BASE_CONTEXT.app.exec()
    sys.exit(exit_code)
