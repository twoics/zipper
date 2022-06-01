"""The module represents a widget for selecting the file/folder name and directory where it will be saved
Send signal to start conversion"""

# Standard library imports
from typing import Tuple
from pathlib import Path

# Third party imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class PathSelectionWidget(QWidget):
    """Widget Class, If all fields are filled without problems, it sends a signal to start working"""

    COLOR_ARRAY = [int, int, int]
    DIRECTORY = str
    NAME = str
    PATH = Path

    EMPTY_FIELD = ""

    SET_SYMBOLS_ORD = {33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                       58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126}
    INVALID_SYMBOLS = {"<", ">", ":", '"', "/", "\\", "|", "?", "*"}

    # Signal emit PATH to save result and folder/file NAME
    _signal_with_path_and_name = QtCore.pyqtSignal(PATH, NAME)

    def __init__(self):
        super().__init__()
        self._result_dir = None
        self._result_name = None

        self._verticalLayout = QtWidgets.QVBoxLayout(self)
        self._input_name_frame = QtWidgets.QFrame(self)
        self._verticalLayout_2 = QtWidgets.QVBoxLayout(self._input_name_frame)
        self._information_text = QtWidgets.QLabel(self._input_name_frame)
        self._lineEdit = QtWidgets.QLineEdit(self._input_name_frame)
        self._frame = QtWidgets.QFrame(self)
        self._verticalLayout_3 = QtWidgets.QVBoxLayout(self._frame)
        self._label = QtWidgets.QLabel(self._frame)
        self._pushButton_2 = QtWidgets.QPushButton(self._frame)

        self._pushButton_2.clicked.connect(self._emit_signal)

        self._setup_ui()

    def get_path_signal(self) -> QtCore.pyqtSignal():
        """
        Returns the signal for listening,
        emitted when the user has selected
        a directory and a name to save the result
        :return: Signal for listening
        """
        return self._signal_with_path_and_name

    def set_text_color(self, color: COLOR_ARRAY) -> None:
        """
        Set colors for hints and input fields on widget
        :param color: Color to set
        :return: None
        """
        red = color[0]
        green = color[1]
        blue = color[2]
        self._label.setStyleSheet(f'''
                color: rgb({red}, {green}, {blue});''')
        self._information_text.setStyleSheet(f'''
                        color: rgb({red}, {green}, {blue});''')
        self._lineEdit.setStyleSheet(" QLineEdit {"
                                     f"color: rgb({red}, {green}, {blue});"
                                     "     border: 2px solid gray;"
                                     "     border-radius: 10px;"
                                     "     padding: 0 8px;"
                                     "     selection-background-color: darkgray;"
                                     " }")

    def clear_input_filed(self) -> None:
        self._lineEdit.setText("")

    def _get_data_from_all_fields(self) -> Tuple[DIRECTORY, NAME]:
        return QtWidgets.QFileDialog.getExistingDirectory(), self._lineEdit.text()

    def _check_ui_fields(self) -> bool:
        """
        Checks the name and path, if there are no problems returns True otherwise False
        :return: True or False
        """
        if self._result_name is self.EMPTY_FIELD or self._result_dir is self.EMPTY_FIELD:
            return False
        if len(self._result_name) == 1 and self._result_name in self.SET_SYMBOLS_ORD:
            return False
        # Are there any forbidden characters in the name
        if set(self._result_name).intersection(self.INVALID_SYMBOLS):
            return False

        path = Path(self._result_dir)
        for file in path.iterdir():
            if file.stem == self._result_name:
                return False
        return True

    def _emit_signal(self) -> QtCore.pyqtSignal():
        """
        If the fields are filled without problems, then it sends a signal ("signal_to_start_convert") to start working
        :return: Signal or None
        """
        self._result_dir, self._result_name = self._get_data_from_all_fields()
        self.clear_input_filed()
        if self._check_ui_fields():
            self._signal_with_path_and_name.emit(Path(self._result_dir), self._result_name)
        else:
            QMessageBox.warning(self, "Invalid path or name",
                                "You must enter the correct name and specify the correct path")

    def _setup_ui(self) -> None:
        """Setting UI"""

        self.setObjectName("Form")
        self.resize(921, 624)
        self.setStyleSheet("QProgressBar{\n"
                           "    border: solid black;\n"
                           "    border-radius: 15px;\n"
                           "    color: black;\n"
                           "}\n"
                           "\n"
                           "QProgressBar::chunk{\n"
                           "    border-radius : 15px;\n"
                           "    background-color: rgb(87, 182, 225);\n"
                           "}"
                           "QMessageBox{"
                           "  background-color: rgb(255, 255, 255);"
                           "}"
                           "QMessageBox QLabel {"
                           "  color: rgb(0, 0, 0);"
                           "  background-color: rgb(255, 255, 255);"
                           "}"
                           "QMessageBox QPushButton {"
                           " background-color: rgb(255, 255, 255);"
                           "}")
        self._verticalLayout.setContentsMargins(-1, 11, -1, 30)
        self._verticalLayout.setObjectName("verticalLayout")
        self._input_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._input_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._input_name_frame.setObjectName("input_name_frame")
        self._verticalLayout_2.setObjectName("verticalLayout_2")
        font = QtGui.QFont()
        font.setPointSize(16)
        self._information_text.setFont(font)
        self._information_text.setAlignment(Qt.AlignCenter)
        self._information_text.setObjectName("information_text")
        self._verticalLayout_2.addWidget(self._information_text, 0, Qt.AlignBottom)
        self._lineEdit.setMinimumSize(QtCore.QSize(500, 30))
        self._lineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self._lineEdit.setFont(font)
        self._lineEdit.setStyleSheet(" QLineEdit {\n"
                                     "     border: 2px solid gray;\n"
                                     "     border-radius: 10px;\n"
                                     "     padding: 0 8px;\n"
                                     "     selection-background-color: darkgray;\n"
                                     " }")
        self._lineEdit.setAlignment(Qt.AlignCenter)
        self._lineEdit.setObjectName("lineEdit")
        self._verticalLayout_2.addWidget(self._lineEdit, 0, Qt.AlignHCenter)
        self._verticalLayout.addWidget(self._input_name_frame)
        self._frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._frame.setObjectName("frame")
        self._verticalLayout_3.setObjectName("verticalLayout_3")
        font = QtGui.QFont()
        font.setPointSize(16)
        self._label.setFont(font)
        self._label.setObjectName("label")
        self._verticalLayout_3.addWidget(self._label, 0, Qt.AlignHCenter)
        self._pushButton_2.setMinimumSize(QtCore.QSize(300, 50))
        self._pushButton_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self._pushButton_2.setFont(font)
        self._pushButton_2.setObjectName("pushButton_2")
        self._verticalLayout_3.addWidget(self._pushButton_2, 0, Qt.AlignHCenter)
        self._verticalLayout.addWidget(self._frame, 0, Qt.AlignVCenter)

        self._translate(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def _translate(self, widget) -> None:
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("Form", "Form"))
        self._information_text.setText(_translate("Form", "Enter what the result will be named"))
        self._label.setText(_translate("Form", "Select the directory to save the result"))
        self._pushButton_2.setText(_translate("Form", "Choose and start"))
