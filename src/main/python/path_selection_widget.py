from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from pathlib import Path


class PathSelectionWidget(QWidget):
    EMPTY_FIELD = ""
    SET_SYMBOLS_ORD = {33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                       58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126}
    INVALID_SYMBOLS = {"<", ">", ":", '"', "/", "\\", "|", "?", "*"}

    NAME = str
    PATH = Path

    signal_to_start_convert = QtCore.pyqtSignal(PATH, NAME)

    def __init__(self):
        super().__init__()
        self._result_dir = None
        self._result_name = None

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.input_name_frame = QtWidgets.QFrame(self)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.input_name_frame)
        self.information_text = QtWidgets.QLabel(self.input_name_frame)
        self.lineEdit = QtWidgets.QLineEdit(self.input_name_frame)
        self.frame = QtWidgets.QFrame(self)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.label = QtWidgets.QLabel(self.frame)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)

        self.pushButton_2.clicked.connect(self._emit_signal)

        self._setup_ui(self)

    def _setup_ui(self, widget):
        widget.setObjectName("Form")
        widget.resize(921, 624)
        widget.setStyleSheet("QProgressBar{\n"
                             "    border: solid black;\n"
                             "    border-radius: 15px;\n"
                             "    color: black;\n"
                             "}\n"
                             "\n"
                             "QProgressBar::chunk{\n"
                             "    border-radius : 15px;\n"
                             "    background-color: rgb(87, 182, 225);\n"
                             "}")
        self.verticalLayout.setContentsMargins(-1, 11, -1, 30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_name_frame.setObjectName("input_name_frame")
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.information_text.setFont(font)
        self.information_text.setAlignment(Qt.AlignCenter)
        self.information_text.setObjectName("information_text")
        self.verticalLayout_2.addWidget(self.information_text, 0, Qt.AlignBottom)
        self.lineEdit.setMinimumSize(QtCore.QSize(500, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(" QLineEdit {\n"
                                    "     border: 2px solid gray;\n"
                                    "     border-radius: 10px;\n"
                                    "     padding: 0 8px;\n"
                                    "     selection-background-color: darkgray;\n"
                                    " }")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit, 0, Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.input_name_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)
        self.pushButton_2.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignVCenter)

        self._translate(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def _translate(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("Form", "Form"))
        self.information_text.setText(_translate("Form", "Enter what the result will be named"))
        self.label.setText(_translate("Form", "Select the directory to save the result"))
        self.pushButton_2.setText(_translate("Form", "Choose and start"))

    def _get_data_from_all_fields(self):
        self._result_dir = QtWidgets.QFileDialog.getExistingDirectory()
        self._result_name = self.lineEdit.text()

    def _check_ui_fields(self):
        if self._result_name is self.EMPTY_FIELD or self._result_dir is self.EMPTY_FIELD:
            return False
        if len(self._result_name) == 1 and self._result_name in self.SET_SYMBOLS_ORD:
            return False
        # Are there any forbidden characters in the name
        if set(self._result_name).intersection(self.INVALID_SYMBOLS):
            return False
        return True

    def _emit_signal(self):
        self._get_data_from_all_fields()
        if self._check_ui_fields():
            self.signal_to_start_convert.emit(Path(self._result_dir), self._result_name)
