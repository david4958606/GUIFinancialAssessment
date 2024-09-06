from PyQt6 import QtWidgets
from views.main_ui import MainUi
from utilities.ui_utils import UiUtils
from utilities.file_utils import FileUtils

class MainUiController:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.main_window = QtWidgets.QMainWindow()
        self.ui = MainUi()
        self.ui.setup_ui(self.main_window)

        # Link buttons to their respective functions
        self.ui.pushButton.clicked.connect(self.open_financial_objective)
        self.ui.pushButton_2.clicked.connect(UiUtils.show_file_not_found_warning)

    def show(self):
        self.update_car_cka()
        self.update_fin_obj_status()
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()

    def open_financial_objective(self):
        print("MainUIController: open_financial_objective called")  # Debug print
        self.main_window.hide()
        self.app_controller.show_fin_obj()
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

    def update_fin_obj_status(self):
        status = FileUtils.get_financial_objective()
        UiUtils.update_label_text(self.ui.l_obj_status, status)