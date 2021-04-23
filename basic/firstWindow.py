# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2021/4/23
    File Name: firstWindow
    Description:
-------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication的实例
    app = QApplication(sys.argv)
    # 创建窗口
    w = QWidget()
    # 设置尺寸和title
    w.resize(500,400)
    w.setWindowTitle("My First Window")
    # 显示窗口
    w.show()

    # 进入程序的主循环 并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())