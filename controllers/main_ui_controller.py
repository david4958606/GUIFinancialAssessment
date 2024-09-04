from PyQt6 import QtWidgets
from views.main_ui import Ui_Main
from controllers.fin_obj_ui_controller import FinancialObjectiveController
from utilities.ui_utils import UiUtils  # Importing the UiUtils class
from utilities.file_utils import FileUtils  # Importing the FileUtils class


class MainUiController:
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.main_window)

        # Link buttons to their respective functions
        self.fin_obj_controller = FinancialObjectiveController()
        self.ui.pushButton.clicked.connect(self.open_financial_objective)
        self.ui.pushButton_2.clicked.connect(UiUtils.show_file_not_found_warning)

    def show_main_window(self):
        self.update_car_cka()
        self.main_window.show()

    def open_financial_objective(self):
        print("MainUIController: open_financial_objective called")  # Debug print
        self.main_window.hide()
        self.fin_obj_controller.show()
        FileUtils.amend_result_file("Your Financial Objective: ")

    def update_car_cka(self):
        if FileUtils.judge_car():
            UiUtils.update_label_text(self.ui.l_CAR_status, "Passed")
            UiUtils.update_label_color(self.ui.l_CAR_status, "green")
        else:
            UiUtils.update_label_text(self.ui.l_CAR_status, "Failed")
            UiUtils.update_label_color(self.ui.l_CAR_status, "red")
        if FileUtils.judge_cka():
            UiUtils.update_label_text(self.ui.l_CKA_status, "Passed")
            UiUtils.update_label_color(self.ui.l_CKA_status, "green")
        else:
            UiUtils.update_label_text(self.ui.l_CKA_status, "Failed")
            UiUtils.update_label_color(self.ui.l_CKA_status, "red")
