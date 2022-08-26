import os
import sys
import cv2
import numpy as np
from libs.Common import Common
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from UI.Pic2Vid import Ui_Pic2Vid


class Pic2Vid_Widget(QWidget,Ui_Pic2Vid):
    def __init__(self):
        super(Pic2Vid_Widget, self).__init__()
        styleFile = "./qrc/style.qss"
        style = Common.readQss(styleFile)
        self.setFixedSize(640, 480)
        #self.setStyleSheet(style)
        self.setupUi(self)
        self.framelist = list()  # 重置时需要初始化
        self.CloseButton.clicked.connect(self.close)
        self.PicDirButton.clicked.connect(self.selectPicDir)
        self.ResetButton.clicked.connect(self.WidgetReset)
        self.ConfirmButton.clicked.connect(self.CreateVideo)
        self.VideoDirButton.clicked.connect(self.selectVidDir)

    def selectPicDir(self):
        PicDir = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.PicDirPath.setText(PicDir)
        self.VideoDirPath.setText(PicDir)
        FileList = sorted(os.listdir(PicDir))
        for i, FileName in enumerate(FileList):
            if (FileName.split(".")[-1]) in ['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG']:
                PicName = PicDir + '/' + FileName
                self.PicList.addItem(PicName)
                self.framelist.append(PicName)

    def selectVidDir(self):
        VideoDir = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.VideoDirPath.setText(VideoDir)

    def WidgetReset(self):
        self.VideoType.setCurrentIndex(0)
        self.PicDirPath.clear()
        self.VideoDirPath.clear()
        self.VideoName.setText("Video")
        self.FPS.setText("30")
        self.PicList.clear()
        self.framelist.clear()
        self.progressBar.setValue(0)

    def CheckValue(self):
        # 检查输出文件夹是否存在
        if os.path.isdir(self.VideoDirPath.text()) is False:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Check Your VideoDirPath!')
            msg_box.exec_()
            return False
        if len(self.VideoName.text()) == 0:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Check Your VideoName!')
            msg_box.exec_()
            return False
        if int(self.FPS.text()) < 0 or int(self.FPS.text()) > 50:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Please Set 0<=FPS<=50!')
            msg_box.exec_()
            return False
        return True

    def CreateVideo(self):
        if self.CheckValue() is False:
            return
        video_type = "." + self.VideoType.currentText()
        output_video_path = self.VideoDirPath.text() + "/" + self.VideoName.text() + video_type

        test_load = cv2.imread(self.framelist[0])
        img_shape = np.shape(test_load)[:-1]
        img_shape = img_shape[1], img_shape[0]
        if self.VideoType.currentIndex() == 0:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
        elif self.VideoType.currentIndex() == 1:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        video_writer = cv2.VideoWriter(output_video_path, fourcc, int(self.FPS.text()), img_shape)

        list_sz = len(self.framelist)
        for i, FramePath in enumerate(self.framelist):
            progressValue = int((i+1) / list_sz * 100)
            self.progressBar.setValue(progressValue)
            frame = cv2.imread(FramePath)
            video_writer.write(frame)
        video_writer.release()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Pic2VidWidget = Pic2Vid_Widget()
    Pic2VidWidget.show()
    sys.exit(app.exec_())