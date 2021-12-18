"""This module is for converting files"""
import zipfile
import os
from PyQt5 import QtCore
from pathlib import Path

_FOLDER_SUFFIX = ''


class FileConvertor(QtCore.QObject):
    """Class for converting files"""

    process_percent = QtCore.pyqtSignal(int)  # Signal with the number of sorted files as a percentage

    def __init__(self):
        super(FileConvertor, self).__init__()
        self._total_files_size = 0
        self._count_processed_files = 0

    def zip_convert(self, path_files_to_convert: list, result_dir: Path, archive_name: str, compression: bool = True):
        """
        This method converts the list of files into a zip archive, and compresses it.
        Also, at runtime, it sends a process percent signal with the value of the number of processed files (in percent)
        :param path_files_to_convert: List with path to files (Using pathlib)
        :param result_dir: Directory where to save the archive
        :param archive_name: The name to be assigned to the archive
        :param compression: Archive compression flag
        :return: None
        """
        result_dir = "C:/test_folder/" + archive_name + ".zip"
        # TODO Change here

        self._total_files_size = _get_total_size(path_files_to_convert)

        z_archive = zipfile.ZipFile(result_dir, 'w', zipfile.ZIP_DEFLATED) if compression else \
            zipfile.ZipFile(result_dir, 'w', zipfile.ZIP_STORED)

        for path in path_files_to_convert:
            self._write_file_and_notify(path, z_archive)
            for nested_paths in path.glob('**/*'):  # If path to folder -> looping through the folder
                self._write_file_and_notify(nested_paths, z_archive, folder_path=path)
        z_archive.close()

        self._total_files_size = 0
        self._count_processed_files = 0

    def unzip_archive(self, path_to_archive, result_dir):
        """
        Unpacks a .zip archive into the specified directory
        Also, at runtime, it sends a signal - the percentage of converted files
        :param path_to_archive:
        :param result_dir:
        :return: None
        """
        with zipfile.ZipFile(path_to_archive, "r") as zip_file:
            path_list = zip_file.namelist()
            print(path_list)
            total_size = len(path_list)
            current_size = 0
            for file_path in path_list:
                zip_file.extract(file_path, "C:/test_folder/")
                # TODO Change here
                current_size += 1
                self.process_percent.emit((current_size / total_size) * 100)

    def _write_file_and_notify(self, path_to_file, archive: zipfile.ZipFile, folder_path=None):
        percent = 100 * self._count_processed_files / self._total_files_size

        index = path_to_file.parts.index(folder_path.name) if folder_path else path_to_file.parts.index(
            path_to_file.name)
        path_without_root = Path(*path_to_file.parts[index:])  # Path without root files
        archive.write(path_to_file, path_without_root)  # Write nested path without root

        self.process_percent.emit(percent)
        self._count_processed_files += os.path.getsize(path_to_file)


def _get_total_size(path_files_to_convert: list):
    total_size = 0
    for path in path_files_to_convert:
        for nested_paths in path.glob('**/*'):
            total_size += os.path.getsize(nested_paths)
        total_size += os.path.getsize(path)
    return total_size
