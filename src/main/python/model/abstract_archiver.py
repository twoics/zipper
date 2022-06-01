"""
The module implements the interface of work with the archiver
"""
# Standard library imports
from typing import List
from pathlib import Path
from abc import ABC, abstractmethod

# Third party imports
from PyQt5 import QtCore

PATH_LIST = List[Path]


class IArchiver(ABC):
    """
    Interface of the class
    that implements the archiver logic
    """
    @abstractmethod
    def get_process_signal(self) -> QtCore.pyqtSignal():
        """
        Returns the signal for listening,
        which emits a percentage of the processed files
        :return:
        """
        pass

    @abstractmethod
    def zip_convert(self, path_files_to_convert: PATH_LIST, result_dir: Path, archive_name: str,
                    compression: bool = True) -> None:
        """
        This method converts the list of files into a zip archive, and compresses it.
        Also, at runtime, it sends a process percent signal with the value of the number of processed files (in percent)
        :param path_files_to_convert: List with path to files
        :param result_dir: Directory where to save the archive
        :param archive_name: The name to be assigned to the archive
        :param compression: Archive compression flag
        :return: None
        """
        pass

    @abstractmethod
    def unzip_archives(self, archives_paths: PATH_LIST, result_dir: Path, result_folder_name: str) -> None:
        """
        Unpacks a .zip archive into the specified directory
        Also, at runtime, it sends a signal - the percentage of converted files
        :param archives_paths: List with path to files
        :param result_dir: Directory where to save the folder
        :param result_folder_name: Folder name
        :return: None
        """
        pass
