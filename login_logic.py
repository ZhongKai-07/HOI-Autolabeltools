import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QMessageBox
from login import *


class MyLogin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.end_event)

        # 登陆函数
    def end_event(self):
        if self.lineEdit.text() == "":
            QMessageBox.about(self, '登录', '请输入姓名')
        elif self.lineEdit_2.text() == "":
            QMessageBox.about(self, '登录', '请输入密码')
        else:
            QMessageBox.about(self, '登录', self.lineEdit.text()+'欢迎登陆')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyLogin()
    myWin.show()
    
    sys.exit(app.exec_())