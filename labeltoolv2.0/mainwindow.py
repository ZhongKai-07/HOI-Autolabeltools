from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from UI.MainWindow import Ui_MainWindow
from UI.labelimg import Ui_LabelImg
from libs.Common import Common


class Main_Window(QMainWindow, Ui_LabelImg):
    def __init__(self):
        super(Main_Window, self).__init__()
        styleFile = "./qrc/style.qss"
        style = Common.readQss(styleFile)
        # self.setStyleSheet(style)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = Main_Window()
    mainWidget.show()
    sys.exit(app.exec_())