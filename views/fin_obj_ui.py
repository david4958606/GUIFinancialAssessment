import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                             QRadioButton, QPushButton, QButtonGroup, QSpacerItem)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class FinancialObjectiveUI(QWidget):
    save_clicked = pyqtSignal(str)  # Signal to emit when save is clicked

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Financial Objective')
        self.setFixedSize(640, 480)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel('Your Financial Objective')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        layout.addWidget(title)

        layout.addSpacerItem(QSpacerItem(20, 20))

        question = QLabel('When it comes to investing, what is your goal?')
        question.setFont(QFont('Arial', 14))
        question.setWordWrap(True)
        layout.addWidget(question)

        self.button_group = QButtonGroup()
        options = ['1. Growing your wealth',
                   '2. Generating income', '3. Preserving your capital']
        for i, option in enumerate(options):
            radio = QRadioButton(option)
            radio.setFont(QFont('Arial', 12))
            self.button_group.addButton(radio, i)
            layout.addWidget(radio)

        layout.addStretch(1)

        save_button = QPushButton('Save & Next')
        save_button.setFont(QFont('Arial', 12))
        save_button.setFixedSize(100, 30)
        save_button.clicked.connect(self.on_save_clicked)
        layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def on_save_clicked(self):
        selected = self.button_group.checkedButton()
        if selected:
            self.save_clicked.emit(selected.text())
        else:
            self.save_clicked.emit("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FinancialObjectiveUI()
    ex.show()
    sys.exit(app.exec())
