from PyQt6 import QtWidgets
from controllers.app_controller import AppController
from utilities.file_utils import FileUtils
import sys

def main():
    FileUtils.new_result_file()
    app = QtWidgets.QApplication([])
    controller = AppController()
    controller.show_main()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
