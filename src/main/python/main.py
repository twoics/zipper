"""This module is the entry point, and represents the application logic"""
import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore
from zip_per_ui import UiZipPer
from controller import Controller


class Main:
    def __init__(self):
        self._window_UI = UiZipPer()
        self._window_UI.show()

        self.thread = QtCore.QThread()
        self._controller = Controller()

        self._controller.moveToThread(self.thread)

        self.thread.start()
        self._slots()

    def _slots(self):
        self._window_UI.generate_signal.connect(self._controller.run)
        self._controller.finished.connect(self.get_controller_result)

    def get_controller_result(self):
        print("Done")


if __name__ == "__main__":
    app = ApplicationContext()
    a = Main()
    exit_code = app.app.exec()
    sys.exit(exit_code)
