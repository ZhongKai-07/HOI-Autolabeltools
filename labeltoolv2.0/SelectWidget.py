from PyQt5.QtWidgets import QWidget, QApplication
import sys
from Pic2VideoWidget import Pic2Vid_Widget
from UI.Startui import Ui_Start
from Vid2PicWidget import Vid2Pic_Widget
from libs.Common import Common
from mainwindow import Main_Window
from window import MyWindow


class SelectWidget(QWidget, Ui_Start):
    def __init__(self):
        super(SelectWidget, self).__init__()
        styleFile = "./qrc/style.qss"
        style = Common.readQss(styleFile)
        # self.setFixedSize(200, 300)
        # self.setStyleSheet(style)
        self.setupUi(self)
        self.Pic2VidButton.clicked.connect(self.pic2video)
        self.Vid2PicButton.clicked.connect(self.video2pic)
        self.BBoxLabelImgButton.clicked.connect(self.labeltool)

    def pic2video(self):
        self.Pic2VideoWidget = Pic2Vid_Widget()
        self.Pic2VideoWidget.show()

    def video2pic(self):
        self.Video2PicWidget = Vid2Pic_Widget()
        self.Video2PicWidget.show()

    def labeltool(self):
        self.MainWindow = Main_Window()
        self.MainWindow.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    selectWidget = SelectWidget()
    selectWidget.show()
    sys.exit(app.exec_())