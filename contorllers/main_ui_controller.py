from PyQt6 import QtWidgets
from views.main_ui import Ui_Main
import os

class MainUiController(QtWidgets.QMainWindowm, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.start_new)
        self.pushButton_2.clicked.connect(self.show_result)

    def start_new(self):
        pass

    def show_result(self):
        # Judge if result.txt exists
        if not os.path.exists("result.txt"):
            QtWidgets.QMessageBox.warning(self, "Error", "No result file")
            return
