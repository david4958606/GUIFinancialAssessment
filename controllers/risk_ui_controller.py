from views.risk_ui import RiskProfilingUI
from utilities.file_utils import FileUtils
from PyQt6.QtWidgets import QApplication
import sys

class RiskProfilingController:
    def __init__(self):
        self.view = RiskProfilingUI()
        self.view.save_clicked.connect(self.on_save)

    def show(self):
        print("RiskProfilingController: show method called")  # Debug print
        self.view.show()
        self.view.raise_()  # Bring the window to the front
        self.view.activateWindow()  # Activate the window

    def on_save(self, results):
        print("Risk Profiling Results:")
        FileUtils.amend_result_file(("Risk Profiling Results:"))
        for question, answer in results:
            print(f"Question: {question}")
            FileUtils.amend_result_file((f"Question: {question}"))
            print(f"Answer: {answer if answer else 'Not answered'}")
            FileUtils.amend_result_file((f"Answer: {answer if answer else 'Not answered'}"))
            print()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = RiskProfilingController()
    controller.show()
    sys.exit(app.exec())