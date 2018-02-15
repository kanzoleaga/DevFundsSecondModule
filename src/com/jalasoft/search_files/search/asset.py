"""
Asset class
"""
import os
from datetime import datetime
from ctypes import wintypes

class Asset(object):
    def __init__(self, path, name):
        """

        :param path: path entered for the user to any search
        :param name:this contains file or directory name
        """

        self.path = path
        self.name = name
        self.size = os.path.getsize(path)
        self.is_directory = os.path.isdir(path)
        # Get more details
        format = '%Y-%m-%d %H:%M'
        status = os.stat(path)
        self.last_access = datetime.fromtimestamp(status.st_atime)
        self.modified = datetime.fromtimestamp(status.st_mtime)
        self.created = datetime.fromtimestamp(status.st_ctime)
        self.last_access = self.last_access.strftime(format)
        self.modified = self.modified.strftime(format)
        self.created = self.created.strftime(format)

    def get_path(self):
        return self.path

    def get_size(self):
        return self.size

    def get_is_directory(self):
        return self.is_directory

    def get_name(self):
        return self.name

    def get_last_access(self):
        return self.last_access

    def get_modified_date(self):
        return self.modified

    def get_created_date(self):
        return self.created
