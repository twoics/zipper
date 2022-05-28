"""
This module implements an abstract UI class,
but in it I don't set its behavior,
could say it's an interface.
In what follows I will use the notion of interface,
for abstract classes of this type
"""

from abc import ABC, abstractmethod
from PyQt5 import QtCore


class IView(ABC):
    """
    Interface for the UI
    """
    @abstractmethod
    def get_processing_signal(self) -> QtCore.pyqtSignal:
        """
        Returns the signal for listening,
        emitted when user start files processing
        """
        pass

    @abstractmethod
    def set_progress_value(self, value: int) -> None:
        """
        Takes the value of the progress
        :param value: Current progress value
        """
        pass
