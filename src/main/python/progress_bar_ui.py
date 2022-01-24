from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class ProgressBarWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.frame = QtWidgets.QFrame(self)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.information_text = QtWidgets.QLabel(self.frame)
        self.progress_bar = QtWidgets.QProgressBar(self.frame)
        self.label = QtWidgets.QLabel(self)

        self._setup_ui()
        self.set_stylesheet()

    def set_progress_value(self, value: int) -> None:
        self.progress_bar.setValue(value)

    def set_stylesheet(self):
        self.setStyleSheet("QProgressBar{\n"
                           "    border: solid black;\n"
                           "    border-radius: 15px;\n"
                           "    color: black;\n"
                           "}\n"
                           "\n"
                           "QProgressBar::chunk{\n"
                           "    border-radius : 15px;\n"
                           "    background-color: rgb(87, 182, 225);\n"
                           "}")

    def _setup_ui(self):
        self.setObjectName("Form")
        self.resize(892, 623)
        self.verticalLayout.setContentsMargins(-1, 11, -1, 30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.information_text.setFont(font)
        self.information_text.setAlignment(Qt.AlignCenter)
        self.information_text.setObjectName("information_text")
        self.verticalLayout_2.addWidget(self.information_text, 0, Qt.AlignBottom)
        self.progress_bar.setMinimumSize(QtCore.QSize(40, 40))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_2.addWidget(self.progress_bar)
        self.verticalLayout.addWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, Qt.AlignBottom)

        self._translate()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.information_text.setText(_translate("Form", "File processing progress"))
        self.progress_bar.setFormat(_translate("Form", "%p%"))
        self.label.setText(_translate("Form", "Thanks for using ZipPer"))
