"""This module is for converting files"""
import zipfile
import os
from PyQt5 import QtCore
from pathlib import Path
from typing import List

FOLDER_SUFFIX = ''
PATH_LIST = List[Path]


class FileConvertor(QtCore.QObject):
    """Class for converting files"""

    process_percent = QtCore.pyqtSignal(int)  # Signal with the number of sorted files as a percentage

    def __init__(self):
        super(FileConvertor, self).__init__()
        self._total_files_size = 0
        self._size_processed_files = 0

    def zip_convert(self, path_files_to_convert: PATH_LIST, result_dir: Path, archive_name: str,
                    compression: bool = True):
        """
        This method converts the list of files into a zip archive, and compresses it.
        Also, at runtime, it sends a process percent signal with the value of the number of processed files (in percent)
        :param path_files_to_convert: List with path to files (Using pathlib)
        :param result_dir: Directory where to save the archive
        :param archive_name: The name to be assigned to the archive
        :param compression: Archive compression flag
        :return: None
        """
        result_dir = "C:/test/" + archive_name + ".zip"
        # TODO Change here

        self._total_files_size = _get_total_size(path_files_to_convert)

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

    def unzip_archives(self, list_archives_paths, result_dir, result_folder_name):
        """
        Unpacks a .zip archive into the specified directory
        Also, at runtime, it sends a signal - the percentage of converted files
        :param list_archives_paths:
        :param result_dir:
        :param result_folder_name:
        :return: None
        """
        total_files = len(list_archives_paths)
        processed_archives = 0
        for path_to_archive in list_archives_paths:
            with zipfile.ZipFile(path_to_archive, "r") as zip_file:
                path_list = zip_file.namelist()
                for file_path in path_list:
                    print("-")
                    zip_file.extract(file_path, "D:/test_folder/" + result_folder_name)
                    # TODO Change here
                    processed_archives += 1
                    self.process_percent.emit((processed_archives / total_files) * 100)


def _write_file(path_to_file: Path, archive: zipfile.ZipFile, folder_path: Path = None):
    index = path_to_file.parts.index(folder_path.name) if folder_path \
        else path_to_file.parts.index(path_to_file.name)

    path_without_root = Path(*path_to_file.parts[index:])  # Path without root files
    archive.write(path_to_file, path_without_root)  # Write nested path without root


def _get_total_size(path_files_to_convert: PATH_LIST):
    total_size = 0
    for path in path_files_to_convert:
        for nested_paths in path.glob('**/*'):
            total_size += os.path.getsize(nested_paths)
        total_size += os.path.getsize(path)
    return total_size
