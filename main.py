from PyQt6 import QtWidgets
from controllers.main_ui_controller import MainUiController
from utilities.file_utils import FileUtils

if __name__ == "__main__":
    FileUtils.new_result_file()  # Create a new result file
    app = QtWidgets.QApplication([])

    controller = MainUiController()
    controller.show_main_window()    # Show the main window

    app.exec()
