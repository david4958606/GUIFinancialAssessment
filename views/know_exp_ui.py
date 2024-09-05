import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QRadioButton, QPushButton, QButtonGroup, QSpacerItem,
                             QCheckBox)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class KnowledgeExperienceUI(QWidget):
    save_clicked = pyqtSignal(list)  # Signal to emit when save is clicked

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Your Knowledge and Experience')
        self.setFixedSize(640, 600)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel('Your Knowledge and Experience')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        layout.addWidget(title)

        layout.addSpacerItem(QSpacerItem(20, 20))

        self.questions = [
            {
                'text': '1. I have a diploma or higher qualification in finance, business or accounting',
                'type': 'radio',
                'options': ['Yes', 'No']
            },
            {
                'text': '2. I have a professional finance qualification',
                'type': 'radio',
                'options': ['Yes', 'No']
            },
            {
                'text': '3. In the last 10 years, I have at least 3 years of working experience in finance or accounting',
                'type': 'radio',
                'options': ['Yes', 'No']
            },
            {
                'text': '4. In the last 3 years, I have performed at least 6 investment-related transactions',
                'type': 'checkbox',
                'options': [
                    'Group A: Unit trust, insurance',
                    'Group B: Currency-linked investments',
                    'Group C: Futures, Certificates, Contracts, etc.',
                    'None of above'
                ]
            }
        ]

        self.button_groups = []
        self.checkboxes = []

        for question in self.questions:
            q_label = QLabel(question['text'])
            q_label.setFont(QFont('Arial', 12))
            q_label.setWordWrap(True)
            layout.addWidget(q_label)

            if question['type'] == 'radio':
                button_group = QButtonGroup()
                self.button_groups.append(button_group)
                for i, option in enumerate(question['options']):
                    radio = QRadioButton(option)
                    radio.setFont(QFont('Arial', 11))
                    button_group.addButton(radio, i)
                    layout.addWidget(radio)
            elif question['type'] == 'checkbox':
                for option in question['options']:
                    checkbox = QCheckBox(option)
                    checkbox.setFont(QFont('Arial', 11))
                    self.checkboxes.append(checkbox)
                    layout.addWidget(checkbox)

            layout.addSpacerItem(QSpacerItem(10, 10))

        layout.addStretch(1)

        save_button = QPushButton('Save && Continue')
        save_button.setFont(QFont('Arial', 12))
        save_button.setFixedSize(100, 30)
        save_button.clicked.connect(self.on_save_clicked)
        layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def on_save_clicked(self):
        results = []
        for i, question in enumerate(self.questions):
            if question['type'] == 'radio':
                selected = self.button_groups[i].checkedButton()
                if selected:
                    results.append((question['text'], selected.text()))
                else:
                    results.append((question['text'], ""))
            elif question['type'] == 'checkbox':
                selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
                results.append((question['text'], selected if selected else ["None selected"]))
        self.save_clicked.emit(results)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KnowledgeExperienceUI()
    ex.show()
    sys.exit(app.exec())