"""This module is for converting files, main logic"""

# Standard library imports
import os
import zipfile
from typing import List
from pathlib import Path

# Third party imports
from PyQt5 import QtCore

# Local application imports
from .file_handler import FileHandler

FOLDER_SUFFIX = ''
PATH_LIST = List[Path]
ZIP = ".zip"


class Archiver(QtCore.QObject):
    """Class for converting files"""

    process_percent = QtCore.pyqtSignal(int)  # Signal with the number of sorted files as a percentage

    def __init__(self):
        super(Archiver, self).__init__()
        self._file_handler = FileHandler()

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

        # This is necessary because open expects a str type
        result_dir = str(Path.joinpath(result_dir, archive_name + ZIP))

        total_files_size = self._file_handler.get_total_size(path_files_to_convert)
        size_processed_files = 0

        # Check division by zero
        if total_files_size == 0:
            total_files_size = 1
            size_processed_files = 1

        # Compression mode difference - compress or not compress
        z_archive = zipfile.ZipFile(result_dir, 'w', zipfile.ZIP_DEFLATED) if compression else \
            zipfile.ZipFile(result_dir, 'w', zipfile.ZIP_STORED)

        for path in path_files_to_convert:
            self._file_handler.write_in_archive(path, z_archive)
            size_processed_files += os.path.getsize(path)
            self._emit_progress_signal(size_processed_files, total_files_size)

            for nested_paths in path.glob('**/*'):  # If path to folder -> looping through the folder
                self._file_handler.write_in_archive(nested_paths, z_archive, folder_path=path)
                size_processed_files += os.path.getsize(nested_paths)
                self._emit_progress_signal(size_processed_files, total_files_size)

        z_archive.close()

    def unzip_archives(self, archives_paths: PATH_LIST, result_dir: Path, result_folder_name: str) -> None:
        """
        Unpacks a .zip archive into the specified directory
        Also, at runtime, it sends a signal - the percentage of converted files
        :param archives_paths: List with path to files
        :param result_dir: Directory where to save the folder
        :param result_folder_name: Folder name
        :return: None
        """

        total_files = self._file_handler.count_files_in_archives(archives_paths)
        processed_files = 0
        for path_to_archive in archives_paths:
            # This is necessary because open expects a str type
            path_to_archive = str(path_to_archive)
            with zipfile.ZipFile(path_to_archive, "r") as zip_file:
                files_info_list = zip_file.infolist()
                for info_about_file in files_info_list:
                    # This is necessary for correct work with files/folders named with Russian letters
                    # because when working with folders/files named with Russian letters,
                    # they are incorrectly encoded and random unicode characters are obtained
                    info_about_file.filename = info_about_file.filename.encode('cp437').decode('cp866')
                    zip_file.extract(info_about_file, str(Path.joinpath(result_dir, result_folder_name)))

                    processed_files += 1
                    self._emit_progress_signal(processed_files, total_files)

    def _emit_progress_signal(self, processed: int, total: int) -> QtCore.pyqtSignal(int):
        """
        Sends a signal with the number of percent of the work done
        :param processed: Count processed files or size
        :param total: Total files or size
        :return: Emit signal
        """
        percent = 100 * processed / total
        # TODO FIX THIS

        # Since calculations often produce floating point numbers and rounding produces
        # an integer that has already been sent by the signal, I do this check to avoid unnecessary signals

        # if round(percent) == int(percent) and percent % 1 > 5:
        #     self.process_percent.emit(percent)
