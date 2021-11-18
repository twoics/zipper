"""This module is the entry point, and represents the application logic"""
import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from ZipPerUI import UiZipPer


class Main:
    def __init__(self):
        window = UiZipPer()
        window.show()


if __name__ == "__main__":
    app = ApplicationContext()
    a = Main()
    exit_code = app.app.exec()
    sys.exit(exit_code)
