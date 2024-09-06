import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QRadioButton, QPushButton, QButtonGroup, QSpacerItem)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class InvestmentPreferencesUI(QWidget):
    save_clicked = pyqtSignal(tuple)  # Signal to emit when save is clicked

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Your Investment Preferences')
        self.setFixedSize(500, 400)  # Reduced size due to fewer elements

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel('Your Investment Preferences')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        layout.addWidget(title)

        layout.addSpacerItem(QSpacerItem(20, 20))

        self.question = 'How often will you monitor or review your investments?'
        self.options = ['1. Annually', '2. Half yearly', '3. Quarterly', '4. Monthly']

        q_label = QLabel(self.question)
        q_label.setFont(QFont('Arial', 12))
        q_label.setWordWrap(True)
        layout.addWidget(q_label)

        self.button_group = QButtonGroup()
        for i, option in enumerate(self.options):
            radio = QRadioButton(option)
            radio.setFont(QFont('Arial', 11))
            self.button_group.addButton(radio, i)
            layout.addWidget(radio)

        layout.addStretch(1)

        save_button = QPushButton('Save && Continue')
        save_button.setFont(QFont('Arial', 12))
        save_button.setFixedSize(150, 30)
        save_button.clicked.connect(self.on_save_clicked)
        layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def on_save_clicked(self):
        selected = self.button_group.checkedButton()
        if selected:
            self.save_clicked.emit((self.question, selected.text()))
        else:
            self.save_clicked.emit((self.question, ""))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InvestmentPreferencesUI()
    ex.show()
    sys.exit(app.exec())