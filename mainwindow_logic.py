import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import detect_config
from mainwindow import *
from detect_config import *
import cv2 as cv
import numpy as np
from mrcnn import utils
from mrcnn.config import Config


# load the pretrained weights file
coco_model_path = "F:\\HOI\\labeltool\\models\\mask_rcnn_coco.h5"
if not os.path.exists(coco_model_path):
    utils.download_trained_weights(coco_model_path)
    print("download!\\*********************")

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Rcnn目标检测v1.0")
        self.pushButton.clicked.connect(self.show_image)
        self.pushButton_2.clicked.connect(self.detect_image)

    def show_image(self):
        '''
        从本地读取图片
        '''
        global imgName

        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", ""
                                                       , "*.jpg;;*.png, *.PNG;;All File(*)")
        if imgName:
            self.captured = cv.imread(str(imgName))
            # Opencv图像以BGR通道存储，显示时需要从BGR2RGB
            self.captured = cv.cvtColor(self.captured, cv.COLOR_BGR2RGB)

            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(QImg).scaled(
                 self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        fname = imgName
        print(fname)
        self.textBrowser.setPlainText("成功打开图片")
        # jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        # self.label.setPixmap(jpg)

    def detect_image(self):
        '''
        检测图片
        :return:
        '''
        global  imgName
        # if not hasattr(self, "captured"):
        #     print("没有输入图像")
        #     self.textBrowser.setPlainText("没有输入图像")
        #     return
        print("开始")
        print(imgName.split("/")[-1])
        result = detect_config.detect(imgName)
        self.textBrowser.append("进行检测")
        print(result)
        self.captured = cv.imread(str(result))
        self.captured = cv.cvtColor(self.captured, cv.COLOR_BGR2RGB)

        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.label_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))



        self.textBrowser.append("检测完成")
























if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = MyWindow()
    my.show()
    
    sys.exit(app.exec_())