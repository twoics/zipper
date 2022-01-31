"""This module is the UI of the application, all the main widgets are located here."""

# Standard library imports
from typing import List
from pathlib import Path

# Third party imports
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# Local application imports
from .files_list import QList
from .information_window import HintPage
from .progress_bar_ui import ProgressBarWindow
from .path_selection_widget import PathSelectionWidget
from . import zip_per_icons  # Don't remove it, it is an icon import
from model.base import get_current_colors_from_json, change_current_theme_in_json, get_current_theme_style

FILES_LIST = List[Path]

DARK_THEME = "dark"

ZIP = ".zip"

# Operation mode
CREATE_ZIP_WITH_COMPRESS = 1
CREATE_ZIP_NOT_COMPRESS = 2
UNZIP = 3

# Main Windows
OPERATION_MODE_SELECTION_WINDOW = 0
FILE_OPERATION_WINDOW = 1
PROGRESS_OF_PROCESSED_FILES_WINDOW = 2
PATH_SELECTION_WINDOW = 3

# Windows for working with files
FILE_LIST_WINDOW = 0
INFORMATION_WINDOW = 1

# Signal types
PATH_LIST = list
OPERATION_MODE = int
DIRECTORY = Path
NAME = str

INFORMATION_ABOUT_THIS_APP = """What is it?
This application helps you to zip and unzip files

How it works:
1) Choose one of three modes of operation: Archiving with 
compression, archiving without compression, or unzipping
2) Next, select the files you want to work with, 
the drag and drop function is also supported
3) Specify the name of the file / folder where the result of the 
work will be saved, and also indicate the directory where 
it will be stored
4) After that, wait until the application completes its work, 
after the file is created, the application itself will go 
to the main window"""


class UiZipPer(QMainWindow):
    """Main UI"""

    # This signal is used to start file processing
    signal_to_start_convert = QtCore.pyqtSignal(PATH_LIST, OPERATION_MODE, DIRECTORY, NAME)

    def __init__(self, controller_link):
        QMainWindow.__init__(self, parent=None)
        self._operating_mode = None
        self._controller = controller_link
        # Position for moving main window
        self.click_position = None

        # Colors
        self._main_background_color = None
        self._button_color = None
        self._button_hover = None
        self._app_name_color = None
        self._top_right_hover = None
        self._top_right_background = None
        self._close_button_hover = None
        self._main_body_background = None

        self._theme_icon = QtGui.QIcon()
        self._central_widget = QtWidgets.QWidget(self)
        self._verticalLayout = QtWidgets.QVBoxLayout(self._central_widget)
        self._appBar = QtWidgets.QFrame(self._central_widget)
        self._horizontalLayout = QtWidgets.QHBoxLayout(self._appBar)
        self._topLeftButton = QtWidgets.QFrame(self._appBar)
        self._horizontalLayout_5 = QtWidgets.QHBoxLayout(self._topLeftButton)
        self._back_button = QtWidgets.QPushButton(self._topLeftButton)
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
        self._main_windows = QtWidgets.QStackedWidget(self._mainBody)
        self._bar_window = ProgressBarWindow()
        self._path_selection_widget = PathSelectionWidget()
        self._optionButtons = QtWidgets.QWidget()
        self._verticalLayout_3 = QtWidgets.QVBoxLayout(self._optionButtons)
        self._buttons = QtWidgets.QFrame(self._optionButtons)
        self._gridLayout = QtWidgets.QGridLayout(self._buttons)
        self._create_zip_with_compress_button = QtWidgets.QPushButton(self._buttons)
        self._create_zip_not_compress_button = QtWidgets.QPushButton(self._buttons)
        self._unpack_zip_button = QtWidgets.QPushButton(self._buttons)
        self._bottomBar = QtWidgets.QFrame(self._optionButtons)
        self._horizontalLayout_7 = QtWidgets.QHBoxLayout(self._bottomBar)
        self._infoResources = QtWidgets.QPushButton(self._bottomBar)
        self._changeTheme = QtWidgets.QPushButton(self._bottomBar)
        self._convertor = QtWidgets.QWidget()
        self._verticalLayout_2 = QtWidgets.QVBoxLayout(self._convertor)
        self._windows_for_working_with_files = QtWidgets.QStackedWidget(self._convertor)
        self._main_list = QList()
        self._drag_and_drop_information_window = HintPage()
        self._bottom = QtWidgets.QFrame(self._convertor)
        self._horizontalLayout_3 = QtWidgets.QHBoxLayout(self._bottom)
        self._add_file_button = QtWidgets.QPushButton(self._bottom)
        self._next_button = QtWidgets.QPushButton(self._bottom)
        self._del_file_button = QtWidgets.QPushButton(self._bottom)

        self._init_slots()

        self._set_stylesheet_by_json_colors()

        self._setup_ui()

    def open_main_window_after_shutdown(self) -> None:
        self._clear_all_fields()
        self._windows_for_working_with_files.setCurrentIndex(INFORMATION_WINDOW)
        self._main_windows.setCurrentIndex(OPERATION_MODE_SELECTION_WINDOW)
        self._bar_window.set_progress_value(0)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.click_position = event.globalPos()

    def _open_main_page_by_button_click(self) -> None:
        if self._main_windows.currentIndex() != PROGRESS_OF_PROCESSED_FILES_WINDOW:
            self._clear_all_fields()
            self._windows_for_working_with_files.setCurrentIndex(INFORMATION_WINDOW)
            self._main_windows.setCurrentIndex(OPERATION_MODE_SELECTION_WINDOW)

    def _init_slots(self) -> None:
        """Connects signals and slots"""
        self._logic_slots()

        self._ui_slots()

    def _logic_slots(self) -> None:
        # Signal that starts file conversion
        self.signal_to_start_convert.connect(self._controller.run)

        # A signal that outputs data to save the result of the program
        # Upon receipt, all the necessary data is collected and sent to the "signal_to_start_convert" signal
        self._path_selection_widget.signal_with_path_and_name.connect(self._emit_signal_to_start_conversion)

        # During the work of the controller, he sends a signal indicating the number of percent of the work done,
        # we set this percentage in the progress bar
        self._controller.percent_count.connect(self._set_progress_bar_value)

    def _ui_slots(self) -> None:
        # When user drags files, remove prompt window and show the file window
        self._drag_and_drop_information_window.on_dragging.connect(self._set_window_with_files)

        # When the user has added a file, through the button, remove the prompt window and show the file window
        self._main_list.added_file.connect(self._update_window)

        # Top right buttons
        self._closeButton.clicked.connect(lambda: self.close())
        self._minimizeButton.clicked.connect(lambda: self.showMinimized())
        self._maximizeButton.clicked.connect(self._maximize_or_restore)

        # Opens the page and notify about change status
        self._create_zip_with_compress_button.clicked.connect(
            lambda: self._set_file_conversion_window_by_mode(CREATE_ZIP_WITH_COMPRESS))
        self._create_zip_not_compress_button.clicked.connect(
            lambda: self._set_file_conversion_window_by_mode(CREATE_ZIP_NOT_COMPRESS))
        self._unpack_zip_button.clicked.connect(
            lambda: self._set_file_conversion_window_by_mode(UNZIP))

        # Delete and add file buttons
        self._add_file_button.clicked.connect(
            lambda: self._main_list.add_file(QFileDialog.getOpenFileName()[0]))
        self._del_file_button.clicked.connect(
            lambda: self._main_list.delete_file())

        # By clicking this button: A window opens for selecting the path where the file and its name are saved.
        self._next_button.clicked.connect(self._open_path_selection_widget)

        # Other slots
        self._back_button.clicked.connect(self._open_main_page_by_button_click)
        self._changeTheme.clicked.connect(self._change_theme)
        self._appBar.mouseMoveEvent = self._move_window  # For moving app window

    def _set_json_colors_to_variables(self) -> None:
        """
        Get colors from JSON and set colors to variable
        :return: None
        """
        colors_dict = get_current_colors_from_json()
        self._main_background_color = colors_dict["main_background_color"]
        self._button_color = colors_dict["button_color"]
        self._button_hover = colors_dict["button_hover"]
        self._app_name_color = colors_dict["app_name"]
        self._top_right_hover = colors_dict["top_rights_buttons_hover"]
        self._top_right_background = colors_dict["top_rights_buttons"]
        self._close_button_hover = colors_dict["close_button_hover"]
        self._main_body_background = colors_dict["main_body_background"]

    def _set_stylesheet_by_json_colors(self) -> None:
        """
        Set colors to widget by colors from JSON
        :return: None
        """
        self._set_json_colors_to_variables()

        self._central_widget.setStyleSheet(f"background-color: rgb({self._main_background_color[0]}, "
                                           f"{self._main_background_color[1]}, {self._main_background_color[2]});")

        self._appBar.setStyleSheet("QPushButton{"
                                   f"background-color: rgb({self._button_color[0]}, {self._button_color[1]}, {self._button_color[2]});"
                                   "    border-radius: 15;"
                                   "}"
                                   "QPushButton::hover"
                                   "{"
                                   f"    background-color: rgb({self._button_hover[0]}, {self._button_hover[1]}, "
                                   f"{self._button_hover[2]});"
                                   "}")

        self._topRightButtons.setStyleSheet("QPushButton{"
                                            "        border-radius: 5;"
                                            f"        background-color: rgb({self._top_right_background[0]}, "
                                            f"{self._top_right_background[1]}, {self._top_right_background[2]});"
                                            "}"
                                            "QPushButton::hover"
                                            "{"
                                            f"        background-color : rgb({self._top_right_hover[0]}, "
                                            f"{self._top_right_hover[1]},"
                                            f" {self._top_right_hover[2]});"
                                            "}")

        self._closeButton.setStyleSheet("QPushButton{"
                                        "        border-radius: 5;"
                                        f"        background-color: rgb({self._top_right_background[0]}, "
                                        f"{self._top_right_background[1]}, {self._top_right_background[2]});"
                                        "}"
                                        "QPushButton::hover"
                                        "{"
                                        f"    background-color: rgb({self._close_button_hover[0]}, {self._close_button_hover[1]},"
                                        f" {self._close_button_hover[2]});"
                                        "}")

        self._mainBody.setStyleSheet(f"background-color: rgb({self._main_body_background[0]}, "
                                     f"{self._main_body_background[1]}, {self._main_body_background[2]});")

        self._main_windows.setStyleSheet("QPushButton{"
                                         f"    background-color: rgb({self._button_color[0]}, "
                                         f"{self._button_color[1]}, {self._button_color[2]});"
                                         "    border-radius: 15;"
                                         "}"
                                         "QPushButton::hover"
                                         "{"
                                         f"    background-color: rgb({self._button_hover[0]}, {self._button_hover[1]},"
                                         f" {self._button_hover[2]});"
                                         "}")

        self._name.setStyleSheet((f"color: rgb({self._app_name_color[0]}, "
                                  f"{self._app_name_color[1]}, {self._app_name_color[2]});"))

        # For Custom UI elements
        self._main_list.set_stylesheet(self._main_background_color)
        self._main_list.set_color_for_list_elements(self._app_name_color)
        self._path_selection_widget.set_text_color(self._app_name_color)
        self._bar_window.set_text_color(self._app_name_color)
        self._drag_and_drop_information_window.set_text_color(self._app_name_color)

        # Change icon by current color
        if get_current_theme_style() == DARK_THEME:
            self._theme_icon.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-sun-32.png"), Qt.QIcon.Normal,
                                       Qt.QIcon.Off)
        else:
            self._theme_icon.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-moon-32.png"), Qt.QIcon.Normal,
                                       Qt.QIcon.Off)
        self._changeTheme.setIcon(self._theme_icon)

    def _clear_all_fields(self) -> None:
        self._main_list.delete_all()
        self._path_selection_widget.clear_input_filed()

    def _maximize_or_restore(self) -> None:
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def _change_theme(self) -> None:
        """Change app-theme dark -> light or light -> dark"""
        change_current_theme_in_json()
        self._set_stylesheet_by_json_colors()

    def _check_files_list_by_empty(self, files_list: FILES_LIST) -> bool:
        if len(files_list) == 0:
            QMessageBox.warning(self, "Error", "No files found to convert")
            return False
        return True

    def _check_files_list_by_unpacking(self, files_list: FILES_LIST) -> bool:
        """
        If the archive unpacking mode is selected, it checks that all elements are in .ZIP format
        :param files_list: List with files
        :return: Is all files .ZIP format if unpacking mode is selected
        """
        if self._operating_mode == UNZIP:
            for file in files_list:
                if file.suffix != ZIP:
                    QMessageBox.warning(self, "Error",
                                        f"Only .ZIP files are available for unpacking, but a {str(file.suffix).upper()}"
                                        f" file of type was found")
                    return False
        return True

    def _emit_signal_to_start_conversion(self, result_dir: Path, name: str) -> None:
        """
        Starts processing files
        :param result_dir: Directory where to save the result
        :param name: Name of result file or folder
        :return: None
        """
        self._main_windows.setCurrentIndex(PROGRESS_OF_PROCESSED_FILES_WINDOW)
        files_list = self._main_list.get_files_path()

        # Start file processing
        self.signal_to_start_convert.emit(files_list, self._operating_mode, result_dir, name)
        # self._controller.run(files_list, self._operating_mode, result_dir, name)

    def _open_path_selection_widget(self) -> None:
        files_list = self._main_list.get_files_path()

        if not self._check_files_list_by_unpacking(files_list) or not self._check_files_list_by_empty(files_list):
            return

        self._main_windows.setCurrentIndex(PATH_SELECTION_WINDOW)

    def _set_file_conversion_window_by_mode(self, mode) -> None:
        self._operating_mode = mode
        self._main_windows.setCurrentIndex(FILE_OPERATION_WINDOW)

    def _set_window_with_files(self) -> None:
        self._windows_for_working_with_files.setCurrentIndex(FILE_LIST_WINDOW)

    def _update_window(self) -> None:
        if self._windows_for_working_with_files.currentIndex() == 1:
            self._set_window_with_files()

    def _set_progress_bar_value(self, value: int) -> None:
        self._bar_window.set_progress_value(value)

    def _move_window(self, event: QtGui.QMouseEvent) -> None:
        self.move(self.pos() + event.globalPos() - self.click_position)
        self.click_position = event.globalPos()
        event.accept()

    def _setup_ui(self) -> None:
        self.setObjectName("MainWindow")
        self.resize(954, 643)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self._central_widget.setObjectName("centralwidget")
        self._verticalLayout.setContentsMargins(0, 0, 0, 0)
        self._verticalLayout.setSpacing(0)
        self._verticalLayout.setObjectName("verticalLayout")
        self._appBar.setMinimumSize(QtCore.QSize(0, 70))
        self._appBar.setMaximumSize(QtCore.QSize(16777215, 70))
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
        self._back_button.setMinimumSize(QtCore.QSize(0, 65))
        self._back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-menu-32.png"), Qt.QIcon.Normal, Qt.QIcon.Off)
        self._back_button.setIcon(icon)
        self._back_button.setIconSize(QtCore.QSize(24, 24))
        self._back_button.setObjectName("pushButton")
        self._horizontalLayout_5.addWidget(self._back_button)
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
        self._name.setObjectName("name")
        self._horizontalLayout_6.addWidget(self._name, 0, Qt.Qt.AlignRight)
        self._icon.setText("")
        self._icon.setPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-32.png"))
        self._icon.setObjectName("icon")
        self._horizontalLayout_6.addWidget(self._icon)
        self._horizontalLayout.addWidget(self._appName)
        self._topRightButtons.setMinimumSize(QtCore.QSize(80, 0))
        self._topRightButtons.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self._mainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._mainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self._mainBody.setObjectName("mainBody")
        self._horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self._horizontalLayout_2.setSpacing(0)
        self._horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._main_windows.setObjectName("stackedWidget")
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
        self._create_zip_with_compress_button.setMinimumSize(QtCore.QSize(150, 150))
        self._create_zip_with_compress_button.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._create_zip_with_compress_button.setFont(font)
        self._create_zip_with_compress_button.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/compress_and_create-depositphotos-bgremover.png"),
                        Qt.QIcon.Normal, Qt.QIcon.Off)
        self._create_zip_with_compress_button.setIcon(icon4)
        self._create_zip_with_compress_button.setIconSize(QtCore.QSize(32, 32))
        self._create_zip_with_compress_button.setObjectName("rarPack")
        self._gridLayout.addWidget(self._create_zip_with_compress_button, 0, 0, 1, 1)
        self._create_zip_not_compress_button.setMinimumSize(QtCore.QSize(150, 150))
        self._create_zip_not_compress_button.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._create_zip_not_compress_button.setFont(font)
        self._create_zip_not_compress_button.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-archive-32.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._create_zip_not_compress_button.setIcon(icon5)
        self._create_zip_not_compress_button.setIconSize(QtCore.QSize(32, 32))
        self._create_zip_not_compress_button.setObjectName("zipPack")
        self._gridLayout.addWidget(self._create_zip_not_compress_button, 0, 1, 1, 1)
        self._unpack_zip_button.setMinimumSize(QtCore.QSize(150, 150))
        self._unpack_zip_button.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._unpack_zip_button.setFont(font)
        self._unpack_zip_button.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/unpack.png"), Qt.QIcon.Normal,
                        Qt.QIcon.Off)
        self._unpack_zip_button.setIcon(icon6)
        self._unpack_zip_button.setIconSize(QtCore.QSize(32, 32))
        self._unpack_zip_button.setObjectName("unpack")
        self._gridLayout.addWidget(self._unpack_zip_button, 0, 2, 1, 1)
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
        self._main_windows.addWidget(self._optionButtons)
        self._convertor.setStyleSheet("")
        self._convertor.setObjectName("convertor")
        self._verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self._verticalLayout_2.setSpacing(0)
        self._verticalLayout_2.setObjectName("verticalLayout_2")
        self._windows_for_working_with_files.setObjectName("convertor_windows")
        self._main_list.setObjectName("main_page")
        self._windows_for_working_with_files.addWidget(self._main_list)
        self._windows_for_working_with_files.addWidget(self._drag_and_drop_information_window)
        self._windows_for_working_with_files.setCurrentIndex(INFORMATION_WINDOW)
        self._verticalLayout_2.addWidget(self._windows_for_working_with_files)
        self._bottom.setMinimumSize(QtCore.QSize(0, 80))
        self._bottom.setMaximumSize(QtCore.QSize(16777215, 80))
        self._bottom.setStyleSheet("")
        self._bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self._bottom.setObjectName("bottom")
        self._horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._add_file_button.setMinimumSize(QtCore.QSize(100, 50))
        self._add_file_button.setMaximumSize(QtCore.QSize(100, 50))
        self._add_file_button.setStyleSheet("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-add-file-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self._add_file_button.setIcon(icon10)
        self._add_file_button.setIconSize(QtCore.QSize(32, 32))
        self._add_file_button.setObjectName("addFile")
        self._horizontalLayout_3.addWidget(self._add_file_button, 0, Qt.Qt.AlignLeft)
        self._next_button.setMinimumSize(QtCore.QSize(400, 50))
        self._next_button.setMaximumSize(QtCore.QSize(400, 50))
        self._next_button.setStyleSheet("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-create-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self._next_button.setIcon(icon11)
        self._next_button.setIconSize(QtCore.QSize(32, 32))
        self._next_button.setObjectName("generate")
        self._horizontalLayout_3.addWidget(self._next_button, 0, Qt.Qt.AlignHCenter)
        self._del_file_button.setMinimumSize(QtCore.QSize(100, 50))
        self._del_file_button.setMaximumSize(QtCore.QSize(100, 50))
        self._del_file_button.setStyleSheet("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/ZipPerIcons/icons8-delete-file-32.png"), Qt.QIcon.Normal,
                         Qt.QIcon.Off)
        self._del_file_button.setIcon(icon12)
        self._del_file_button.setIconSize(QtCore.QSize(32, 32))
        self._del_file_button.setObjectName("delFile")
        self._horizontalLayout_3.addWidget(self._del_file_button, 0, Qt.Qt.AlignRight)
        self._verticalLayout_2.addWidget(self._bottom)
        self._main_windows.addWidget(self._convertor)
        self._main_windows.addWidget(self._bar_window)
        self._main_windows.addWidget(self._path_selection_widget)
        self._horizontalLayout_2.addWidget(self._main_windows)
        self._verticalLayout.addWidget(self._mainBody)
        self.setCentralWidget(self._central_widget)

        self._translate_ui()
        self._main_windows.setCurrentIndex(OPERATION_MODE_SELECTION_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(self)

    def _translate_ui(self) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._name.setText(_translate("MainWindow", "ZipPer"))
        self._create_zip_with_compress_button.setText(_translate("MainWindow", "Compression"))
        self._create_zip_not_compress_button.setText(_translate("MainWindow", "Not Compress"))
        self._unpack_zip_button.setText(_translate("MainWindow", "Unpack"))
        self._add_file_button.setText(_translate("MainWindow", "Add"))
        self._next_button.setText(_translate("MainWindow", "Next"))
        self._del_file_button.setText(_translate("MainWindow", "Delete"))
