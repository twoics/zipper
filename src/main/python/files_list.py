"""This module presents a list of files to be converted"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, \
    QListWidgetItem
from pathlib import Path
from custom_list_element import _QCustomQWidget
from typing import List, Union

LIST_COLOR = [int, int, int]
LIST_PATHS = List[Path]


class QList(QWidget):
    """
    The class representing the work of QListWidget, supports the
    drag and drop function, works together with QCustomQWidget
    """
    added_file = QtCore.pyqtSignal()

    def __init__(self):
        super(QList, self).__init__(parent=None)
        self._data_list = []

        self._color_for_list_elements = None

        self._list_widget = QListWidget(self)
        self.setAcceptDrops(True)

        window_layout = QVBoxLayout()
        window_layout.addWidget(self._list_widget)
        self.setLayout(window_layout)

    def get_files_path(self) -> LIST_PATHS:
        """
        Return list with objects pathlib.Path
        :return: List with paths files
        """
        return self._data_list

    def add_file(self, path_to_file: str) -> Union[QtCore.pyqtSignal(), None]:
        """
        Add file into files list
        If the file was added successfully sends a signal, if the file was not added, it returns None
        :param path_to_file: Path to the file to add
        :return: Sends the "added_file" signal if the file was successfully added, otherwise nothing
        """
        if not path_to_file:
            return

        path = Path(path_to_file)

        custom_widget = _QCustomQWidget(self._color_for_list_elements)
        custom_widget.set_file_name(path)
        custom_widget.set_file_icon(path)

        list_item = QListWidgetItem()
        list_item.setSizeHint(custom_widget.sizeHint())

        self._data_list.append(path)

        self._list_widget.addItem(list_item)
        self._list_widget.setItemWidget(list_item, custom_widget)

        self.added_file.emit()

    def delete_file(self) -> None:
        """
        Deletes the selected file
        :return: None
        """
        current_row_index = self._list_widget.currentRow()
        if current_row_index >= 0:
            self._list_widget.takeItem(current_row_index)
            self._data_list.pop(current_row_index)

    def delete_all(self) -> None:
        """
        Removes all files from the file list
        :return: None
        """
        self._data_list.clear()
        self._list_widget.clear()

    def set_stylesheet(self, colors_list: LIST_COLOR) -> None:
        """
        Sets the background color by colors_list
        :param colors_list: Color to be set
        :return: None
        """
        self.setStyleSheet("background-color: rgb"
                           f"({colors_list[0]}, {colors_list[1]}, {colors_list[2]});"
                           "border: 0px")

    def set_color_for_list_elements(self, color_for_list_items: LIST_COLOR) -> None:
        """
        Sets the color for the text of list items
        :param color_for_list_items: Color for text list items
        :return: None
        """
        self._color_for_list_elements = color_for_list_items

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            self.add_file(f)
