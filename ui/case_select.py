from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QMessageBox,
)
from PySide6.QtCore import Qt


class CaseSelectScreen(QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.setStyleSheet(
            "QWidget { background-color: #0f172a; color: #e2e8f0; }"
            "QLabel { color: #f8fafc; }"
            "QPushButton {"
            "background-color: #1d4ed8;"
            "color: #ffffff;"
            "border: none;"
            "border-radius: 10px;"
            "font-size: 16px;"
            "font-weight: bold;"
            "padding: 12px 16px;"
            "}"
            "QPushButton:hover { background-color: #2563eb; }"
            "QPushButton:pressed { background-color: #1e40af; }"
            "QFrame { background-color: #111827; border: 1px solid #334155; border-radius: 14px; }"
        )

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(18)
        layout.setContentsMargins(60, 40, 60, 40)

        title = QLabel("SELECT CASE")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 32px; font-weight: bold; }")

        case1 = QFrame()
        case1_layout = QVBoxLayout()
        case1_layout.setContentsMargins(24, 18, 24, 18)
        case1_layout.setSpacing(10)

        case1_title = QLabel("CASE 001")
        case1_title.setStyleSheet("QLabel { font-size: 16px; color: #93c5fd; }")
        case1_name = QLabel("消えたUSB")
        case1_name.setStyleSheet("QLabel { font-size: 24px; font-weight: bold; }")
        case1_description = QLabel("研究室から重要なUSBが消えた。")
        case1_description.setStyleSheet("QLabel { font-size: 16px; color: #cbd5e1; }")

        investigate_button = QPushButton("この事件を調査")
        investigate_button.setMinimumHeight(52)

        investigate_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.case_detail_screen
            )
        )

        case1_layout.addWidget(case1_title)
        case1_layout.addWidget(case1_name)
        case1_layout.addWidget(case1_description)
        case1_layout.addWidget(investigate_button)

        case1.setLayout(case1_layout)

        back_button = QPushButton("戻る")
        back_button.setMinimumHeight(52)
        back_button.setMinimumWidth(180)

        back_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.title_screen
            )
        )

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(case1)
        layout.addSpacing(10)
        layout.addWidget(back_button, 0, Qt.AlignCenter)

        self.setLayout(layout)