# main.py
# Author: Nguyen Huu Khanh (Khanh ECB)
# Description: Đây là một ứng dụng nhỏ dùng để quản lý thông tin mua bán của tiệm bạc
# Date: 7-2025
from gui.class_main_window import GuiRoot
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GuiRoot()
    win.show()
    sys.exit(app.exec_())