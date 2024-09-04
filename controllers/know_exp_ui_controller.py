from views.know_exp_ui import KnowledgeExperienceUI
from PyQt6.QtWidgets import QApplication
from utilities.file_utils import FileUtils
import sys

class KnowledgeExperienceController:
    def __init__(self):
        self.view = KnowledgeExperienceUI()
        self.view.save_clicked.connect(self.on_save)

    def show(self):
        print("KnowledgeExperienceController: show method called")  # Debug print
        self.view.show()
        self.view.raise_()  # Bring the window to the front
        self.view.activateWindow()  # Activate the window

    def on_save(self, results):
        print("Knowledge and Experience Results:")
        FileUtils.amend_result_file(("Knowledge and Experience Results:"))
        for question, answer in results:
            print(f"Question: {question}")
            FileUtils.amend_result_file((f"Question: {question}"))
            if isinstance(answer, list):
                print("Answer:")
                FileUtils.amend_result_file(("Answer:"))
                for item in answer:
                    print(f"  - {item}")
                    FileUtils.amend_result_file((f"  - {item}"))
            else:
                print(f"Answer: {answer if answer else 'Not answered'}")
                FileUtils.amend_result_file((f"Answer: {answer if answer else 'Not answered'}"))
            print()  # Add a blank line between questions for better readability

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = KnowledgeExperienceController()
    controller.show()
    sys.exit(app.exec())