"""This module is for converting files, main logic"""
import zipfile
import os
from PyQt5 import QtCore
from pathlib import Path
from typing import List

FOLDER_SUFFIX = ''
PATH_LIST = List[Path]
ZIP = ".zip"


class FileConvertor(QtCore.QObject):
    """Class for converting files"""

    process_percent = QtCore.pyqtSignal(int)  # Signal with the number of sorted files as a percentage

    def __init__(self):
        super(FileConvertor, self).__init__()
        self._total_files_size = 0
        self._size_processed_files = 0

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

        self._total_files_size = _get_total_size(path_files_to_convert)

        # For prevent division by zero
        if self._total_files_size == 0:
            self._total_files_size = 1
            self._size_processed_files = 1

        # Compression mode difference - compress or not compress
        z_archive = zipfile.ZipFile(result_dir, 'w', zipfile.ZIP_DEFLATED) if compression else \
            zipfile.ZipFile(result_dir, 'w', zipfile.ZIP_STORED)

        for path in path_files_to_convert:
            _write_file(path, z_archive)
            self._size_processed_files += os.path.getsize(path)
            percent = 100 * self._size_processed_files / self._total_files_size
            self.process_percent.emit(percent)

            for nested_paths in path.glob('**/*'):  # If path to folder -> looping through the folder
                _write_file(nested_paths, z_archive, folder_path=path)
                self._size_processed_files += os.path.getsize(nested_paths)
                percent = 100 * self._size_processed_files / self._total_files_size
                self.process_percent.emit(percent)

        z_archive.close()

        self._total_files_size = 0
        self._size_processed_files = 0

    def unzip_archives(self, list_archives_paths: PATH_LIST, result_dir: Path, result_folder_name: str) -> None:
        """
        Unpacks a .zip archive into the specified directory
        Also, at runtime, it sends a signal - the percentage of converted files
        :param list_archives_paths: List with path to files
        :param result_dir: Directory where to save the folder
        :param result_folder_name: Folder name
        :return: None
        """
        total_files = len(list_archives_paths)
        processed_archives = 0
        for path_to_archive in list_archives_paths:
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
                    processed_archives += 1
                    self.process_percent.emit((processed_archives / total_files) * 100)


def _write_file(path_to_file: Path, archive: zipfile.ZipFile, folder_path: Path = None) -> None:
    """
    Write file into archive
    :param path_to_file: Path to file
    :param archive: Archive to write the file to
    :param folder_path: Path to the parent directory, if any
    :return: None
    """
    index = path_to_file.parts.index(folder_path.name) if folder_path \
        else path_to_file.parts.index(path_to_file.name)

    path_without_root = Path(*path_to_file.parts[index:])  # Path without root files
    archive.write(path_to_file, path_without_root)  # Write nested path without root


def _get_total_size(path_files_to_convert: PATH_LIST) -> int:
    """
    Return total size of files to convert
    :param path_files_to_convert: List with files
    :return: total size
    """
    total_size = 0
    for path in path_files_to_convert:
        for nested_paths in path.glob('**/*'):
            total_size += os.path.getsize(nested_paths)
        total_size += os.path.getsize(path)
    return total_size
