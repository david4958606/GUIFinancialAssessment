from PyQt6 import QtWidgets
from controllers.main_ui_controller import MainUiController  # 导入控制器

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    controller = MainUiController()  # 创建控制器实例
    controller.show_main_window()    # 显示主窗口

    app.exec()
