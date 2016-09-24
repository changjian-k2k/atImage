# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
import cv2
import numpy as np
from PIL import Image


class SimpleISP(QObject):
    def __init__(self):
        super(SimpleISP, self).__init__()

    @staticmethod
    def bgra_rgb_converter(data):
        rlt = (int(data[2] * 100) / 100, int(data[1] * 100) / 100, int(data[0] * 100) / 100)
        return rlt

    @staticmethod
    def float_format(data):
        # rlt = tuple([int(x*100)/100 for x in data])
        rlt = (int(data[0] * 100) / 100, int(data[1] * 100) / 100, int(data[2] * 100) / 100)
        return rlt

    @staticmethod
    def get_image_data(file_path, roi=None):
        im = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if im is None:
            pil_image = Image.open(file_path).convert('RGBA')
            im = np.array(pil_image)
            im = cv2.cvtColor(im, cv2.COLOR_RGBA2BGRA)

        height, width, channel = im.shape
        if (roi is not None and roi[0] >= 0 and roi[1] >= 0 and roi[2] > roi[0] and roi[3] > roi[1] and roi[2] <= 1 and \
                        roi[3] <= 1):
            c1 = round(width * roi[0])
            c2 = round(width * roi[2])
            r1 = round(height * roi[1])
            r2 = round(height * roi[3])
            im = im[r1:r2, c1:c2]

        return im

    @staticmethod
    def calculate_mean_std(file_path, roi=None, gray=False, pedestal=0):
        im = SimpleISP.get_image_data(file_path, roi)
        im[im < pedestal] = pedestal
        im -= pedestal
        if im is None:
            rlt_mean = (0,0,0)
            rlt_std = (0,0,0)
        else:
            if gray is False:
                rlt_mean, rlt_std = cv2.meanStdDev(im)
            else:
                im = cv2.cvtColor(im, cv2.COLOR_BGRA2GRAY)
                tmp_mean, tmp_std = cv2.meanStdDev(im)
                rlt_mean = tuple([tmp_mean]*3)
                rlt_std = tuple([tmp_std]*3)

        mean = SimpleISP.bgra_rgb_converter(rlt_mean)
        std = SimpleISP.bgra_rgb_converter(rlt_std)
        # rlt = (int(rlt_raw[2] * 100) / 100, int(rlt_raw[1] * 100) / 100, int(rlt_raw[0] * 100) / 100)

        return mean, std

    @staticmethod
    def calculate_mean_snr(file_path, roi=None, gray=False, pedestal=0):
        raw_mean, std = SimpleISP.calculate_mean_std(file_path, roi, gray, pedestal)
        if 0 in std:
            raw_snr = std
        else:
            raw_snr = 20 * np.log10(np.array(raw_mean)/np.array(std))

        mean = SimpleISP.float_format(raw_mean)
        snr = SimpleISP.float_format(raw_snr)

        return mean, snr
