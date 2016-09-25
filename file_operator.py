# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog
import os


class ImageFolder(QObject):
    def __init__(self):
        super(ImageFolder, self).__init__()
        self.cur_dir = None
        self.file_list = []
        self.extensions = None

    def select_folder(self, path):
        if not isinstance(path, str):
            path = os.getcwd()

        self.cur_dir = QFileDialog.getExistingDirectory(caption="选取图片所在文件夹", directory=path)

        return self.cur_dir

    def find_files(self, extension):
        self.file_list.clear()
        self.extensions = extension

        if len(self.cur_dir) is not 0:
            files = os.listdir(self.cur_dir)
            file_num = len(files)

            for iFile in range(file_num):
                file_name = files[iFile]
                file_path = os.path.join(self.cur_dir, file_name)
                file_ext = self._find_extension(file_name)

                if (file_ext in extension) and os.path.isfile(file_path):
                    self.file_list.append(file_name)

    @staticmethod
    def _find_extension(file_name):
        lists = file_name.split('.')
        if len(lists) > 1:
            file_ext = lists[-1]
            return file_ext.lower()
        else:
            return None

    def get_file_path(self, file_name):
        if file_name in self.file_list:
            temp = os.path.join(self.cur_dir, file_name)
            return os.path.normpath(temp)
        else:
            return None

