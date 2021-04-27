# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2021/4/27
    File Name: FirstMainWin
    Description:
-------------------------------------------------
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        # 设置title
        self.setWindowTitle("第一个窗口")
        self.resize(400, 300)

        # 状态栏
        self.status = self.statusBar()
        self.status.showMessage("10秒钟后消失", 100000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon/1.jpeg"))

    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())