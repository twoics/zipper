"""This module implements an element for a list of files"""

# Standard library imports
from pathlib import Path

# Third party imports
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QFileIconProvider


class _QCustomQWidget(QWidget):
    """
    Class of custom element QListWidget, has an icon and text, icon and text, the icon is selected from the system
    for a specific file type, you can set the color of the text
    """
    COLOR_ARRAY = [int, int, int]

    def __init__(self, txt_color: COLOR_ARRAY = None):
        """
        Initialization
        :param txt_color: Optional parameter - text color: array of 3 rgb elements, each element must be < 256.
        """
        super(_QCustomQWidget, self).__init__()

        if txt_color and (len(txt_color) != 3 or not all(color < 256 for color in txt_color)):
            raise Exception("Color list must have 3 elements: [red, green, blue] and they must be <= 255")

        self._text_color = txt_color

        self._horizontal_layout = QHBoxLayout()

        self._file_name = QLabel()
        self._file_icon = QLabel()

        self._horizontal_layout.addWidget(self._file_icon, 0)
        self._horizontal_layout.addWidget(self._file_name, 1)

        self.setLayout(self._horizontal_layout)

        if self._text_color:
            red, green, blue = self._text_color
            self._file_name.setStyleSheet(f'''
                color: rgb({red}, {green}, {blue});''')
        self.setStyleSheet(f"background-color: rgb(0, 0, 0, 0);")  # Set alpha to null for correct view

    def set_file_icon(self, path_to_file: Path) -> None:
        """
        Set icon from system icons
        :param path_to_file: Way to file
        :type path_to_file: Path
        :return: None
        """
        file_info = QtCore.QFileInfo(str(path_to_file))

        icon_provider = QFileIconProvider()
        icon = icon_provider.icon(file_info)
        pixmap = icon.pixmap(QSize(16, 16))
        self._file_icon.setPixmap(pixmap)

    def set_file_name(self, file: Path) -> None:
        self._file_name.setText(file.name)
