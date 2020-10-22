# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 449)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 390, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 481, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(460, 60, 71, 21))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(380, 131, 181, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit_model = QtWidgets.QTextEdit(Dialog)
        self.textEdit_model.setGeometry(QtCore.QRect(110, 350, 441, 31))
        self.textEdit_model.setDocumentTitle("")
        # self.textEdit_model.setMarkdown("")
        self.textEdit_model.setObjectName("textEdit_model")
        self.textEdit_picture = QtWidgets.QTextEdit(Dialog)
        self.textEdit_picture.setGeometry(QtCore.QRect(110, 390, 441, 31))
        # self.textEdit_picture.setMarkdown("")
        self.textEdit_picture.setObjectName("textEdit_picture")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 80, 361, 251))
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.model_button)
        self.pushButton_2.clicked.connect(Dialog.picture_button)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "基于神经网络的检测识别系统"))
        self.pushButton.setText(_translate("Dialog", "模型选择"))
        self.pushButton_2.setText(_translate("Dialog", "图片选择"))
        self.label.setText(_translate("Dialog", "基于神经网络的检测识别系统"))
        self.label_2.setText(_translate("Dialog", "Version:V1.0"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">提示</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 点击模型选择按钮，进行模型选择（无操作应用默认模型）。</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 点击图片选择按钮，进行图片选择。</span></p></body></html>"))
        self.textEdit_model.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_picture.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

    #实现pushButton_click()函数，textEdit_model是我们放上去的文本框的id
    def model_button(self):
        self.textEdit_model.clear()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self.centralwidget,
                                                                "select model file", getcwd(),  # 起始路径
                                                                "Model File (*.hdf5)")  # 文件类型
        # self.textEdit_model.setText("你点击了按钮")
        if fileName_choose != '':
            self.model_path = fileName_choose
            self.textEdit_model.setText(fileName_choose + ' file selected')
        else:
            self.textEdit_model.setText('Use default model')




    def picture_button(self):
        # self.textEdit_picture.setText("你点击了按钮")
        self.textEdit_model.clear()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self.centralwidget,
                                                                "select picture file", getcwd(),  # 起始路径
                                                                "Picture File (*.jpg;*.jpeg;*.png)")  # 文件类型
        # self.textEdit_model.setText("你点击了按钮")
        if fileName_choose != '':
            self.model_path = fileName_choose
            self.textEdit_picture.setText(fileName_choose + ' file selected')
            self.textEdit_model.setText('model file selected')
            self.textEdit_3.setText('Recognizing emoticons...')
            QtWidgets.QApplication.processEvents()
        else:
            self.textEdit_picture.setText('Please select one picture!')
