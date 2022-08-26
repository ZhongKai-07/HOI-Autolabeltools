import os
import sys
import cv2
from libs.Common import Common
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from UI.Vid2Pic import Ui_Vid2Pic


class Vid2Pic_Widget(QWidget, Ui_Vid2Pic):
    def __init__(self):
        super(Vid2Pic_Widget, self).__init__()
        styleFile = "./qrc/style.qss"
        style = Common.readQss(styleFile)
        self.setFixedSize(605, 250)
        # self.setStyleSheet(style)
        self.setupUi(self)
        self.framelist = list()  # 重置时需要初始化, 用于最后写入一个txt文件

        self.VideoButton.clicked.connect(self.selectVideo)
        self.PicSaveButton.clicked.connect(self.selectPicDir)
        self.ConfirmButton.clicked.connect(self.CreateFrame)
        self.ResetButton.clicked.connect(self.ParamReset)
        self.CloseButton.clicked.connect(self.close)

    def selectVideo(self):
        VideoPath = QFileDialog.getOpenFileName(self, "selectVideo", "./",
                                                "Video Files(*.mp4 *.avi *.MPEG *.h264);;MP4 Files(*.mp4);;AVI Files(*.avi);;MPEG Files(*.MPEG);;H264 Files(*.h264)")
        self.VideoPath.setText(list(VideoPath)[0])
        NewPicSaveDir = list(VideoPath)[0].split(".")[0]
        # if os.path.isdir(NewPicSaveDir) is False:
        #     os.mkdir(NewPicSaveDir)
        self.PicSaveDir.setText(NewPicSaveDir)

        cap = cv2.VideoCapture(list(VideoPath)[0])
        if cap.isOpened():
            ret, frame = cap.read()
            shape = frame.shape
            self.ImgHeight.setText(str(shape[0]))
            self.ImgWidth.setText(str(shape[1]))
        cap.release()

    def selectPicDir(self):
        PicSaveDir = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.PicSaveDir.setText(PicSaveDir)

    def ParamReset(self):
        self.VideoPath.clear()
        self.PicSaveDir.clear()
        self.DuraNum.setText("1")
        self.ImgWidth.clear()
        self.ImgHeight.clear()
        self.progressBar.setValue(0)
        self.framelist = list()

    def CheckValue(self):
        if os.path.exists(self.VideoPath.text()) is False:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Check Your VideoPath!')
            msg_box.exec_()
            return False
        if os.path.isdir(self.PicSaveDir.text()) is False:
            reply = QMessageBox.information(self, 'Confirm',
                                  'This Dir does not exist! Do you need to generate?',
                                  QMessageBox.Yes | QMessageBox.No)
            if reply:
                os.mkdir(self.PicSaveDir.text())
            else:
                return False
        if int(self.DuraNum.text()) <= 0:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Check the FPS!')
            msg_box.exec_()
            return False
        if int(self.ImgHeight.text()) <= 0 or int(self.ImgHeight.text()) <= 0:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Check the Shape of the frame!')
            msg_box.exec_()
            return False
        return True

    def CreateFrame(self):
        if self.CheckValue() is False:
            return

        cap = cv2.VideoCapture(self.VideoPath.text())
        if cap.isOpened():
            frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.ImgHeight.text()))
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.ImgWidth.text()))
            frame_num = 0  # 用于生成图片名称
            dura = int(self.DuraNum.text())
            for i in range(int(frame_count)):
                ret, frame = cap.read()
                self.progressBar.setValue(int((i + 1) / frame_count * 100))
                print()
                if (i + 1) % dura == 0:
                    frame_num += 1
                    SaveImgName = self.PicSaveDir.text() + "/" + str(frame_num).zfill(7) + ".jpg"
                    cv2.imwrite(SaveImgName, frame)

                    self.framelist.append(SaveImgName)

            cap.release()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Video Not Open!!!')
            msg_box.exec_()
            return

        # 生成list.txt
        ListPath = self.PicSaveDir.text() + "/list.txt"
        file = open(ListPath, "w")
        for i, PicName in enumerate(self.framelist):
            file.write(PicName + "\n")
        file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Vid2PicWidget = Vid2Pic_Widget()
    Vid2PicWidget.show()
    sys.exit(app.exec_())
