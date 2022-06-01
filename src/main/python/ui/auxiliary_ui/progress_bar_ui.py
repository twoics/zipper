"""The module represents the progress bar widget"""

# Third party imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class ProgressBarWindow(QWidget):
    """Bar progress class, sets the bar progress value
    from the main UI module, which receives the value from the controller module signal"""

    COLOR_ARRAY = [int, int, int]

    def __init__(self):
        super().__init__()
        self._verticalLayout = QtWidgets.QVBoxLayout(self)
        self._frame = QtWidgets.QFrame(self)
        self._verticalLayout_2 = QtWidgets.QVBoxLayout(self._frame)
        self._information_text = QtWidgets.QLabel(self._frame)
        self._progress_bar = QtWidgets.QProgressBar(self._frame)
        self._label = QtWidgets.QLabel(self)

        self._setup_ui()
        self._set_stylesheet()

    def set_progress_value(self, value: int) -> None:
        self._progress_bar.setValue(value)

    def set_text_color(self, color: COLOR_ARRAY) -> None:
        """Set text color by transferred color"""
        red = color[0]
        green = color[1]
        blue = color[2]
        self._label.setStyleSheet(f'''
                color: rgb({red}, {green}, {blue});''')
        self._information_text.setStyleSheet(f'''
                        color: rgb({red}, {green}, {blue});''')

    def _set_stylesheet(self) -> None:
        self.setStyleSheet("QProgressBar{"
                           "    border: solid black;"
                           "    border-radius: 15px;"
                           "    color: black;"
                           "}"
                           "QProgressBar::chunk{"
                           "    border-radius : 15px;"
                           "    background-color: rgb(87, 182, 225);"
                           "}")

    def _setup_ui(self) -> None:
        """Setting UI"""
        self.setObjectName("Form")
        self.resize(892, 623)
        self._verticalLayout.setContentsMargins(-1, 11, -1, 30)
        self._verticalLayout.setObjectName("verticalLayout")
        self._frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._frame.setObjectName("frame")
        self._verticalLayout_2.setObjectName("verticalLayout_2")
        font = QtGui.QFont()
        font.setPointSize(16)
        self._information_text.setFont(font)
        self._information_text.setAlignment(Qt.AlignCenter)
        self._information_text.setObjectName("information_text")
        self._verticalLayout_2.addWidget(self._information_text, 0, Qt.AlignBottom)
        self._progress_bar.setMinimumSize(QtCore.QSize(40, 40))
        self._progress_bar.setProperty("value", 0)
        self._progress_bar.setAlignment(Qt.AlignCenter)
        self._progress_bar.setObjectName("progress_bar")
        self._verticalLayout_2.addWidget(self._progress_bar)
        self._verticalLayout.addWidget(self._frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self._label.setFont(font)
        self._label.setAlignment(Qt.AlignCenter)
        self._label.setObjectName("label")
        self._verticalLayout.addWidget(self._label, 0, Qt.AlignBottom)

        self._translate()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _translate(self) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self._information_text.setText(_translate("Form", "File processing progress"))
        self._progress_bar.setFormat(_translate("Form", "%p%"))
        self._label.setText(_translate("Form", "Thanks for using ZipPer"))
