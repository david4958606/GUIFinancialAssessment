import os
from PyQt6 import QtWidgets
from utilities.file_utils import FileUtils
from utilities.result_utils import ResultUtils


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
        if not FileUtils.check_result_file():
            UiUtils.show_warning("Result not found")

    @staticmethod
    def update_label_text(label, text):
        label.setText(text)

    @staticmethod
    def update_label_color(label, color):
        label.setStyleSheet(f"color: {color}")

    @staticmethod
    def show_result():
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Information")
        text = ResultUtils.recommend_products()
        msg_box.setText(text)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

