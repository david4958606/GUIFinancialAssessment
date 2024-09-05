from views.fin_obj_ui import FinancialObjectiveUI
from PyQt6.QtWidgets import QApplication
import sys
import utilities.ui_utils as ui_utils
import utilities.file_utils as file_utils
from controllers.risk_ui_controller import RiskProfilingController


class FinancialObjectiveController:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.view = FinancialObjectiveUI()
        self.view.save_clicked.connect(self.on_save)

    def show(self):
        self.view.show()

    def on_save(self, selected_option):
        if selected_option:
            # ui_utils.UiUtils.show_warning("Selected option: " + selected_option)
            file_utils.FileUtils.amend_result_file(selected_option)
        else:
            ui_utils.UiUtils.show_warning("Please select an option")
        # open next window
        self.open_risk_profiling()
        self.view.close()

    def open_risk_profiling(self):
        print("FinancialObjectiveController: open_risk_profiling called")
        self.app_controller.show_risk()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = FinancialObjectiveController()
    controller.show()
    sys.exit(app.exec())
