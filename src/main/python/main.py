"""This module is the entry point, and represents the application logic"""
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore
from zip_per_ui import UiZipPer
from controller import Controller
import sys
import json

LIGHT_THEME = "light"
DARK_THEME = "dark"


class Main(ApplicationContext):
    def __init__(self):
        super().__init__()
        colors_dict = self._get_color_from_json()

        self._thread = QtCore.QThread()
        self._controller = Controller()
        self._controller.moveToThread(self._thread)

        self._window_UI = UiZipPer(self._controller, colors_dict)
        self._window_UI.show()

        self._thread.start()
        self._slots()

    def run(self):
        return self.app.exec_()

    def _slots(self):
        self._controller.finished.connect(self.get_controller_result)
        self._window_UI.signal_to_change_theme.connect(self._change_theme)

    def _get_color_from_json(self):
        with open(self.get_resource("color_data.json")) as json_file:
            json_dict = json.load(json_file)
            style_type = json_dict['style']
            if style_type == LIGHT_THEME:
                result_dict = json_dict['colors_light']
            else:
                result_dict = json_dict['colors_dark']
        return result_dict

    def get_controller_result(self):
        # self._window_UI.open_main_page()
        print("Done")

    def _change_theme(self):
        # Replace color-style in json
        with open(self.get_resource("color_data.json")) as json_file:
            data = json.load(json_file)
            # If a dark theme is installed, set a light one, and vice versa
            data["style"] = DARK_THEME if data["style"] == LIGHT_THEME else LIGHT_THEME

        with open(self.get_resource("color_data.json"), "w") as json_file:
            json.dump(data, json_file)

        # Set new color for UI
        self._window_UI.setup_colors(self._get_color_from_json())
        self._window_UI.set_stylesheet_by_current_colors()


if __name__ == "__main__":
    appctxt = Main()
    exit_code = appctxt.run()
    sys.exit(exit_code)

    # app = ApplicationContext()
    # a = Main()
    # exit_code = app.app.exec()
    # sys.exit(exit_code)
