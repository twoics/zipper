import os

from PyQt5 import Qt
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QFileIconProvider, QListWidget, QVBoxLayout, QListWidgetItem

import ZipPerIcons

MAIN_BACKGROUND_COLOR = [175, 182, 190]
BUTTON_COLOR = [222, 226, 230]
BUTTON_HOVER = [220, 220, 221]
APP_NAME = [255, 255, 255]
TOP_RIGHT_HOVER = [220, 220, 221]
TOP_RIGHT_BACKGROUND = [173, 181, 189]
CLOSE_BUTTON_HOVER = [255, 94, 91]
MAIN_BODY_BACKGROUND = [173, 181, 189]


class Ui_MainWindow(object):
    """Main UI"""

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(f"background-color: rgb({MAIN_BACKGROUND_COLOR[0]}, "
                                         f"{MAIN_BACKGROUND_COLOR[1]}, {MAIN_BACKGROUND_COLOR[2]});")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appBar = QtWidgets.QFrame(self.centralwidget)
        self.appBar.setMinimumSize(QtCore.QSize(0, 70))
        self.appBar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.appBar.setStyleSheet("QPushButton{"
                                  f"background-color: rgb({BUTTON_COLOR[0]}, {BUTTON_COLOR[1]}, {BUTTON_COLOR[2]});"
                                  "    border-radius: 15;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  f"    background-color: rgb({BUTTON_HOVER[0]}, {BUTTON_HOVER[1]}, {BUTTON_HOVER[2]});"
                                  "}")

        self.appBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appBar.setObjectName("appBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.appBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.topLeftButton = QtWidgets.QFrame(self.appBar)
        self.topLeftButton.setMinimumSize(QtCore.QSize(100, 0))
        self.topLeftButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.topLeftButton.setStyleSheet("")
        self.topLeftButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topLeftButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topLeftButton.setObjectName("topLeftButton")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.topLeftButton)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.topLeftButton)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 65))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-menu-32.png"), Qt.QIcon.Normal, Qt.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.topLeftButton, 0, Qt.Qt.AlignLeft)
        self.appName = QtWidgets.QFrame(self.appBar)
        self.appName.setMinimumSize(QtCore.QSize(250, 0))
        self.appName.setMaximumSize(QtCore.QSize(250, 16777215))
        self.appName.setStyleSheet("")
        self.appName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appName.setObjectName("appName")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.appName)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.name = QtWidgets.QLabel(self.appName)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setStyleSheet("")
        self.name.setObjectName("name")
        self.horizontalLayout_6.addWidget(self.name, 0, Qt.Qt.AlignRight)
        self.icon = QtWidgets.QLabel(self.appName)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-32.png"))
        self.icon.setObjectName("icon")
        self.horizontalLayout_6.addWidget(self.icon)
        self.horizontalLayout.addWidget(self.appName)
        self.topRightButtons = QtWidgets.QFrame(self.appBar)
        self.topRightButtons.setMinimumSize(QtCore.QSize(80, 0))
        self.topRightButtons.setMaximumSize(QtCore.QSize(150, 16777215))
        self.topRightButtons.setStyleSheet("QPushButton{"
                                           "        border-radius: 5;"
                                           f"        background-color: rgb({TOP_RIGHT_BACKGROUND[0]}, "
                                           f"{TOP_RIGHT_BACKGROUND[1]}, {TOP_RIGHT_BACKGROUND[2]});"
                                           "}"
                                           "QPushButton::hover"
                                           "{"
                                           f"        background-color : rgb({TOP_RIGHT_HOVER[0]}, {TOP_RIGHT_HOVER[1]},"
                                           f" {TOP_RIGHT_HOVER[2]});"
                                           "}")
        self.topRightButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topRightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topRightButtons.setObjectName("topRightButtons")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.topRightButtons)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimazeButton = QtWidgets.QPushButton(self.topRightButtons)
        self.minimazeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-minimize-window-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self.minimazeButton.setIcon(icon1)
        self.minimazeButton.setIconSize(QtCore.QSize(24, 24))
        self.minimazeButton.setObjectName("minimazeButton")
        self.horizontalLayout_4.addWidget(self.minimazeButton)
        self.maximazeButton = QtWidgets.QPushButton(self.topRightButtons)
        self.maximazeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-maximize-window-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self.maximazeButton.setIcon(icon2)
        self.maximazeButton.setIconSize(QtCore.QSize(24, 24))
        self.maximazeButton.setObjectName("maximazeButton")
        self.horizontalLayout_4.addWidget(self.maximazeButton)
        self.closeButton = QtWidgets.QPushButton(self.topRightButtons)
        self.closeButton.setStyleSheet("QPushButton{"
                                       "        border-radius: 5;"
                                       f"        background-color: rgb({TOP_RIGHT_BACKGROUND[0]}, "
                                       f"{TOP_RIGHT_BACKGROUND[1]}, {TOP_RIGHT_BACKGROUND[2]});"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       f"    background-color: rgb({CLOSE_BUTTON_HOVER[0]}, {CLOSE_BUTTON_HOVER[1]},"
                                       f" {CLOSE_BUTTON_HOVER[2]});"
                                       "}")
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-close-window-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_4.addWidget(self.closeButton)
        self.horizontalLayout.addWidget(self.topRightButtons, 0, Qt.Qt.AlignRight)
        self.verticalLayout.addWidget(self.appBar)
        self.mainBody = QtWidgets.QFrame(self.centralwidget)
        self.mainBody.setMinimumSize(QtCore.QSize(0, 0))
        self.mainBody.setStyleSheet(f"background-color: rgb({MAIN_BODY_BACKGROUND[0]}, "
                                    f"{MAIN_BODY_BACKGROUND[1]}, {MAIN_BODY_BACKGROUND[2]});")
        self.mainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBody.setObjectName("mainBody")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainBody)
        self.stackedWidget.setStyleSheet("QPushButton{"
                                         f"    background-color: rgb({BUTTON_COLOR[0]}, "
                                         f"{BUTTON_COLOR[1]}, {BUTTON_COLOR[2]});"
                                         "    border-radius: 15;"
                                         "}"
                                         "QPushButton::hover"
                                         "{"
                                         f"    background-color: rgb({BUTTON_HOVER[0]}, {BUTTON_HOVER[1]},"
                                         f" {BUTTON_HOVER[2]});"
                                         "}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.optionButtons = QtWidgets.QWidget()
        self.optionButtons.setStyleSheet("")
        self.optionButtons.setObjectName("optionButtons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.optionButtons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttons = QtWidgets.QFrame(self.optionButtons)
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.gridLayout = QtWidgets.QGridLayout(self.buttons)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.rarPack = QtWidgets.QPushButton(self.buttons)
        self.rarPack.setMinimumSize(QtCore.QSize(150, 150))
        self.rarPack.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rarPack.setFont(font)
        self.rarPack.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-rar-32.png"), Qt.QIcon.Normal, Qt.QIcon.Off)
        self.rarPack.setIcon(icon4)
        self.rarPack.setIconSize(QtCore.QSize(32, 32))
        self.rarPack.setObjectName("rarPack")
        self.gridLayout.addWidget(self.rarPack, 0, 0, 1, 1)
        self.zipPack = QtWidgets.QPushButton(self.buttons)
        self.zipPack.setMinimumSize(QtCore.QSize(150, 150))
        self.zipPack.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zipPack.setFont(font)
        self.zipPack.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-zip-32.png"), Qt.QIcon.Normal, Qt.QIcon.Off)
        self.zipPack.setIcon(icon5)
        self.zipPack.setIconSize(QtCore.QSize(32, 32))
        self.zipPack.setObjectName("zipPack")
        self.gridLayout.addWidget(self.zipPack, 0, 1, 1, 1)
        self.unpack = QtWidgets.QPushButton(self.buttons)
        self.unpack.setMinimumSize(QtCore.QSize(150, 150))
        self.unpack.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unpack.setFont(font)
        self.unpack.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-unpacking-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self.unpack.setIcon(icon6)
        self.unpack.setIconSize(QtCore.QSize(32, 32))
        self.unpack.setObjectName("unpack")
        self.gridLayout.addWidget(self.unpack, 1, 0, 1, 1)
        self.convert = QtWidgets.QPushButton(self.buttons)
        self.convert.setMinimumSize(QtCore.QSize(150, 150))
        self.convert.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convert.setFont(font)
        self.convert.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-export-pdf-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self.convert.setIcon(icon7)
        self.convert.setIconSize(QtCore.QSize(32, 32))
        self.convert.setObjectName("convert")
        self.gridLayout.addWidget(self.convert, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.buttons)
        self.bottomBar = QtWidgets.QFrame(self.optionButtons)
        self.bottomBar.setMinimumSize(QtCore.QSize(0, 60))
        self.bottomBar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.bottomBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomBar.setObjectName("bottomBar")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.bottomBar)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.changeTheme = QtWidgets.QPushButton(self.bottomBar)
        self.changeTheme.setMinimumSize(QtCore.QSize(40, 40))
        self.changeTheme.setMaximumSize(QtCore.QSize(40, 40))
        self.changeTheme.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-moon-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self.changeTheme.setIcon(icon8)
        self.changeTheme.setIconSize(QtCore.QSize(32, 32))
        self.changeTheme.setObjectName("changeTheme")
        self.horizontalLayout_7.addWidget(self.changeTheme, 0, Qt.Qt.AlignLeft)
        self.infoResurses = QtWidgets.QPushButton(self.bottomBar)
        self.infoResurses.setMinimumSize(QtCore.QSize(40, 40))
        self.infoResurses.setMaximumSize(QtCore.QSize(40, 40))
        self.infoResurses.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-info-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self.infoResurses.setIcon(icon9)
        self.infoResurses.setIconSize(QtCore.QSize(32, 32))
        self.infoResurses.setObjectName("infoResurses")
        self.horizontalLayout_7.addWidget(self.infoResurses, 0, Qt.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.bottomBar)
        self.stackedWidget.addWidget(self.optionButtons)
        self.convertor = QtWidgets.QWidget()
        self.convertor.setStyleSheet("")
        self.convertor.setObjectName("convertor")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.convertor)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.convertor_windows = QtWidgets.QStackedWidget(self.convertor)
        self.convertor_windows.setObjectName("convertor_windows")

        self.main_page = QList()  # TODO

        self.main_page.setObjectName("main_page")
        self.convertor_windows.addWidget(self.main_page)

        self.helper_window = HelperPage()

        self.convertor_windows.addWidget(self.helper_window)  # TODO Helper Window

        self.convertor_windows.setCurrentIndex(1)

        self.helper_window.on_dragging.connect(self.set_main_page)  # TODO Slot

        self.verticalLayout_2.addWidget(self.convertor_windows)
        self.bottom = QtWidgets.QFrame(self.convertor)
        self.bottom.setMinimumSize(QtCore.QSize(0, 80))
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 80))
        self.bottom.setStyleSheet("")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addFile = QtWidgets.QPushButton(self.bottom)
        self.addFile.setMinimumSize(QtCore.QSize(100, 50))
        self.addFile.setMaximumSize(QtCore.QSize(100, 50))
        self.addFile.setStyleSheet("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-add-file-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self.addFile.setIcon(icon10)
        self.addFile.setIconSize(QtCore.QSize(32, 32))
        self.addFile.setObjectName("addFile")
        self.horizontalLayout_3.addWidget(self.addFile, 0, Qt.Qt.AlignLeft)
        self.generate = QtWidgets.QPushButton(self.bottom)
        self.generate.setMinimumSize(QtCore.QSize(400, 50))
        self.generate.setMaximumSize(QtCore.QSize(400, 50))
        self.generate.setStyleSheet("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self.generate.setIcon(icon11)
        self.generate.setIconSize(QtCore.QSize(32, 32))
        self.generate.setObjectName("generate")
        self.horizontalLayout_3.addWidget(self.generate, 0, Qt.Qt.AlignHCenter)
        self.delFile = QtWidgets.QPushButton(self.bottom)
        self.delFile.setMinimumSize(QtCore.QSize(100, 50))
        self.delFile.setMaximumSize(QtCore.QSize(100, 50))
        self.delFile.setStyleSheet("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-delete-file-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self.delFile.setIcon(icon12)
        self.delFile.setIconSize(QtCore.QSize(32, 32))
        self.delFile.setObjectName("delFile")
        self.horizontalLayout_3.addWidget(self.delFile, 0, Qt.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.bottom)
        self.stackedWidget.addWidget(self.convertor)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "ZipPer"))
        self.rarPack.setText(_translate("MainWindow", "Pack in .rar"))
        self.zipPack.setText(_translate("MainWindow", "Pack in .zip"))
        self.unpack.setText(_translate("MainWindow", "Unpack"))
        self.convert.setText(_translate("MainWindow", "Word to pdf"))
        self.addFile.setText(_translate("MainWindow", "Add"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.delFile.setText(_translate("MainWindow", "Delete"))

    def set_main_page(self):
        self.convertor_windows.setCurrentIndex(0)

    def set_helper_page(self):
        self.convertor_windows.setCurrentIndex(1)


class HelperPage(QWidget):
    """
    This window show prompt for user, that it can use drag and drop, as soon as the user starts dragging the file,
    this class sends a signal to change the window to set the main window
    """

    on_dragging = QtCore.pyqtSignal()

    def __init__(self):
        super(HelperPage, self).__init__(parent=None)
        self.setAcceptDrops(True)

        self.setObjectName("helper_window")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.helper_frame = QtWidgets.QFrame(self)
        self.helper_frame.setMinimumSize(QtCore.QSize(400, 100))
        self.helper_frame.setMaximumSize(QtCore.QSize(400, 100))
        self.helper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helper_frame.setObjectName("helper_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.helper_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.icon_helper = QtWidgets.QLabel(self.helper_frame)
        self.icon_helper.setText("")
        self.icon_helper.setPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-drag-and-drop-32.png"))
        self.icon_helper.setObjectName("icon_helper")
        self.horizontalLayout_9.addWidget(self.icon_helper)
        self.text_helper = QtWidgets.QLabel(self.helper_frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.text_helper.setFont(font)
        self.text_helper.setObjectName("text_helper")
        self.horizontalLayout_9.addWidget(self.text_helper)
        self.horizontalLayout_8.addWidget(self.helper_frame, 0, Qt.Qt.AlignHCenter | Qt.Qt.AlignVCenter)
        self.text_helper.setText("Drag and Drop your files here")

    def dragEnterEvent(self, event):
        self.on_dragging.emit()


class QCustomQWidget(QWidget):
    """
    Class of custom element QListWidget, has an icon and text, icon and text, the icon is selected from the system
    for a specific file type, you can set the color of the text
    """

    def __init__(self, txt_color: list = None):
        """
        Initialization
        :param txt_color: Optional parameter - text color array of 3 rgb elements, each element must be < 256.
        """
        super(QCustomQWidget, self).__init__()

        if txt_color and (len(txt_color) != 3 or not all(color < 256 for color in txt_color)):
            raise Exception("Color list must have 3 elements: [red, green, blue] and they must be <= 255")

        self.text_color = txt_color

        self.horizontal_layout = QHBoxLayout()

        self.file_name = QLabel()
        self.file_icon = QLabel()

        self.horizontal_layout.addWidget(self.file_icon, 0)
        self.horizontal_layout.addWidget(self.file_name, 1)

        self.setLayout(self.horizontal_layout)

        if self.text_color:
            red, green, blue = self.text_color
            self.file_name.setStyleSheet(f'''
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
        self.file_icon.setPixmap(pixmap)

    def set_file_name(self, text):
        self.file_name.setText(text)


class QList(QWidget):
    """
    The class representing the work of QListWidget, supports the
    drag and drop function, works together with QCustomQWidget
    """

    def __init__(self):
        super(QList, self).__init__(parent=None)
        self.list_widget = QListWidget(self)
        self.setAcceptDrops(True)

        self.setStyleSheet("background-color: rgb(175, 182, 190);"
                           "border: 0px")
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.list_widget)
        self.setLayout(window_layout)

    def add_file(self, path_to_file: str):
        custom_widget = QCustomQWidget()
        custom_widget.set_file_name(os.path.basename(path_to_file))
        custom_widget.set_file_icon(path_to_file)

        list_item = QListWidgetItem()
        list_item.setSizeHint(custom_widget.sizeHint())

        self.list_widget.addItem(list_item)
        self.list_widget.setItemWidget(list_item, custom_widget)

    def delete_file(self):
        pass

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            self.add_file(f)
