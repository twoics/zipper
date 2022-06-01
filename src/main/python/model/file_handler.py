"""
A module that implements a class with static methods of working with a file
"""

# Standard library imports
import os
import zipfile
from pathlib import Path
from typing import List


class FileHandler:
    """Auxiliary class for the archiver"""

    PATH_LIST = List[Path]

    @staticmethod
    def write_in_archive(path_to_file: Path, archive: zipfile.ZipFile, folder_path: Path = None) -> None:
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

    @staticmethod
    def get_total_size(path_files_to_convert: PATH_LIST) -> int:
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

    @staticmethod
    def count_files_in_archives(archives_paths: PATH_LIST) -> int:
        """
        Counts the number of files in all the archives transferred in the list
        :param archives_paths: List with archives paths
        :return: Count files
        """
        count_archives = 0
        for archive in archives_paths:
            with zipfile.ZipFile(str(archive), "r") as zip_file:
                count_archives += len(zip_file.namelist())
        return count_archives
