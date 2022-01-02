from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel, QLineEdit, QPushButton

_MAIN_BACKGROUND_COLOR = [175, 182, 190]
_BUTTON_COLOR = [222, 226, 230]
_BUTTON_HOVER = [220, 220, 221]
_APP_NAME = [255, 255, 255]
_TOP_RIGHT_HOVER = [220, 220, 221]
_TOP_RIGHT_BACKGROUND = [173, 181, 189]
_CLOSE_BUTTON_HOVER = [255, 94, 91]
_MAIN_BODY_BACKGROUND = [173, 181, 189]


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.some_layout = QFormLayout()
        self.button = QPushButton(self)
        self.input_line = QLineEdit()
        self.text = QLabel("Input Result Name")
        self.setWindowTitle("Saving the result")
        self.setup_ui()
        self.setup_css()

    def setup_ui(self):
        self.button.setMinimumSize(30, 50)
        self.button.setText("Choose directory")
        self.button.clicked.connect(self.a)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.text.setFont(font)

        self.some_layout.addRow(self.text, self.input_line)

        self.some_layout.addRow(self.button)
        self.setLayout(self.some_layout)

    def setup_css(self):
        self.setStyleSheet(f"background-color: rgb({_MAIN_BACKGROUND_COLOR[0]}, "
                           f"{_MAIN_BACKGROUND_COLOR[1]}, {_MAIN_BACKGROUND_COLOR[2]});")

        self.button.setStyleSheet("QPushButton{"
                                  f"    background-color: rgb({_BUTTON_COLOR[0]}, "
                                  f"{_BUTTON_COLOR[1]}, {_BUTTON_COLOR[2]});"
                                  "    border-radius: 15;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  f"    background-color: rgb({_BUTTON_HOVER[0]}, {_BUTTON_HOVER[1]},"
                                  f" {_BUTTON_HOVER[2]});"
                                  "}")

        self.input_line.setStyleSheet(f"background-color: rgb(255, "
                                      f"255, 255);")

    def a(self):
        print(QtWidgets.QFileDialog.getExistingDirectory())
