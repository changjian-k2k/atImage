#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QPen
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtWidgets import QGraphicsPixmapItem
from atImage_ui_form import Ui_Form
from file_operator import *
from simple_isp import *
import os
from qt_binder import *

c_t = "\t"

class atImage_window(QtWidgets.QWidget, Ui_Form):
    mean_update = QtCore.pyqtSignal([tuple], [list], name="meanUpdate")
    snr_update = QtCore.pyqtSignal([tuple], [list], name="snrUpdate")

    def __init__(self):
        super(atImage_window, self).__init__()
        self.setupUi(self)

        self.image_file = ImageFolder()
        self.extension_name = ['bmp', 'png', 'jpg', 'jpeg', 'tiff']
        self.rect = [-1, -1, -1, -1]
        self.item_rect = None
        self.item_img = None
        self.view_width = self.graphicsView_image.width() - 2
        self.view_height = self.graphicsView_image.height() - 2
        self.img_width = None
        self.img_height = None
        self.norm_roi = None

        self._mean_r = 0
        self._mean_g = 0
        self._mean_b = 0
        self._snr_r = 0
        self._snr_g = 0
        self._snr_b = 0

        self._rect_xStart = 0
        self._rect_yStart = 0
        self._rect_xEnd = 0
        self._rect_yEnd = 0
        self._rect_width = 0
        self._rect_height = 0

        self._gray_output = True
        self._pedestal = 0

        self.scene = QGraphicsScene(self.graphicsView_image)
        self.graphicsView_image.setScene(self.scene)
        self.graphicsView_image.setSceneRect(0, 0, self.view_width, self.view_height)
        self.graphicsView_image.show()

        self.pen_rect = QPen(QtCore.Qt.magenta, 2, QtCore.Qt.SolidLine)
        self.item_rect = QGraphicsRectItem()
        self.item_rect.setPen(self.pen_rect)

        self.pushButton_folderPath.clicked.connect(self.select_folder_path)
        self.listWidget_fileList.clicked.connect(self.update_image_show)
        self.pushButton_getMean.clicked.connect(self.show_files_mean)
        self.graphicsView_image.mousePressEvent = self.click_down_on_image
        # self.graphicsView_image.mouseReleaseEvent = self.release_up_on_image
        self.lineEdit_xStart.returnPressed.connect(self._update_xStart)
        self.lineEdit_yStart.returnPressed.connect(self._update_yStart)
        self.lineEdit_xEnd.returnPressed.connect(self._update_xEnd)
        self.lineEdit_yEnd.returnPressed.connect(self._update_yEnd)
        self.checkBox_gray_output.stateChanged.connect(self._update_gray_output)
        self.lineEdit_pedestal.textChanged.connect(self._change_pedestal)
        self.pushButton_clear_log.clicked.connect(self._clear_log)

        self.mean_update.connect(self.handle_mean_update)
        self.snr_update.connect(self.handle_snr_update)

    @property
    def mean_r(self):
        return self._mean_r

    @mean_r.setter
    def mean_r(self, value):
        self.label_mean_R.setText(str(value))
        self._mean_r = value

    @property
    def mean_g(self):
        return self._mean_g

    @mean_g.setter
    def mean_g(self, value):
        self.label_mean_G.setText(str(value))
        self._mean_g = value

    @property
    def mean_b(self):
        return self._mean_b

    @mean_b.setter
    def mean_b(self, value):
        self.label_mean_B.setText(str(value))
        self._mean_b = value

    @property
    def snr_r(self):
        return self._snr_r

    @snr_r.setter
    def snr_r(self, value):
        self.label_snr_R.setText(str(value))
        self._snr_r = value

    @property
    def snr_g(self):
        return self._snr_g

    @snr_g.setter
    def snr_g(self, value):
        self.label_snr_G.setText(str(value))
        self._snr_g = value

    @property
    def snr_b(self):
        return self._snr_b

    @snr_b.setter
    def snr_b(self, value):
        self.label_snr_B.setText(str(value))
        self._snr_b = value

    @property
    def rect_width(self):
        self._rect_width = abs(self._rect_xEnd - self._rect_xStart)
        return self._rect_width

    @rect_width.setter
    def rect_width(self, value):
        self.label_rect_width.setText(str(value))
        self._rect_width = value

    @property
    def rect_height(self):
        self._rect_height = abs(self._rect_yEnd - self._rect_yStart)
        return self._rect_height

    @rect_height.setter
    def rect_height(self, value):
        self.label_rect_height.setText(str(value))
        self._rect_height = value

    @property
    def rect_xStart(self):
        return self._rect_xStart

    @rect_xStart.setter
    def rect_xStart(self, value):
        self.lineEdit_xStart.setText(str(value))
        self._rect_xStart = value
        self._update_rect(value, 0, 0)
        self._draw_rect_on_image()

    @property
    def rect_xEnd(self):
        return self._rect_xEnd

    @rect_xEnd.setter
    def rect_xEnd(self, value):
        self.lineEdit_xEnd.setText(str(value))
        self._rect_xEnd = value
        self._update_rect(value, 0, 1)
        self._draw_rect_on_image()

    @property
    def rect_yStart(self):
        return self._rect_yStart

    @rect_yStart.setter
    def rect_yStart(self, value):
        self.lineEdit_yStart.setText(str(value))
        self._rect_yStart = value
        self._update_rect(value, 1, 0)
        self._draw_rect_on_image()

    @property
    def rect_yEnd(self):
        return self._rect_yEnd

    @rect_yEnd.setter
    def rect_yEnd(self, value):
        self.lineEdit_yEnd.setText(str(value))
        self._rect_yEnd = value
        self._update_rect(value, 1, 1)
        self._draw_rect_on_image()

    @property
    def pedestal(self):
        return self._pedestal

    @pedestal.setter
    def pedestal(self, value):
        self.lineEdit_OB.setText(str(value))
        self._pedestal = value

    def _update_rect_size(self, dim=2):
        if dim == 2:
            self.rect_width = self.rect_xEnd - self.rect_xStart
            self.rect_height = self.rect_yEnd - self.rect_yStart

        if dim == 0:
            self.rect_width = self.rect_xEnd - self.rect_xStart

        if dim == 1:
            self.rect_height = self.rect_yEnd - self.rect_yStart

    def select_folder_path(self):
        path = self.lineEdit_folderPath.text()

        self.image_file.select_folder(path)
        self.lineEdit_folderPath.setText(self.image_file.cur_dir)

        self.listWidget_fileList.clear()
        self.image_file.find_files(self.extension_name)
        self.listWidget_fileList.addItems(self.image_file.file_list)

    def get_selected_file_path(self):
        selected_item = self.listWidget_fileList.currentItem()
        if selected_item is None:
            return None
        file_path = self.image_file.get_file_path(selected_item.text())
        return file_path

    def get_mean_snr(self, file_path):
        mean, snr = SimpleISP.calculate_mean_snr(file_path, self.norm_roi, self._gray_output, self._pedestal)
        return mean, snr

    def output_mean(self, mean, snr, file_path="Null", head_flag=True):
        if self._gray_output is False:
            if head_flag is True:
                self.textEdit_results.append("")
                self.textEdit_results.append("====>>>> Image Calculation <<<<====")
                self.textEdit_results.append("==================================================================")
                self.textEdit_results.append("R_Mean\tG_Mean\tB_Mean\tR_SNR\tG_SNR\tB_SNR\tfile_path")
            self.textEdit_results.append(str(mean[0]) + c_t + str(mean[1]) + c_t+str(mean[2]) + c_t
                                         + str(snr[0]) + c_t + str(snr[1]) + c_t + str(snr[2]) + c_t + str(file_path))
        else:
            if head_flag is True:
                self.textEdit_results.append("")
                self.textEdit_results.append("====>>>> Image Calculation <<<<====")
                self.textEdit_results.append("==================================================================")
                self.textEdit_results.append("Gray_Mean\tGray_SNR\tfile_path")
            self.textEdit_results.append(str(mean[0]) + c_t + str(snr[0]) + c_t + str(file_path))

    def _update_result(self):
        file_path = self.get_selected_file_path()
        if file_path is not None:
            mean, snr = self.get_mean_snr(file_path)
            self.mean_update.emit(mean)
            self.snr_update.emit(snr)

    def update_image_show(self):
        file_path = self.get_selected_file_path()

        if file_path is not None:
            self.scene.removeItem(self.item_img)
            pixmap = QPixmap(file_path)
            self.img_width = pixmap.width()
            self.img_height = pixmap.height()
            scaled_pixmap = pixmap.scaled(self.view_width, self.view_height)
            self.item_img = QGraphicsPixmapItem(scaled_pixmap)
            self.scene.addItem(self.item_img)

            if self.norm_roi is not None:
                self._draw_rect_on_image()

            mean, snr = self.get_mean_snr(file_path)
            self.mean_update.emit(mean)
            self.snr_update.emit(snr)

    def show_files_mean(self):
        file_num = self.listWidget_fileList.count()
        for idx in range(file_num):
            file_item = self.listWidget_fileList.item(idx)
            file_path = self.image_file.get_file_path(file_item.text())

            mean, snr = self.get_mean_snr(file_path)
            if idx == 0:
                self.output_mean(mean, snr, file_path)
            else:
                self.output_mean(mean, snr, file_path, False)

    def handle_mean_update(self, mean):
        self.mean_r = mean[0]
        self.mean_g = mean[1]
        self.mean_b = mean[2]

    def handle_snr_update(self, snr):
        self.snr_r = snr[0]
        self.snr_g = snr[1]
        self.snr_b = snr[2]

    def _update_rect(self, val, dim, pos):
        if dim == 0:  # for x, width
            if val < 0:
                val = 0
            elif val > self.view_width:
                val = self.view_width

            if pos == 0:  # 0 for start
                self.rect[2] += self.rect[0] - val
                self.rect[0] = val
            elif pos == 1:  # 1 for end
                self.rect[2] = val - self.rect[0]

        elif dim == 1:  # for y, height
            if val < 0:
                val = 0
            elif val > self.view_height:
                val = self.view_height

            if pos == 0:  # 0 for start
                self.rect[3] += self.rect[1] - val
                self.rect[1] = val
            elif pos == 1:  # 1 for end
                self.rect[3] = val - self.rect[1]

        self._update_rect_size(dim)

    def set_rect(self, pos, head_flag=False):
        x = pos.x()
        y = pos.y()

        if pos.x() < 0:
            x = 0
        elif pos.x() > self.view_width:
            x = self.view_width

        if pos.y() < 0:
            y = 0
        elif pos.y() > self.view_height:
            y = self.view_height

        if head_flag is False:
            self.rect[2] = x - self.rect[0]
            self.rect[3] = y - self.rect[1]
        else:
            self.rect[0] = x
            self.rect[1] = y
            self.rect[2] = 0
            self.rect[3] = 0

            self.rect_xStart = x
            self.rect_yStart = y

        self.rect_xEnd = x
        self.rect_yEnd = y
        self._update_rect_size(2)

    def _draw_rect_on_image(self):
        self.scene.removeItem(self.item_rect)
        self.item_rect.setRect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
        self.scene.addItem(self.item_rect)

    def draw_rect_on_image(self, event):
        cur_pos = event.pos()
        self.set_rect(cur_pos)
        self._draw_rect_on_image()

    def move_on_image(self, event):
        self.draw_rect_on_image(event)

    def click_down_on_image(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            offset = event.pos()
            self.set_rect(offset, True)
            self.graphicsView_image.mouseMoveEvent = self.move_on_image
            self.graphicsView_image.mouseReleaseEvent = self.release_up_on_image
        elif event.button() == QtCore.Qt.RightButton:
            print("right button")

    def release_up_on_image(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.graphicsView_image.mouseMoveEvent = None
            self.graphicsView_image.mouseReleaseEvent = None

            end_pos = event.pos()
            self.set_rect(end_pos)
            self._draw_rect_on_image()

            roi = [self.rect[0]/self.view_width, self.rect[1]/self.view_height,
                   (self.rect[0]+self.rect[2])/self.view_width,
                   (self.rect[1]+self.rect[3])/self.view_height]
            self.norm_roi = roi
            self._update_result()

    def _update_xStart(self):
        raw_text = self.lineEdit_xStart.text()
        self.rect_xStart = int(raw_text)
        self._update_rect_size(0)

    def _update_yStart(self):
        raw_text = self.lineEdit_yStart.text()
        self.rect_yStart = int(raw_text)
        self._update_rect_size(1)

    def _update_xEnd(self):
        raw_text = self.lineEdit_xEnd.text()
        self.rect_xEnd = int(raw_text)
        self._update_rect_size(0)

    def _update_yEnd(self):
        raw_text = self.lineEdit_yEnd.text()
        self.rect_yEnd = int(raw_text)
        self._update_rect_size(1)

    def _update_gray_output(self):
        self._gray_output = self.checkBox_gray_output.isChecked()
        self._update_result()

    def _change_pedestal(self):
        temp = self.lineEdit_pedestal.text()
        if len(temp) == 0:
            self._pedestal = 0
        else:
            self._pedestal = int(temp)
        self._update_result()

    def _clear_log(self):
        self.textEdit_results.clear()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_M:
            self.show_files_mean()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    atImage_show = atImage_window()
    atImage_show.show()
    sys.exit(app.exec_())

