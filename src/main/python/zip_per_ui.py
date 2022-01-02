"""This module is the UI of the application, all the main widgets are located here."""
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from information_window import _HelperPage
from files_list import _QList
from path_selection_widget import Dialog
import zip_per_icons

# Colors
_MAIN_BACKGROUND_COLOR = [175, 182, 190]
_BUTTON_COLOR = [222, 226, 230]
_BUTTON_HOVER = [220, 220, 221]
_APP_NAME = [255, 255, 255]
_TOP_RIGHT_HOVER = [220, 220, 221]
_TOP_RIGHT_BACKGROUND = [173, 181, 189]
_CLOSE_BUTTON_HOVER = [255, 94, 91]
_MAIN_BODY_BACKGROUND = [173, 181, 189]

# Operation mode
_CREATE_ZIP_WITH_COMPRESS = 1
_CREATE_ZIP_NOT_COMPRESS = 2
_UNZIP = 3


class UiZipPer(QMainWindow):
    """Main UI"""
    generate_file_signal = QtCore.pyqtSignal(list, int)  # Signal from UI to controller, to start processing files

    # list - files paths, int - operation mode

    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self._operating_mode = None

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
        self._create_zip_with_compress = QtWidgets.QPushButton(self._buttons)
        self._create_zip_not_compress = QtWidgets.QPushButton(self._buttons)
        self._unpack_zip = QtWidgets.QPushButton(self._buttons)
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
        self._init_signals_and_slots()

        # Create UI
        self._setup_ui(self)

    def _init_signals_and_slots(self):
        self._helper_window.on_dragging.connect(self._set_main_convertor)

        self._main_list.added_file.connect(self._update_window)

        self._backButton.clicked.connect(self._open_main_page)

        # Opens the page and notify about change status
        self._create_zip_with_compress.clicked.connect(
            lambda: self._set_convertor_page_with_mode(_CREATE_ZIP_WITH_COMPRESS))
        self._create_zip_not_compress.clicked.connect(
            lambda: self._set_convertor_page_with_mode(_CREATE_ZIP_NOT_COMPRESS))
        self._unpack_zip.clicked.connect(
            lambda: self._set_convertor_page_with_mode(_UNZIP))

        self._addFile.clicked.connect(
            lambda: self._main_list.add_file(QFileDialog.getOpenFileName()[0]))
        self._delFile.clicked.connect(
            lambda: self._main_list.delete_file())

        self._generate.clicked.connect(self._check_and_emit_signal_to_controller)

    def _setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(954, 643)
        self._central_widget.setStyleSheet(f"background-color: rgb({_MAIN_BACKGROUND_COLOR[0]}, "
                                           f"{_MAIN_BACKGROUND_COLOR[1]}, {_MAIN_BACKGROUND_COLOR[2]});")
        self._central_widget.setObjectName("centralwidget")
        self._verticalLayout.setContentsMargins(0, 0, 0, 0)
        self._verticalLayout.setSpacing(0)
        self._verticalLayout.setObjectName("verticalLayout")
        self._appBar.setMinimumSize(QtCore.QSize(0, 70))
        self._appBar.setMaximumSize(QtCore.QSize(16777215, 70))
        self._appBar.setStyleSheet("QPushButton{"
                                   f"background-color: rgb({_BUTTON_COLOR[0]}, {_BUTTON_COLOR[1]}, {_BUTTON_COLOR[2]});"
                                   "    border-radius: 15;"
                                   "}"
                                   "QPushButton::hover"
                                   "{"
                                   f"    background-color: rgb({_BUTTON_HOVER[0]}, {_BUTTON_HOVER[1]}, "
                                   f"{_BUTTON_HOVER[2]});"
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
                                            f"        background-color: rgb({_TOP_RIGHT_BACKGROUND[0]}, "
                                            f"{_TOP_RIGHT_BACKGROUND[1]}, {_TOP_RIGHT_BACKGROUND[2]});"
                                            "}"
                                            "QPushButton::hover"
                                            "{"
                                            f"        background-color : rgb({_TOP_RIGHT_HOVER[0]}, "
                                            f"{_TOP_RIGHT_HOVER[1]},"
                                            f" {_TOP_RIGHT_HOVER[2]});"
                                            "}")
        self._topRightButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._topRightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self._topRightButtons.setObjectName("topRightButtons")
        self._horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._minimizeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/minimize.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._minimizeButton.setIcon(icon1)
        self._minimizeButton.setIconSize(QtCore.QSize(24, 24))
        self._minimizeButton.setObjectName("minimazeButton")
        self._horizontalLayout_4.addWidget(self._minimizeButton)
        self._maximizeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/maximize.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._maximizeButton.setIcon(icon2)
        self._maximizeButton.setIconSize(QtCore.QSize(24, 24))
        self._maximizeButton.setObjectName("maximazeButton")
        self._horizontalLayout_4.addWidget(self._maximizeButton)
        self._closeButton.setStyleSheet("QPushButton{"
                                        "        border-radius: 5;"
                                        f"        background-color: rgb({_TOP_RIGHT_BACKGROUND[0]}, "
                                        f"{_TOP_RIGHT_BACKGROUND[1]}, {_TOP_RIGHT_BACKGROUND[2]});"
                                        "}"
                                        "QPushButton::hover"
                                        "{"
                                        f"    background-color: rgb({_CLOSE_BUTTON_HOVER[0]}, {_CLOSE_BUTTON_HOVER[1]},"
                                        f" {_CLOSE_BUTTON_HOVER[2]});"
                                        "}")
        self._closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/close.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._closeButton.setIcon(icon3)
        self._closeButton.setIconSize(QtCore.QSize(24, 24))
        self._closeButton.setObjectName("closeButton")
        self._horizontalLayout_4.addWidget(self._closeButton)
        self._horizontalLayout.addWidget(self._topRightButtons, 0, Qt.Qt.AlignRight)
        self._verticalLayout.addWidget(self._appBar)
        self._mainBody.setMinimumSize(QtCore.QSize(0, 0))
        self._mainBody.setStyleSheet(f"background-color: rgb({_MAIN_BODY_BACKGROUND[0]}, "
                                     f"{_MAIN_BODY_BACKGROUND[1]}, {_MAIN_BODY_BACKGROUND[2]});")
        self._mainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._mainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self._mainBody.setObjectName("mainBody")
        self._horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_2.setSpacing(0)
        self._horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._stackedWidget.setStyleSheet("QPushButton{"
                                          f"    background-color: rgb({_BUTTON_COLOR[0]}, "
                                          f"{_BUTTON_COLOR[1]}, {_BUTTON_COLOR[2]});"
                                          "    border-radius: 15;"
                                          "}"
                                          "QPushButton::hover"
                                          "{"
                                          f"    background-color: rgb({_BUTTON_HOVER[0]}, {_BUTTON_HOVER[1]},"
                                          f" {_BUTTON_HOVER[2]});"
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
        self._create_zip_with_compress.setMinimumSize(QtCore.QSize(150, 150))
        self._create_zip_with_compress.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._create_zip_with_compress.setFont(font)
        self._create_zip_with_compress.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/compress_and_create-depositphotos-bgremover.png"),
                        Qt.QIcon.Normal, Qt.QIcon.Off)
        self._create_zip_with_compress.setIcon(icon4)
        self._create_zip_with_compress.setIconSize(QtCore.QSize(32, 32))
        self._create_zip_with_compress.setObjectName("rarPack")
        self._gridLayout.addWidget(self._create_zip_with_compress, 0, 0, 1, 1)
        self._create_zip_not_compress.setMinimumSize(QtCore.QSize(150, 150))
        self._create_zip_not_compress.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._create_zip_not_compress.setFont(font)
        self._create_zip_not_compress.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-archive-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._create_zip_not_compress.setIcon(icon5)
        self._create_zip_not_compress.setIconSize(QtCore.QSize(32, 32))
        self._create_zip_not_compress.setObjectName("zipPack")
        self._gridLayout.addWidget(self._create_zip_not_compress, 0, 1, 1, 1)
        self._unpack_zip.setMinimumSize(QtCore.QSize(150, 150))
        self._unpack_zip.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._unpack_zip.setFont(font)
        self._unpack_zip.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/unpack.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._unpack_zip.setIcon(icon6)
        self._unpack_zip.setIconSize(QtCore.QSize(32, 32))
        self._unpack_zip.setObjectName("unpack")
        self._gridLayout.addWidget(self._unpack_zip, 0, 2, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(10)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/file_change.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
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
        self._create_zip_with_compress.setText(_translate("MainWindow", "Compression"))
        self._create_zip_not_compress.setText(_translate("MainWindow", "Not Compress"))
        self._unpack_zip.setText(_translate("MainWindow", "Unpack"))
        self._addFile.setText(_translate("MainWindow", "Add"))
        self._generate.setText(_translate("MainWindow", "Generate"))
        self._delFile.setText(_translate("MainWindow", "Delete"))

    def _open_main_page(self):
        self._main_list.delete_all()
        self._set_helper_convertor()
        self._stackedWidget.setCurrentIndex(0)

    def _set_convertor_page_with_mode(self, mode):
        self._operating_mode = mode
        self._stackedWidget.setCurrentIndex(1)

    def _set_main_convertor(self):
        self._convertor_windows.setCurrentIndex(0)

    def _set_helper_convertor(self):
        self._convertor_windows.setCurrentIndex(1)

    def _update_window(self):
        if self._convertor_windows.currentIndex() == 1:
            self._set_main_convertor()

    def _check_and_emit_signal_to_controller(self):
        files_list = self._main_list.get_files_path()
        dlg = Dialog(self)
        dlg.exec()

        if self._operating_mode == _UNZIP:
            for file in files_list:
                if file.suffix != ".zip":
                    QMessageBox.warning(self, "Error",
                                        f"Only .ZIP files are available for unpacking, but a {str(file.suffix).upper()}"
                                        f" file of type was found")
                    return

        self.generate_file_signal.emit(files_list, self._operating_mode)
