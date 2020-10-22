# -*- coding: utf-8 -*-
# Time    : 2020/5/26 19:45
# Author  : CS
# @Software: PyCharm
# @version : 1.0 2020/5/26

import warnings
import os
# 忽略警告
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings(action='ignore')
from ER import Ui_Window
from sys import argv, exit
from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    app = QApplication(argv)

    window = QMainWindow()
    ui = Ui_Window(window)

    window.show()
    exit(app.exec_())
