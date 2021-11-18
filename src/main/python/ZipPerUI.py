"""This module is the UI of the application, all the main widgets are located here."""
import os
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QFileIconProvider, QListWidget, QVBoxLayout, \
    QListWidgetItem, QFileDialog
from PyQt5.QtWidgets import QMainWindow

import ZipPerIcons

MAIN_BACKGROUND_COLOR = [175, 182, 190]
BUTTON_COLOR = [222, 226, 230]
BUTTON_HOVER = [220, 220, 221]
APP_NAME = [255, 255, 255]
TOP_RIGHT_HOVER = [220, 220, 221]
TOP_RIGHT_BACKGROUND = [173, 181, 189]
CLOSE_BUTTON_HOVER = [255, 94, 91]
MAIN_BODY_BACKGROUND = [173, 181, 189]


class UiZipPer(QMainWindow):
    """Main UI"""

    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self._central_widget = QtWidgets.QWidget(self)
        self._verticalLayout = QtWidgets.QVBoxLayout(self._central_widget)
        self._appBar = QtWidgets.QFrame(self._central_widget)
        self._horizontalLayout = QtWidgets.QHBoxLayout(self._appBar)
        self._topLeftButton = QtWidgets.QFrame(self._appBar)
        self._horizontalLayout_5 = QtWidgets.QHBoxLayout(self._topLeftButton)
        self._backButton = QtWidgets.QPushButton(self._topLeftButton)
        self._appName = QtWidgets.QFrame(self._appBar)
        self._horizontalLayout_6 = QtWidgets.QHBoxLayout(self._appName)
        self._name = QtWidgets.QLabel(self._appName)
        self._icon = QtWidgets.QLabel(self._appName)
        self._topRightButtons = QtWidgets.QFrame(self._appBar)
        self._horizontalLayout_4 = QtWidgets.QHBoxLayout(self._topRightButtons)
        self._minimizeButton = QtWidgets.QPushButton(self._topRightButtons)
        self._maximizeButton = QtWidgets.QPushButton(self._topRightButtons)
        self._closeButton = QtWidgets.QPushButton(self._topRightButtons)
        self._mainBody = QtWidgets.QFrame(self._central_widget)
        self._horizontalLayout_2 = QtWidgets.QHBoxLayout(self._mainBody)
        self._stackedWidget = QtWidgets.QStackedWidget(self._mainBody)
        self._optionButtons = QtWidgets.QWidget()
        self._verticalLayout_3 = QtWidgets.QVBoxLayout(self._optionButtons)
        self._buttons = QtWidgets.QFrame(self._optionButtons)
        self._gridLayout = QtWidgets.QGridLayout(self._buttons)
        self._rarPack = QtWidgets.QPushButton(self._buttons)
        self._zipPack = QtWidgets.QPushButton(self._buttons)
        self._unpack = QtWidgets.QPushButton(self._buttons)
        self._convert = QtWidgets.QPushButton(self._buttons)
        self._bottomBar = QtWidgets.QFrame(self._optionButtons)
        self._horizontalLayout_7 = QtWidgets.QHBoxLayout(self._bottomBar)
        self._infoResources = QtWidgets.QPushButton(self._bottomBar)
        self._changeTheme = QtWidgets.QPushButton(self._bottomBar)
        self._convertor = QtWidgets.QWidget()
        self._verticalLayout_2 = QtWidgets.QVBoxLayout(self._convertor)
        self._convertor_windows = QtWidgets.QStackedWidget(self._convertor)
        self._main_list = _QList()
        self._helper_window = _HelperPage()
        self._bottom = QtWidgets.QFrame(self._convertor)
        self._horizontalLayout_3 = QtWidgets.QHBoxLayout(self._bottom)
        self._addFile = QtWidgets.QPushButton(self._bottom)
        self._generate = QtWidgets.QPushButton(self._bottom)
        self._delFile = QtWidgets.QPushButton(self._bottom)

        # Slots
        self._create_slots()

        # Create UI
        self._setup_ui(self)

    def _create_slots(self):
        self._helper_window.on_dragging.connect(self._set_main_convertor)
        self._main_list.added_file.connect(self._update_window)

        self._rarPack.clicked.connect(self._open_convertor_page)
        self._zipPack.clicked.connect(self._open_convertor_page)
        self._unpack.clicked.connect(self._open_convertor_page)
        self._convert.clicked.connect(self._open_convertor_page)
        self._backButton.clicked.connect(self._open_main_page)

        self._addFile.clicked.connect(lambda: self._main_list.add_file(QFileDialog.getOpenFileName()[0]))
        self._delFile.clicked.connect(lambda: self._main_list.delete_file())

    def _setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(954, 643)
        self._central_widget.setStyleSheet(f"background-color: rgb({MAIN_BACKGROUND_COLOR[0]}, "
                                          f"{MAIN_BACKGROUND_COLOR[1]}, {MAIN_BACKGROUND_COLOR[2]});")
        self._central_widget.setObjectName("centralwidget")
        self._verticalLayout.setContentsMargins(0, 0, 0, 0)
        self._verticalLayout.setSpacing(0)
        self._verticalLayout.setObjectName("verticalLayout")
        self._appBar.setMinimumSize(QtCore.QSize(0, 70))
        self._appBar.setMaximumSize(QtCore.QSize(16777215, 70))
        self._appBar.setStyleSheet("QPushButton{"
                                  f"background-color: rgb({BUTTON_COLOR[0]}, {BUTTON_COLOR[1]}, {BUTTON_COLOR[2]});"
                                  "    border-radius: 15;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  f"    background-color: rgb({BUTTON_HOVER[0]}, {BUTTON_HOVER[1]}, {BUTTON_HOVER[2]});"
                                  "}")

        self._appBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._appBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self._appBar.setObjectName("appBar")
        self._horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout.setSpacing(0)
        self._horizontalLayout.setObjectName("horizontalLayout")
        self._topLeftButton.setMinimumSize(QtCore.QSize(100, 0))
        self._topLeftButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self._topLeftButton.setStyleSheet("")
        self._topLeftButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._topLeftButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self._topLeftButton.setObjectName("topLeftButton")
        self._horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_5.setSpacing(0)
        self._horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._backButton.setMinimumSize(QtCore.QSize(0, 65))
        self._backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-menu-32.png"), Qt.QIcon.Normal, Qt.QIcon.Off)
        self._backButton.setIcon(icon)
        self._backButton.setIconSize(QtCore.QSize(24, 24))
        self._backButton.setObjectName("pushButton")
        self._horizontalLayout_5.addWidget(self._backButton)
        self._horizontalLayout.addWidget(self._topLeftButton, 0, Qt.Qt.AlignLeft)
        self._appName.setMinimumSize(QtCore.QSize(250, 0))
        self._appName.setMaximumSize(QtCore.QSize(250, 16777215))
        self._appName.setStyleSheet("")
        self._appName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._appName.setFrameShadow(QtWidgets.QFrame.Raised)
        self._appName.setObjectName("appName")
        self._horizontalLayout_6.setObjectName("horizontalLayout_6")
        font = QtGui.QFont()
        font.setPointSize(16)
        self._name.setFont(font)
        self._name.setStyleSheet("")
        self._name.setObjectName("name")
        self._horizontalLayout_6.addWidget(self._name, 0, Qt.Qt.AlignRight)
        self._icon.setText("")
        self._icon.setPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-32.png"))
        self._icon.setObjectName("icon")
        self._horizontalLayout_6.addWidget(self._icon)
        self._horizontalLayout.addWidget(self._appName)
        self._topRightButtons.setMinimumSize(QtCore.QSize(80, 0))
        self._topRightButtons.setMaximumSize(QtCore.QSize(150, 16777215))
        self._topRightButtons.setStyleSheet("QPushButton{"
                                           "        border-radius: 5;"
                                           f"        background-color: rgb({TOP_RIGHT_BACKGROUND[0]}, "
                                           f"{TOP_RIGHT_BACKGROUND[1]}, {TOP_RIGHT_BACKGROUND[2]});"
                                           "}"
                                           "QPushButton::hover"
                                           "{"
                                           f"        background-color : rgb({TOP_RIGHT_HOVER[0]}, {TOP_RIGHT_HOVER[1]},"
                                           f" {TOP_RIGHT_HOVER[2]});"
                                           "}")
        self._topRightButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._topRightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self._topRightButtons.setObjectName("topRightButtons")
        self._horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._minimizeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-minimize-window-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._minimizeButton.setIcon(icon1)
        self._minimizeButton.setIconSize(QtCore.QSize(24, 24))
        self._minimizeButton.setObjectName("minimazeButton")
        self._horizontalLayout_4.addWidget(self._minimizeButton)
        self._maximizeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-maximize-window-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._maximizeButton.setIcon(icon2)
        self._maximizeButton.setIconSize(QtCore.QSize(24, 24))
        self._maximizeButton.setObjectName("maximazeButton")
        self._horizontalLayout_4.addWidget(self._maximizeButton)
        self._closeButton.setStyleSheet("QPushButton{"
                                       "        border-radius: 5;"
                                       f"        background-color: rgb({TOP_RIGHT_BACKGROUND[0]}, "
                                       f"{TOP_RIGHT_BACKGROUND[1]}, {TOP_RIGHT_BACKGROUND[2]});"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       f"    background-color: rgb({CLOSE_BUTTON_HOVER[0]}, {CLOSE_BUTTON_HOVER[1]},"
                                       f" {CLOSE_BUTTON_HOVER[2]});"
                                       "}")
        self._closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-close-window-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._closeButton.setIcon(icon3)
        self._closeButton.setIconSize(QtCore.QSize(24, 24))
        self._closeButton.setObjectName("closeButton")
        self._horizontalLayout_4.addWidget(self._closeButton)
        self._horizontalLayout.addWidget(self._topRightButtons, 0, Qt.Qt.AlignRight)
        self._verticalLayout.addWidget(self._appBar)
        self._mainBody.setMinimumSize(QtCore.QSize(0, 0))
        self._mainBody.setStyleSheet(f"background-color: rgb({MAIN_BODY_BACKGROUND[0]}, "
                                    f"{MAIN_BODY_BACKGROUND[1]}, {MAIN_BODY_BACKGROUND[2]});")
        self._mainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._mainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self._mainBody.setObjectName("mainBody")
        self._horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_2.setSpacing(0)
        self._horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._stackedWidget.setStyleSheet("QPushButton{"
                                         f"    background-color: rgb({BUTTON_COLOR[0]}, "
                                         f"{BUTTON_COLOR[1]}, {BUTTON_COLOR[2]});"
                                         "    border-radius: 15;"
                                         "}"
                                         "QPushButton::hover"
                                         "{"
                                         f"    background-color: rgb({BUTTON_HOVER[0]}, {BUTTON_HOVER[1]},"
                                         f" {BUTTON_HOVER[2]});"
                                         "}")
        self._stackedWidget.setObjectName("stackedWidget")
        self._optionButtons.setStyleSheet("")
        self._optionButtons.setObjectName("optionButtons")
        self._verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self._verticalLayout_3.setSpacing(0)
        self._verticalLayout_3.setObjectName("verticalLayout_3")
        self._buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self._buttons.setObjectName("buttons")
        self._gridLayout.setContentsMargins(0, 0, 0, 0)
        self._gridLayout.setHorizontalSpacing(0)
        self._gridLayout.setVerticalSpacing(6)
        self._gridLayout.setObjectName("gridLayout")
        self._rarPack.setMinimumSize(QtCore.QSize(150, 150))
        self._rarPack.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._rarPack.setFont(font)
        self._rarPack.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-rar-32.png"), Qt.QIcon.Normal, Qt.QIcon.Off)
        self._rarPack.setIcon(icon4)
        self._rarPack.setIconSize(QtCore.QSize(32, 32))
        self._rarPack.setObjectName("rarPack")
        self._gridLayout.addWidget(self._rarPack, 0, 0, 1, 1)
        self._zipPack.setMinimumSize(QtCore.QSize(150, 150))
        self._zipPack.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._zipPack.setFont(font)
        self._zipPack.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-zip-32.png"), Qt.QIcon.Normal, Qt.QIcon.Off)
        self._zipPack.setIcon(icon5)
        self._zipPack.setIconSize(QtCore.QSize(32, 32))
        self._zipPack.setObjectName("zipPack")
        self._gridLayout.addWidget(self._zipPack, 0, 1, 1, 1)
        self._unpack.setMinimumSize(QtCore.QSize(150, 150))
        self._unpack.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._unpack.setFont(font)
        self._unpack.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-unpacking-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._unpack.setIcon(icon6)
        self._unpack.setIconSize(QtCore.QSize(32, 32))
        self._unpack.setObjectName("unpack")
        self._gridLayout.addWidget(self._unpack, 1, 0, 1, 1)
        self._convert.setMinimumSize(QtCore.QSize(150, 150))
        self._convert.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._convert.setFont(font)
        self._convert.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-export-pdf-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._convert.setIcon(icon7)
        self._convert.setIconSize(QtCore.QSize(32, 32))
        self._convert.setObjectName("convert")
        self._gridLayout.addWidget(self._convert, 1, 1, 1, 1)
        self._verticalLayout_3.addWidget(self._buttons)
        self._bottomBar.setMinimumSize(QtCore.QSize(0, 60))
        self._bottomBar.setMaximumSize(QtCore.QSize(16777215, 60))
        self._bottomBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._bottomBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self._bottomBar.setObjectName("bottomBar")
        self._horizontalLayout_7.setObjectName("horizontalLayout_7")
        self._changeTheme.setMinimumSize(QtCore.QSize(40, 40))
        self._changeTheme.setMaximumSize(QtCore.QSize(40, 40))
        self._changeTheme.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-moon-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._changeTheme.setIcon(icon8)
        self._changeTheme.setIconSize(QtCore.QSize(32, 32))
        self._changeTheme.setObjectName("changeTheme")
        self._horizontalLayout_7.addWidget(self._changeTheme, 0, Qt.Qt.AlignLeft)
        self._infoResources.setMinimumSize(QtCore.QSize(40, 40))
        self._infoResources.setMaximumSize(QtCore.QSize(40, 40))
        self._infoResources.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-info-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._infoResources.setIcon(icon9)
        self._infoResources.setIconSize(QtCore.QSize(32, 32))
        self._infoResources.setObjectName("infoResurses")
        self._horizontalLayout_7.addWidget(self._infoResources, 0, Qt.Qt.AlignRight)
        self._verticalLayout_3.addWidget(self._bottomBar)
        self._stackedWidget.addWidget(self._optionButtons)
        self._convertor.setStyleSheet("")
        self._convertor.setObjectName("convertor")
        self._verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self._verticalLayout_2.setSpacing(0)
        self._verticalLayout_2.setObjectName("verticalLayout_2")
        self._convertor_windows.setObjectName("convertor_windows")

        self._main_list.setObjectName("main_page")
        self._convertor_windows.addWidget(self._main_list)

        self._convertor_windows.addWidget(self._helper_window)

        self._convertor_windows.setCurrentIndex(1)

        self._verticalLayout_2.addWidget(self._convertor_windows)
        self._bottom.setMinimumSize(QtCore.QSize(0, 80))
        self._bottom.setMaximumSize(QtCore.QSize(16777215, 80))
        self._bottom.setStyleSheet("")
        self._bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self._bottom.setObjectName("bottom")
        self._horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._addFile.setMinimumSize(QtCore.QSize(100, 50))
        self._addFile.setMaximumSize(QtCore.QSize(100, 50))
        self._addFile.setStyleSheet("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-add-file-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self._addFile.setIcon(icon10)
        self._addFile.setIconSize(QtCore.QSize(32, 32))
        self._addFile.setObjectName("addFile")
        self._horizontalLayout_3.addWidget(self._addFile, 0, Qt.Qt.AlignLeft)
        self._generate.setMinimumSize(QtCore.QSize(400, 50))
        self._generate.setMaximumSize(QtCore.QSize(400, 50))
        self._generate.setStyleSheet("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self._generate.setIcon(icon11)
        self._generate.setIconSize(QtCore.QSize(32, 32))
        self._generate.setObjectName("generate")
        self._horizontalLayout_3.addWidget(self._generate, 0, Qt.Qt.AlignHCenter)
        self._delFile.setMinimumSize(QtCore.QSize(100, 50))
        self._delFile.setMaximumSize(QtCore.QSize(100, 50))
        self._delFile.setStyleSheet("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-delete-file-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self._delFile.setIcon(icon12)
        self._delFile.setIconSize(QtCore.QSize(32, 32))
        self._delFile.setObjectName("delFile")
        self._horizontalLayout_3.addWidget(self._delFile, 0, Qt.Qt.AlignRight)
        self._verticalLayout_2.addWidget(self._bottom)
        self._stackedWidget.addWidget(self._convertor)
        self._horizontalLayout_2.addWidget(self._stackedWidget)
        self._verticalLayout.addWidget(self._mainBody)
        main_window.setCentralWidget(self._central_widget)

        self._translate_ui(main_window)
        self._stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def _translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._name.setText(_translate("MainWindow", "ZipPer"))
        self._rarPack.setText(_translate("MainWindow", "Pack in .rar"))
        self._zipPack.setText(_translate("MainWindow", "Pack in .zip"))
        self._unpack.setText(_translate("MainWindow", "Unpack"))
        self._convert.setText(_translate("MainWindow", "Word to pdf"))
        self._addFile.setText(_translate("MainWindow", "Add"))
        self._generate.setText(_translate("MainWindow", "Generate"))
        self._delFile.setText(_translate("MainWindow", "Delete"))

    def _open_main_page(self):
        self._main_list.delete_all()
        self._set_helper_convertor()
        self._stackedWidget.setCurrentIndex(0)

    def _open_convertor_page(self):
        self._stackedWidget.setCurrentIndex(1)

    def _set_main_convertor(self):
        self._convertor_windows.setCurrentIndex(0)

    def _set_helper_convertor(self):
        self._convertor_windows.setCurrentIndex(1)

    def _update_window(self):
        if self._convertor_windows.currentIndex() == 1:
            self._set_main_convertor()


class _HelperPage(QWidget):
    """
    This window show prompt for user, that it can use drag and drop, as soon as the user starts dragging the file,
    this class sends a signal to change the window to set the main window
    """

    on_dragging = QtCore.pyqtSignal()

    def __init__(self):
        super(_HelperPage, self).__init__(parent=None)
        self.setAcceptDrops(True)

        self.setObjectName("helper_window")
        self._horizontalLayout_8 = QtWidgets.QHBoxLayout(self)
        self._horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_8.setSpacing(0)
        self._horizontalLayout_8.setObjectName("horizontalLayout_8")
        self._helper_frame = QtWidgets.QFrame(self)
        self._helper_frame.setMinimumSize(QtCore.QSize(400, 100))
        self._helper_frame.setMaximumSize(QtCore.QSize(400, 100))
        self._helper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._helper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._helper_frame.setObjectName("helper_frame")
        self._horizontalLayout_9 = QtWidgets.QHBoxLayout(self._helper_frame)
        self._horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_9.setSpacing(0)
        self._horizontalLayout_9.setObjectName("horizontalLayout_9")
        self._icon_helper = QtWidgets.QLabel(self._helper_frame)
        self._icon_helper.setText("")
        self._icon_helper.setPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-drag-and-drop-32.png"))
        self._icon_helper.setObjectName("icon_helper")
        self._horizontalLayout_9.addWidget(self._icon_helper)
        self._text_helper = QtWidgets.QLabel(self._helper_frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        self._text_helper.setFont(font)
        self._text_helper.setObjectName("text_helper")
        self._horizontalLayout_9.addWidget(self._text_helper)
        self._horizontalLayout_8.addWidget(self._helper_frame, 0, Qt.Qt.AlignHCenter | Qt.Qt.AlignVCenter)
        self._text_helper.setText("Drag and Drop your files")

    def dragEnterEvent(self, event):
        self.on_dragging.emit()


class _QCustomQWidget(QWidget):
    """
    Class of custom element QListWidget, has an icon and text, icon and text, the icon is selected from the system
    for a specific file type, you can set the color of the text
    """

    def __init__(self, txt_color: list = None):
        """
        Initialization
        :param txt_color: Optional parameter - text color array of 3 rgb elements, each element must be < 256.
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
                color: rgb({red}, {green}, {blue});
            ''')
        self.setStyleSheet(f"background-color: rgb({0}, {0}, {0}, {0});")  # Set alpha to null for correct view

    def set_file_icon(self, path_to_file: str):
        """
        Set icon from system
        :param path_to_file: Way to file
        :return: None
        """
        file_info = QtCore.QFileInfo(path_to_file)
        icon_provider = QFileIconProvider()
        icon = icon_provider.icon(file_info)
        pixmap = icon.pixmap(QSize(16, 16))
        self._file_icon.setPixmap(pixmap)

    def set_file_name(self, text):
        self._file_name.setText(text)


class _QList(QWidget):
    """
    The class representing the work of QListWidget, supports the
    drag and drop function, works together with QCustomQWidget
    """
    added_file = QtCore.pyqtSignal()

    def __init__(self):
        super(_QList, self).__init__(parent=None)
        self._list_widget = QListWidget(self)
        self.setAcceptDrops(True)

        self.setStyleSheet("background-color: rgb(175, 182, 190);"
                           "border: 0px")
        window_layout = QVBoxLayout()
        window_layout.addWidget(self._list_widget)
        self.setLayout(window_layout)

    def add_file(self, path_to_file: str):
        if not path_to_file:
            raise Exception("Empty file path")

        custom_widget = _QCustomQWidget()
        custom_widget.set_file_name(os.path.basename(path_to_file))
        custom_widget.set_file_icon(path_to_file)

        list_item = QListWidgetItem()
        list_item.setSizeHint(custom_widget.sizeHint())

        self._list_widget.addItem(list_item)
        self._list_widget.setItemWidget(list_item, custom_widget)

        self.added_file.emit()

    def delete_file(self):
        current_row = self.get_current_row()
        if current_row >= 0:
            self._list_widget.takeItem(current_row)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            self.add_file(f)

    def get_current_row(self):
        return self._list_widget.currentRow()

    def delete_all(self):
        self._list_widget.clear()
