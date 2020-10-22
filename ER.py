# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from os import getcwd
import numpy as np
import cv2
import time
from base64 import b64decode
from os import remove
from png import img as bgImg
# import imcore
from label_output import Emotion_7



class Ui_Window(object):
    def __init__(self, MainWindow):
        self.path = getcwd()
        self.timer_camera = QtCore.QTimer()  # 定时器

        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.slot_init()  # 槽函数设置

        # 设置界面动画
        gif = QMovie('./icon/scan.gif')
        self.label_face.setMovie(gif)
        gif.start()

        self.cap = cv2.VideoCapture()  # 屏幕画面对象
        self.CAM_NUM = 0  # 摄像头标号
        self.model_path = None  # 模型路径
        # self.__flag_work = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(500, 595)
        MainWindow.setMinimumSize(QtCore.QSize(500, 595))
        MainWindow.setMaximumSize(QtCore.QSize(500, 595))
        MainWindow.setToolTip("Expression Recognition System")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/change.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(./icon/background.PNG);}\n"
                                 "\n"
                                 "#QInputDialog{border-image: url(./icon/light.png);}\n"
                                 "\n"
                                 "QMenuBar{border-color:transparent;}\n"
                                 "QToolButton[objectName=pushButton_doIt]{\n"
                                 "border:5px;}\n"
                                 "\n"
                                 "QToolButton[objectName=pushButton_doIt]:hover {\n"
                                 "image:url(./icon/run_hover.png);}\n"
                                 "\n"
                                 "QToolButton[objectName=pushButton_doIt]:pressed {\n"
                                 "image:url(./icon/run_pressed.png);}\n"
                                 "\n"
                                 "QScrollBar:vertical{\n"
                                 "background:transparent;\n"
                                 "padding:2px;\n"
                                 "border-radius:8px;\n"
                                 "max-width:14px;}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical{\n"
                                 "background:#9acd32;\n"
                                 "min-height:50px;\n"
                                 "border-radius:8px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical:hover{\n"
                                 "background:#9eb764;}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical:pressed{\n"
                                 "background:#9eb764;\n"
                                 "}\n"
                                 "QScrollBar::add-page:vertical{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "                               \n"
                                 "QScrollBar::sub-page:vertical{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical{\n"
                                 "background:none;}\n"
                                 "                                 \n"
                                 "QScrollBar::sub-line:vertical{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "QScrollArea{\n"
                                 "border:0px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:horizontal{\n"
                                 "background:transparent;\n"
                                 "padding:0px;\n"
                                 "border-radius:6px;\n"
                                 "max-height:4px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal{\n"
                                 "background:#9acd32;\n"
                                 "min-width:50px;\n"
                                 "border-radius:6px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal:hover{\n"
                                 "background:#9eb764;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal:pressed{\n"
                                 "background:#9eb764;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-page:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-page:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "QScrollBar::add-line:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "QToolButton::hover{\n"
                                 "border:0px;\n"
                                 "} ")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # title
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(65, 40, 371, 30)) # 左右、上下、宽、*
        self.label_title.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_title.setObjectName("label_title")

        # Version
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(10, 90, 132, 30)) # 左右、上下、宽、高
        self.label_version.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_version.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_version.setObjectName("label_version")

        #scan_face_Recognizing emoticons
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(30, 130, 440, 300)) # 左右、上下、宽、高
        self.label_face.setMinimumSize(QtCore.QSize(440, 300))
        self.label_face.setMaximumSize(QtCore.QSize(440, 300))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(22)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("border-image: url(./icon/scan.gif);\n"
                                      "color: rgb(255, 125, 0);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")

        # display_selected_model
        self.textEdit_model = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_model.setGeometry(QtCore.QRect(70, 470, 395, 35))  # 左右、上下、宽、高
        self.textEdit_model.setMinimumSize(QtCore.QSize(395, 30))
        self.textEdit_model.setMaximumSize(QtCore.QSize(395, 40))
        self.textEdit_model.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_model.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(10)
        self.textEdit_model.setFont(font)
        self.textEdit_model.setStyleSheet("background-color: transparent;\n"
                                          "border-color: rgb(225, 255, 0);\n"
                                          "color: rgb(125, 125, 125);")  # 选择模型颜色
        self.textEdit_model.setReadOnly(True)
        self.textEdit_model.setObjectName("textEdit_model")

        # select_picture_button
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(10, 530, 50, 40))  # 左右、上下、宽、高
        self.toolButton_file.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        self.toolButton_file.setStyleSheet("background-color: transparent;")
        # self.toolButton_file.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon)
        self.toolButton_file.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file.setObjectName("toolButton_camera_2")

        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(12)

        #display_selected_picture
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(70, 530, 395, 35))  # 左右、上下、宽、高
        self.textEdit_pic.setMinimumSize(QtCore.QSize(395, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(395, 40))
        self.textEdit_pic.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(10)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
                                        "border-color: rgb(255, 255, 0);\n"
                                        "color: rgb(125, 125, 125);")  # 选择图片颜色
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")

        # select_model_button
        self.toolButton_model = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_model.setGeometry(QtCore.QRect(10, 465, 50, 40))  # 左右、上下、宽、高
        self.toolButton_model.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_model.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_model.setAutoFillBackground(False)
        self.toolButton_model.setStyleSheet("background-color: transparent;")
        # self.toolButton_model.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icon/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_model.setIcon(icon2)
        self.toolButton_model.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_model.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_model.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_model.setAutoRaise(False)
        self.toolButton_model.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_model.setObjectName("toolButton_model")

        # (None)
        self.label_outputResult = QtWidgets.QLabel(self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expression recognition system V1.0"))
        self.label_title.setText(_translate("MainWindow", "基于神经网络的表情检测识别系统"))
        self.label_version.setText(_translate("MainWindow", "Version：V1.0"))
        self.label_face.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textEdit_model.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:10pt; font-weight:500; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">Click on the icon to select model.</span></p></body></html>"))
        self.textEdit_pic.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:10pt; font-weight:500; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">Click on the icon to select picture.</span></p></body></html>"))

    def slot_init(self):  # 定义槽函数
        self.toolButton_model.clicked.connect(self.choose_model)
        self.toolButton_file.clicked.connect(self.choose_pic)

    def choose_pic(self):
        # 界面处理
        self.timer_camera.stop()
        self.cap.release()
        self.label_face.clear()

        # 使用文件选择对话框选择图片
        fileName_choose, filetype = QFileDialog.getOpenFileName(
            self.centralwidget, "select picture file",
            self.path,  # 起始路径
            "图片(*.jpg;*.jpeg;*.png)")  # 文件类型
        self.path = fileName_choose  # 保存路径
        if fileName_choose != '':
            self.textEdit_pic.setText(fileName_choose + ' file selected')
            self.label_face.setText('Recognizing emoticons...')
            QtWidgets.QApplication.processEvents()
            # 生成模型对象
            self.emotion_model = Emotion_7(self.model_path)
            # 读取背景图
            tmp = open('slice.png', 'wb')
            tmp.write(b64decode(bgImg))
            tmp.close()
            canvas = cv2.imread('slice.png')
            remove('slice.png')

            image = self.cv_imread(fileName_choose)  # 读取选择的图片
            # 计时并开始模型预测
            QtWidgets.QApplication.processEvents()
            # time_start = time.time()
            result = self.emotion_model.run(image, canvas, self.label_face, self.label_outputResult)
            # time_end = time.time()

        else:
            # 选择取消，恢复界面状态
            self.textEdit_pic.setText('文件未选中')
            gif = QMovie('./icon/scan.gif')
            # self.label_face.setMovie(gif)
            gif.start()

    def cv_imread(self, filePath):
        # 读取图片
        cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
        return cv_img

    def choose_model(self):
        # 选择训练好的模型文件
        self.timer_camera.stop()
        self.cap.release()
        self.label_face.clear()

        # 调用文件选择对话框
        fileName_choose, filetype = QFileDialog.getOpenFileName(self.centralwidget,
                                                                "select model file", getcwd(),  # 起始路径
                                                                "Model File (*.hdf5)")  # 文件类型
        # 显示提示信息
        if fileName_choose != '':
            self.model_path = fileName_choose
            self.textEdit_model.setText(fileName_choose + ' file selected')
        else:
            self.textEdit_model.setText('Use default model')

        # 恢复界面
        gif = QMovie('./icon/scan.gif')
        self.label_face.setMovie(gif)
        gif.start()
