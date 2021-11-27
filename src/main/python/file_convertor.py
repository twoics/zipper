import zipfile
import os
from PyQt5 import QtCore
from pathlib import Path


class FileConvertor(QtCore.QObject):
    """Class for converting files"""

    process_percent = QtCore.pyqtSignal(int)

    def __init__(self):
        super(FileConvertor, self).__init__()

    def zip_convert(self, path_files_to_convert: list, result_dir: Path, archive_name: str):
        """
        This method converts the list of files into a zip archive, and compresses it.
        Also, at runtime, it sends a process percent signal with the value of the number of processed files (in percent)
        :param path_files_to_convert: List with path to files (Using pathlib)
        :param result_dir: Directory where to save the archive
        :param archive_name: The name to be assigned to the archive
        :return: None
        """
        result_dir = "D:/test_folder/" + archive_name + ".zip"
        total_size = 0
        for path in path_files_to_convert:
            total_size += os.path.getsize(path)

        current_size = 0
        z_archive = zipfile.ZipFile(result_dir, 'w', zipfile.ZIP_DEFLATED)
        for path in path_files_to_convert:
            percent = 100 * current_size / total_size
            self.process_percent.emit(percent)
            z_archive.write(path, os.path.basename(path))
            current_size += os.path.getsize(path)
        z_archive.close()
