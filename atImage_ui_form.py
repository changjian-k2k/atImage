# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atImage_ui_form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1119, 627)
        self.listWidget_fileList = QtWidgets.QListWidget(Form)
        self.listWidget_fileList.setGeometry(QtCore.QRect(9, 40, 331, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_fileList.sizePolicy().hasHeightForWidth())
        self.listWidget_fileList.setSizePolicy(sizePolicy)
        self.listWidget_fileList.setAcceptDrops(True)
        self.listWidget_fileList.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget_fileList.setObjectName("listWidget_fileList")
        self.textEdit_results = QtWidgets.QTextEdit(Form)
        self.textEdit_results.setGeometry(QtCore.QRect(9, 278, 451, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_results.sizePolicy().hasHeightForWidth())
        self.textEdit_results.setSizePolicy(sizePolicy)
        self.textEdit_results.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_results.setLineWrapColumnOrWidth(0)
        self.textEdit_results.setObjectName("textEdit_results")
        self.pushButton_getMean = QtWidgets.QPushButton(Form)
        self.pushButton_getMean.setGeometry(QtCore.QRect(350, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_getMean.setFont(font)
        self.pushButton_getMean.setObjectName("pushButton_getMean")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 411, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_folderPath = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_folderPath.sizePolicy().hasHeightForWidth())
        self.lineEdit_folderPath.setSizePolicy(sizePolicy)
        self.lineEdit_folderPath.setObjectName("lineEdit_folderPath")
        self.horizontalLayout.addWidget(self.lineEdit_folderPath)
        self.pushButton_folderPath = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_folderPath.sizePolicy().hasHeightForWidth())
        self.pushButton_folderPath.setSizePolicy(sizePolicy)
        self.pushButton_folderPath.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_folderPath.setObjectName("pushButton_folderPath")
        self.horizontalLayout.addWidget(self.pushButton_folderPath)
        self.graphicsView_image = QtWidgets.QGraphicsView(Form)
        self.graphicsView_image.setGeometry(QtCore.QRect(470, 140, 642, 482))
        self.graphicsView_image.setObjectName("graphicsView_image")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(640, 11, 201, 106))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setMidLineWidth(2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setMidLineWidth(2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setMidLineWidth(2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setMidLineWidth(2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_mean_R = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_mean_R.setFont(font)
        self.label_mean_R.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_mean_R.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_mean_R.setMidLineWidth(0)
        self.label_mean_R.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mean_R.setObjectName("label_mean_R")
        self.gridLayout.addWidget(self.label_mean_R, 1, 1, 1, 1)
        self.label_snr_R = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_snr_R.setFont(font)
        self.label_snr_R.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_snr_R.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_snr_R.setMidLineWidth(0)
        self.label_snr_R.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snr_R.setObjectName("label_snr_R")
        self.gridLayout.addWidget(self.label_snr_R, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setMidLineWidth(2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_mean_G = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_mean_G.setFont(font)
        self.label_mean_G.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_mean_G.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_mean_G.setMidLineWidth(0)
        self.label_mean_G.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mean_G.setObjectName("label_mean_G")
        self.gridLayout.addWidget(self.label_mean_G, 2, 1, 1, 1)
        self.label_snr_G = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_snr_G.setFont(font)
        self.label_snr_G.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_snr_G.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_snr_G.setMidLineWidth(0)
        self.label_snr_G.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snr_G.setObjectName("label_snr_G")
        self.gridLayout.addWidget(self.label_snr_G, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setMidLineWidth(2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_mean_B = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_mean_B.setFont(font)
        self.label_mean_B.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_mean_B.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_mean_B.setMidLineWidth(0)
        self.label_mean_B.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mean_B.setObjectName("label_mean_B")
        self.gridLayout.addWidget(self.label_mean_B, 3, 1, 1, 1)
        self.label_snr_B = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_snr_B.setFont(font)
        self.label_snr_B.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_snr_B.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_snr_B.setLineWidth(1)
        self.label_snr_B.setMidLineWidth(0)
        self.label_snr_B.setAlignment(QtCore.Qt.AlignCenter)
        self.label_snr_B.setObjectName("label_snr_B")
        self.gridLayout.addWidget(self.label_snr_B, 3, 2, 1, 1)
        self.lineEdit_rawWidth = QtWidgets.QLineEdit(Form)
        self.lineEdit_rawWidth.setGeometry(QtCore.QRect(467, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_rawWidth.setFont(font)
        self.lineEdit_rawWidth.setObjectName("lineEdit_rawWidth")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(530, 105, 20, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_rawHeight = QtWidgets.QLineEdit(Form)
        self.lineEdit_rawHeight.setGeometry(QtCore.QRect(550, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_rawHeight.setFont(font)
        self.lineEdit_rawHeight.setObjectName("lineEdit_rawHeight")
        self.comboBox_data_bit = QtWidgets.QComboBox(Form)
        self.comboBox_data_bit.setGeometry(QtCore.QRect(540, 70, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_data_bit.setFont(font)
        self.comboBox_data_bit.setEditable(False)
        self.comboBox_data_bit.setObjectName("comboBox_data_bit")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.comboBox_data_bit.addItem("")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(470, 70, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(890, 20, 151, 98))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.lineEdit_xStart = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_xStart.setFont(font)
        self.lineEdit_xStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_xStart.setObjectName("lineEdit_xStart")
        self.gridLayout_2.addWidget(self.lineEdit_xStart, 1, 1, 1, 1)
        self.lineEdit_yStart = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_yStart.setFont(font)
        self.lineEdit_yStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_yStart.setObjectName("lineEdit_yStart")
        self.gridLayout_2.addWidget(self.lineEdit_yStart, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_xEnd = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_xEnd.setFont(font)
        self.lineEdit_xEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_xEnd.setObjectName("lineEdit_xEnd")
        self.gridLayout_2.addWidget(self.lineEdit_xEnd, 2, 1, 1, 1)
        self.lineEdit_yEnd = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_yEnd.setFont(font)
        self.lineEdit_yEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_yEnd.setObjectName("lineEdit_yEnd")
        self.gridLayout_2.addWidget(self.lineEdit_yEnd, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_rect_width = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_rect_width.setFont(font)
        self.label_rect_width.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_rect_width.setText("")
        self.label_rect_width.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rect_width.setObjectName("label_rect_width")
        self.gridLayout_2.addWidget(self.label_rect_width, 3, 1, 1, 1)
        self.label_rect_height = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_rect_height.setFont(font)
        self.label_rect_height.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_rect_height.setText("")
        self.label_rect_height.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rect_height.setObjectName("label_rect_height")
        self.gridLayout_2.addWidget(self.label_rect_height, 3, 2, 1, 1)
        self.checkBox_gray_output = QtWidgets.QCheckBox(Form)
        self.checkBox_gray_output.setGeometry(QtCore.QRect(470, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_gray_output.setFont(font)
        self.checkBox_gray_output.setChecked(True)
        self.checkBox_gray_output.setObjectName("checkBox_gray_output")
        self.label_OB = QtWidgets.QLabel(Form)
        self.label_OB.setGeometry(QtCore.QRect(470, 40, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_OB.setFont(font)
        self.label_OB.setObjectName("label_OB")
        self.lineEdit_pedestal = QtWidgets.QLineEdit(Form)
        self.lineEdit_pedestal.setGeometry(QtCore.QRect(500, 40, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_pedestal.setFont(font)
        self.lineEdit_pedestal.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pedestal.setObjectName("lineEdit_pedestal")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(540, 40, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.pushButton_clear_log = QtWidgets.QPushButton(Form)
        self.pushButton_clear_log.setGeometry(QtCore.QRect(350, 242, 75, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        self.pushButton_clear_log.setFont(font)
        self.pushButton_clear_log.setObjectName("pushButton_clear_log")

        self.retranslateUi(Form)
        self.comboBox_data_bit.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "atImage"))
        self.pushButton_getMean.setText(_translate("Form", "平均值"))
        self.label.setText(_translate("Form", "文件夹路径："))
        self.pushButton_folderPath.setText(_translate("Form", "..."))
        self.label_5.setText(_translate("Form", "通道"))
        self.label_6.setText(_translate("Form", "亮度值"))
        self.label_7.setText(_translate("Form", "信噪比"))
        self.label_2.setText(_translate("Form", "R"))
        self.label_mean_R.setText(_translate("Form", "0.00"))
        self.label_snr_R.setText(_translate("Form", "0.0"))
        self.label_3.setText(_translate("Form", "G"))
        self.label_mean_G.setText(_translate("Form", "0.00"))
        self.label_snr_G.setText(_translate("Form", "0.0"))
        self.label_4.setText(_translate("Form", "B"))
        self.label_mean_B.setText(_translate("Form", "0.00"))
        self.label_snr_B.setText(_translate("Form", "0.0"))
        self.label_8.setText(_translate("Form", "x"))
        self.comboBox_data_bit.setCurrentText(_translate("Form", "8 bit"))
        self.comboBox_data_bit.setItemText(0, _translate("Form", "8 bit"))
        self.comboBox_data_bit.setItemText(1, _translate("Form", "9 bit"))
        self.comboBox_data_bit.setItemText(2, _translate("Form", "10 bit"))
        self.comboBox_data_bit.setItemText(3, _translate("Form", "11 bit"))
        self.comboBox_data_bit.setItemText(4, _translate("Form", "12 bit"))
        self.comboBox_data_bit.setItemText(5, _translate("Form", "13 bit"))
        self.comboBox_data_bit.setItemText(6, _translate("Form", "14 bit"))
        self.comboBox_data_bit.setItemText(7, _translate("Form", "15 bit"))
        self.comboBox_data_bit.setItemText(8, _translate("Form", "16 bit"))
        self.label_9.setText(_translate("Form", "数据位数"))
        self.label_13.setText(_translate("Form", "x"))
        self.label_14.setText(_translate("Form", "y"))
        self.label_12.setText(_translate("Form", "开始点"))
        self.label_11.setText(_translate("Form", "结束点"))
        self.label_10.setText(_translate("Form", "尺寸"))
        self.checkBox_gray_output.setText(_translate("Form", "灰度输出"))
        self.label_OB.setText(_translate("Form", "OB:"))
        self.lineEdit_pedestal.setText(_translate("Form", "0"))
        self.label_16.setText(_translate("Form", "@ 8 bit"))
        self.pushButton_clear_log.setText(_translate("Form", "清空LOG"))
