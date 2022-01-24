from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, \
    QListWidgetItem
from pathlib import Path
from custom_list_element import _QCustomQWidget

LIST_COLOR = [int, int, int]


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

    def get_files_path(self):
        """
        Return list with objects pathlib.Path
        :return: list
        """
        return self._data_list

    def add_file(self, path_to_file: str):
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

    def delete_file(self):
        current_row_index = self._list_widget.currentRow()
        if current_row_index >= 0:
            self._list_widget.takeItem(current_row_index)
            self._data_list.pop(current_row_index)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            self.add_file(f)

    def delete_all(self):
        self._data_list.clear()
        self._list_widget.clear()

    def set_stylesheet(self, colors_list: LIST_COLOR):
        self.setStyleSheet("background-color: rgb"
                           f"({colors_list[0]}, {colors_list[1]}, {colors_list[2]});"
                           "border: 0px")

    def set_color_for_list_elements(self, colors_list: LIST_COLOR):
        self._color_for_list_elements = colors_list
