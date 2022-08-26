# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labelimg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LabelImg(object):
    def setupUi(self, LabelImg):
        LabelImg.setObjectName("LabelImg")
        LabelImg.resize(1600, 950)
        self.centralwidget = QtWidgets.QWidget(LabelImg)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 191, 901))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -79, 190, 955))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.OpenButton = QtWidgets.QPushButton(self.groupBox_2)
        self.OpenButton.setMinimumSize(QtCore.QSize(0, 50))
        self.OpenButton.setMaximumSize(QtCore.QSize(16777215, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/.designer/resource/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenButton.setIcon(icon)
        self.OpenButton.setObjectName("OpenButton")
        self.verticalLayout_4.addWidget(self.OpenButton)
        self.OpenDirButton = QtWidgets.QPushButton(self.groupBox_2)
        self.OpenDirButton.setMinimumSize(QtCore.QSize(0, 50))
        self.OpenDirButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.OpenDirButton.setObjectName("OpenDirButton")
        self.verticalLayout_4.addWidget(self.OpenDirButton)
        self.SaveDirButton = QtWidgets.QPushButton(self.groupBox_2)
        self.SaveDirButton.setMinimumSize(QtCore.QSize(0, 50))
        self.SaveDirButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SaveDirButton.setObjectName("SaveDirButton")
        self.verticalLayout_4.addWidget(self.SaveDirButton)
        self.ResetButton = QtWidgets.QPushButton(self.groupBox_2)
        self.ResetButton.setMinimumSize(QtCore.QSize(0, 50))
        self.ResetButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ResetButton.setObjectName("ResetButton")
        self.verticalLayout_4.addWidget(self.ResetButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PrevButton = QtWidgets.QPushButton(self.groupBox)
        self.PrevButton.setMinimumSize(QtCore.QSize(0, 50))
        self.PrevButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.PrevButton.setObjectName("PrevButton")
        self.verticalLayout_2.addWidget(self.PrevButton)
        self.NextButton = QtWidgets.QPushButton(self.groupBox)
        self.NextButton.setMinimumSize(QtCore.QSize(0, 50))
        self.NextButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout_2.addWidget(self.NextButton)
        self.CreateBBoxButton = QtWidgets.QPushButton(self.groupBox)
        self.CreateBBoxButton.setMinimumSize(QtCore.QSize(0, 50))
        self.CreateBBoxButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.CreateBBoxButton.setObjectName("CreateBBoxButton")
        self.verticalLayout_2.addWidget(self.CreateBBoxButton)
        self.DeleteBBoxButton = QtWidgets.QPushButton(self.groupBox)
        self.DeleteBBoxButton.setMinimumSize(QtCore.QSize(0, 50))
        self.DeleteBBoxButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.DeleteBBoxButton.setObjectName("DeleteBBoxButton")
        self.verticalLayout_2.addWidget(self.DeleteBBoxButton)
        self.SaveButton = QtWidgets.QPushButton(self.groupBox)
        self.SaveButton.setMinimumSize(QtCore.QSize(0, 50))
        self.SaveButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SaveButton.setObjectName("SaveButton")
        self.verticalLayout_2.addWidget(self.SaveButton)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.LabelTypeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.LabelTypeComboBox.setObjectName("LabelTypeComboBox")
        self.LabelTypeComboBox.addItem("")
        self.LabelTypeComboBox.addItem("")
        self.verticalLayout_2.addWidget(self.LabelTypeComboBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AutoLabelingButton = QtWidgets.QPushButton(self.groupBox_6)
        self.AutoLabelingButton.setMinimumSize(QtCore.QSize(0, 50))
        self.AutoLabelingButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AutoLabelingButton.setObjectName("AutoLabelingButton")
        self.verticalLayout_6.addWidget(self.AutoLabelingButton)
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.ModelComboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.ModelComboBox.setObjectName("ModelComboBox")
        self.ModelComboBox.addItem("")
        self.ModelComboBox.addItem("")
        self.ModelComboBox.addItem("")
        self.verticalLayout_6.addWidget(self.ModelComboBox)
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.LabelNumber = QtWidgets.QLineEdit(self.groupBox_6)
        self.LabelNumber.setObjectName("LabelNumber")
        self.verticalLayout_6.addWidget(self.LabelNumber)
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.ClassComboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.ClassComboBox.setObjectName("ClassComboBox")
        self.ClassComboBox.addItem("")
        self.ClassComboBox.addItem("")
        self.ClassComboBox.addItem("")
        self.ClassComboBox.addItem("")
        self.ClassComboBox.setItemText(3, "")
        self.verticalLayout_6.addWidget(self.ClassComboBox)
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 21))
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(200, 0, 1061, 901))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(10, 60, 1025, 769))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 311, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setStyleSheet("")
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.SaveDir = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.SaveDir.setStyleSheet("")
        self.SaveDir.setObjectName("SaveDir")
        self.horizontalLayout_3.addWidget(self.SaveDir)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(330, 10, 371, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_7.setMinimumSize(QtCore.QSize(125, 0))
        self.label_7.setMaximumSize(QtCore.QSize(125, 16777215))
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.SaveLabelPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.SaveLabelPath.setEnabled(False)
        self.SaveLabelPath.setObjectName("SaveLabelPath")
        self.horizontalLayout_4.addWidget(self.SaveLabelPath)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(710, 10, 321, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setMinimumSize(QtCore.QSize(15, 0))
        self.label_8.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.mouseX = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.mouseX.setObjectName("mouseX")
        self.horizontalLayout_5.addWidget(self.mouseX)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_10.setMinimumSize(QtCore.QSize(15, 0))
        self.label_10.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.mouseY = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.mouseY.setObjectName("mouseY")
        self.horizontalLayout_5.addWidget(self.mouseY)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 840, 1021, 51))
        self.label_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_9.setObjectName("label_9")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(1260, 0, 331, 901))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 331, 411))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 311, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.LabelComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.LabelComboBox.setObjectName("LabelComboBox")
        self.horizontalLayout.addWidget(self.LabelComboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 311, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NameListButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.NameListButton.setObjectName("NameListButton")
        self.horizontalLayout_2.addWidget(self.NameListButton)
        self.NameListPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.NameListPath.setObjectName("NameListPath")
        self.horizontalLayout_2.addWidget(self.NameListPath)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 311, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.ListPreviewWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.ListPreviewWidget.setObjectName("ListPreviewWidget")
        self.verticalLayout_7.addWidget(self.ListPreviewWidget)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 420, 331, 481))
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 20, 311, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_11.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_12.setMinimumSize(QtCore.QSize(50, 0))
        self.label_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_12.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 60, 311, 421))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ImageListWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_7)
        self.ImageListWidget.setObjectName("ImageListWidget")
        self.horizontalLayout_7.addWidget(self.ImageListWidget)
        self.ImageStateListWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_7)
        self.ImageStateListWidget.setEnabled(False)
        self.ImageStateListWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.ImageStateListWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ImageStateListWidget.setObjectName("ImageStateListWidget")
        self.horizontalLayout_7.addWidget(self.ImageStateListWidget)
        LabelImg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LabelImg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        LabelImg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LabelImg)
        self.statusbar.setObjectName("statusbar")
        LabelImg.setStatusBar(self.statusbar)

        self.retranslateUi(LabelImg)
        QtCore.QMetaObject.connectSlotsByName(LabelImg)

    def retranslateUi(self, LabelImg):
        _translate = QtCore.QCoreApplication.translate
        LabelImg.setWindowTitle(_translate("LabelImg", "MainWindow"))
        self.groupBox_2.setTitle(_translate("LabelImg", "Select Image"))
        self.OpenButton.setText(_translate("LabelImg", "Open"))
        self.OpenDirButton.setText(_translate("LabelImg", "Open Dir"))
        self.SaveDirButton.setText(_translate("LabelImg", "Change Save Dir"))
        self.ResetButton.setText(_translate("LabelImg", "Reset"))
        self.groupBox.setTitle(_translate("LabelImg", "Create BBox"))
        self.PrevButton.setText(_translate("LabelImg", "Prev Image"))
        self.NextButton.setText(_translate("LabelImg", "Next Image"))
        self.CreateBBoxButton.setText(_translate("LabelImg", "Create RectBox"))
        self.DeleteBBoxButton.setText(_translate("LabelImg", "Delete RectBox"))
        self.SaveButton.setText(_translate("LabelImg", "Save"))
        self.label_6.setText(_translate("LabelImg", "Select Label Type:"))
        self.LabelTypeComboBox.setItemText(0, _translate("LabelImg", "YOLO"))
        self.LabelTypeComboBox.setItemText(1, _translate("LabelImg", "Pascal VOC"))
        self.groupBox_6.setTitle(_translate("LabelImg", "Auto  Setting"))
        self.AutoLabelingButton.setText(_translate("LabelImg", "Auto Labeling"))
        self.label_2.setText(_translate("LabelImg", "Select model:"))
        self.ModelComboBox.setItemText(0, _translate("LabelImg", "--select--"))
        self.ModelComboBox.setItemText(1, _translate("LabelImg", "Mask-RCNN"))
        self.ModelComboBox.setItemText(2, _translate("LabelImg", "YOLOV7"))
        self.label.setText(_translate("LabelImg", "Label Number:"))
        self.label_13.setText(_translate("LabelImg", "Select Class"))
        self.ClassComboBox.setItemText(0, _translate("LabelImg", "--select--"))
        self.ClassComboBox.setItemText(1, _translate("LabelImg", "car"))
        self.ClassComboBox.setItemText(2, _translate("LabelImg", "person"))
        self.label_14.setText(_translate("LabelImg", "Frame Filter"))
        self.comboBox.setItemText(0, _translate("LabelImg", "select"))
        self.comboBox.setItemText(1, _translate("LabelImg", "Uniform Sample"))
        self.comboBox.setItemText(2, _translate("LabelImg", "Motion Detect"))
        self.label_5.setText(_translate("LabelImg", "Save Dir:"))
        self.label_7.setText(_translate("LabelImg", "Save Label Path:"))
        self.label_8.setText(_translate("LabelImg", "x:"))
        self.label_10.setText(_translate("LabelImg", "y:"))
        self.label_9.setText(_translate("LabelImg", "Shortcut Description:  \n"
"W -- Create RectBox   D -- Next Image     A -- Prev Image   S -- Save Label   Esc -- Cancle RectBox    Del(After Select Image Path) --  Delete Saved Label"))
        self.groupBox_4.setTitle(_translate("LabelImg", "Box Label"))
        self.label_3.setText(_translate("LabelImg", "Class:"))
        self.NameListButton.setText(_translate("LabelImg", "NameList:"))
        self.label_4.setText(_translate("LabelImg", "Label View"))
        self.groupBox_5.setTitle(_translate("LabelImg", "Image List"))
        self.label_11.setText(_translate("LabelImg", "ImagePath"))
        self.label_12.setText(_translate("LabelImg", "State"))