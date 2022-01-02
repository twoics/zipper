from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, \
    QListWidgetItem
from pathlib import Path
from custom_list_element import _QCustomQWidget


class _QList(QWidget):
    """
    The class representing the work of QListWidget, supports the
    drag and drop function, works together with QCustomQWidget
    """
    added_file = QtCore.pyqtSignal()

    def __init__(self):
        super(_QList, self).__init__(parent=None)
        self._data_list = []

        self._list_widget = QListWidget(self)
        self.setAcceptDrops(True)

        self.setStyleSheet("background-color: rgb(175, 182, 190);"
                           "border: 0px")

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
            raise FileNotFoundError("Empty file path")

        path = Path(path_to_file)

        custom_widget = _QCustomQWidget()
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
