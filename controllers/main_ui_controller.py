import os
from PyQt6 import QtWidgets
from views.main_ui import Ui_Main  # 导入生成的UI类

class MainUiController:
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.main_window)

        # 连接按钮点击事件到槽函数
        self.ui.pushButton_2.clicked.connect(self.check_result_file)

    def show_main_window(self):
        self.main_window.show()

    def check_result_file(self):
        # 检查根目录下是否存在 "result.txt" 文件
        if not os.path.exists("result.txt"):
            self.show_warning("No Result Find")

    def show_warning(self, message):
        # 弹出警告框
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()
