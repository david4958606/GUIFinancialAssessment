import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QRadioButton, QPushButton, QButtonGroup, QSpacerItem)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class RiskProfilingUI(QWidget):
    save_clicked = pyqtSignal(list)  # Signal to emit when save is clicked

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Risk Profiling')
        self.setFixedSize(640, 600)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel('Risk Profiling')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        layout.addWidget(title)

        layout.addSpacerItem(QSpacerItem(20, 20))

        self.questions = [
            {
                'text': '1. How long do you want to stay invested for?',
                'options': ['1. Less than 1 year',
                            '2. 1 to 3 years',
                            '3. 3 to 7 years',
                            '4. More than 7 years']
            },
            {
                'text': '2. Which option below describes your investment knowledge and experience?',
                'options': ['1. None',
                            '2. Minimal',
                            '3. Moderate',
                            '4. Good',
                            '5. Extensive']
            },
            {
                'text': '3. What level of average of potential investment loss is acceptable to you?',
                'options': ['1. No',
                            '2. Low',
                            '3. Middle',
                            '4. High']
            },
            {
                'text': '4. Will your financial situation change over the next 12 months?',
                'options': ['1. Worse',
                            '2. No',
                            '3. Better']
            }
        ]

        self.button_groups = []

        for question in self.questions:
            q_label = QLabel(question['text'])
            q_label.setFont(QFont('Arial', 12))
            q_label.setWordWrap(True)
            layout.addWidget(q_label)

            button_group = QButtonGroup()
            self.button_groups.append(button_group)

            for i, option in enumerate(question['options']):
                radio = QRadioButton(option)
                radio.setFont(QFont('Arial', 11))
                button_group.addButton(radio, i)
                layout.addWidget(radio)

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
        for i, group in enumerate(self.button_groups):
            selected = group.checkedButton()
            if selected:
                results.append((self.questions[i]['text'], selected.text()))
            else:
                results.append((self.questions[i]['text'], ""))
        self.save_clicked.emit(results)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RiskProfilingUI()
    ex.show()
    sys.exit(app.exec())