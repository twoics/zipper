"""
This module implements an abstract UI class,
but in it I don't set its behavior,
could say it's an interface.
In what follows I will use the notion of interface,
for abstract classes of this type
"""

from abc import ABC, abstractmethod
from PyQt5 import QtCore
from pathlib import Path


class IView(ABC):
    """
    Interface for the UI
    """

    @abstractmethod
    def get_processing_signal(self) -> QtCore.pyqtSignal(list, int, Path, str):
        """
        Returns the signal for listening,
        emitted when user start files processing
        :return: Signal for listening
        """
        pass

    @abstractmethod
    def get_change_theme_signal(self) -> QtCore.pyqtSignal():
        """
        Returns the signal to be listened to,
        which is emitted when the user wants to change the theme
        :return: Signal for listening
        """
        pass

    @abstractmethod
    def set_theme(self, color_dict: dict) -> None:
        """
        Sets the application theme,
        based on the colors passed in colors_dict
        :param color_dict: Dictionary of colors
        Keys:
            "main_background_color"
            "button_color"
            "button_hover"
            "app_name"
            "top_rights_buttons_hover"
            "top_rights_buttons"
            "close_button_hover"
            "main_body_background"
            "style"
        Values:
            [red, green, blue]
            for style: on of {dark, light}
        :return: None
        """
        pass

    @abstractmethod
    def set_progress_value(self, value: int) -> None:
        """
        Takes the value of the progress
        :param value: Current progress value
        :return: None
        """
        pass

    @abstractmethod
    def reset_ui(self) -> None:
        """
        Resets the ui and displays the first window
        :return:None
        """
        pass
