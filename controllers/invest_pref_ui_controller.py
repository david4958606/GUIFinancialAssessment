from views.invest_pref_ui import InvestmentPreferencesUI
from PyQt6.QtWidgets import QApplication
from utilities.file_utils import FileUtils
import sys


class InvestmentPreferencesController:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.view = InvestmentPreferencesUI()
        self.view.save_clicked.connect(self.on_save)

    def show(self):
        print("InvestmentPreferencesController: show method called")  # Debug print
        self.view.show()
        self.view.raise_()  # Bring the window to the front
        self.view.activateWindow()  # Activate the window

    def on_save(self, result):
        question, answer = result
        print("Investment Preferences Result:")
        FileUtils.amend_result_file("Investment Preferences:")
        print(f"Question: {question}")
        FileUtils.amend_result_file(f"Question: {question}")
        print(f"Answer: {answer if answer else 'Not answered'}")
        FileUtils.amend_result_file(
            f"Answer: {answer if answer else 'Not answered'}")
        self.app_controller.show_main()
        self.view.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = InvestmentPreferencesController()
    controller.show()
    sys.exit(app.exec())
