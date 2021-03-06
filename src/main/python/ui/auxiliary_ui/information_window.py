"""The module represents a hint widget for the user"""

# Third party imports
from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class HintPage(QWidget):
    """
    This window show prompt for user, that it can use drag and drop, as soon as the user starts dragging the file,
    this class sends a signal to change the window to set the main window
    """

    COLOR_ARRAY = [int, int, int]

    # Signal emit when drag and drop happens
    _on_dragging = QtCore.pyqtSignal()

    def __init__(self):
        super(HintPage, self).__init__(parent=None)
        self._horizontalLayout_8 = QtWidgets.QHBoxLayout(self)
        self._helper_frame = QtWidgets.QFrame(self)
        self._horizontalLayout_9 = QtWidgets.QHBoxLayout(self._helper_frame)
        self._icon_helper = QtWidgets.QLabel(self._helper_frame)
        self._text_helper = QtWidgets.QLabel(self._helper_frame)
        self._setup_ui()

    def set_text_color(self, color: COLOR_ARRAY) -> None:
        """
        Set color of text on widget
        :param color: Color for text
        :return: None
        """
        red = color[0]
        green = color[1]
        blue = color[2]
        self._text_helper.setStyleSheet(f'''
                color: rgb({red}, {green}, {blue});''')

    def get_drag_drop_signal(self) -> QtCore.pyqtSignal():
        """
        Returns the signal to listening that
        is emitted when the user does drag and drop
        :return: Signal for listening
        """
        return self._on_dragging

    def dragEnterEvent(self, event):
        self._on_dragging.emit()

    def _setup_ui(self) -> None:
        self.setAcceptDrops(True)
        self.setObjectName("helper_window")
        self._horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_8.setSpacing(0)
        self._horizontalLayout_8.setObjectName("horizontalLayout_8")
        self._helper_frame.setMinimumSize(QtCore.QSize(400, 100))
        self._helper_frame.setMaximumSize(QtCore.QSize(400, 100))
        self._helper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._helper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._helper_frame.setObjectName("helper_frame")
        self._horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_9.setSpacing(0)
        self._horizontalLayout_9.setObjectName("horizontalLayout_9")
        self._icon_helper.setText("")
        self._icon_helper.setPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-drag-and-drop-32.png"))
        self._icon_helper.setObjectName("icon_helper")
        self._horizontalLayout_9.addWidget(self._icon_helper)
        font = QtGui.QFont()
        font.setPointSize(19)
        self._text_helper.setFont(font)
        self._text_helper.setObjectName("text_helper")
        self._horizontalLayout_9.addWidget(self._text_helper)
        self._horizontalLayout_8.addWidget(self._helper_frame, 0, Qt.Qt.AlignHCenter | Qt.Qt.AlignVCenter)
        self._text_helper.setText("Drag and Drop your files")
