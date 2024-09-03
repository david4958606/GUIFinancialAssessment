from views.fin_obj_ui import FinancialObjectiveUI
from PyQt6.QtWidgets import QApplication
import sys

class FinancialObjectiveController:
    def __init__(self):
        self.view = FinancialObjectiveUI()
        self.view.save_clicked.connect(self.on_save)

    def show(self):
        self.view.show()

    def on_save(self, selected_option):
        if selected_option:
            print(f"Selected option: {selected_option}")
        else:
            print("No option selected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = FinancialObjectiveController()
    controller.show()
    sys.exit(app.exec())