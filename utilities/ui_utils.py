import os
from PyQt6 import QtWidgets
import utilities.file_utils as utilities


class UiUtils:
    @staticmethod
    def show_warning(message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

    @staticmethod
    def show_file_not_found_warning():
        if not utilities.FileUtils.check_result_file():
            UiUtils.show_warning("Result not found")

    @staticmethod
    def update_label_text(label, text):
        label.setText(text)

    @staticmethod
    def update_label_color(label, color):
        label.setStyleSheet(f"color: {color}")
