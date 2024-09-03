from PyQt6 import QtWidgets
from views.main_ui import Ui_Main  # 导入生成的UI类
from controllers.fin_obj_ui_controller import FinancialObjectiveController
from utilities.ui_utils import UiUtils  # Importing the UiUtils class


class MainUiController:
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.main_window)

        # 连接按钮点击事件到槽函数
        self.fin_obj_controller = FinancialObjectiveController()
        self.ui.pushButton.clicked.connect(self.open_financial_objective)
        self.ui.pushButton_2.clicked.connect(UiUtils.show_file_not_found_warning)

    def show_main_window(self):
        self.main_window.show()

    def open_financial_objective(self):
        print("MainUIController: open_financial_objective called")  # Debug print
        self.fin_obj_controller.show()
