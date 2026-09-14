from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
)
from PySide6.QtCore import Qt


class CaseDetailScreen(QWidget):

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
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(18)
        layout.setContentsMargins(50, 30, 50, 30)

        title = QLabel("事件概要")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 32px; font-weight: bold; }")

        case_card = QFrame()
        case_layout = QVBoxLayout()
        case_layout.setContentsMargins(24, 18, 24, 18)
        case_layout.setSpacing(10)

        case_name = QLabel("CASE 001: 消えたUSB")
        case_name.setStyleSheet("QLabel { font-size: 28px; font-weight: bold; color: #93c5fd; }")

        details = [
            "発生日時: 2026年3月12日 21:30",
            "発生場所: 研究室 B",
            "被害者: 田村 研究員",
            "被害内容: 重要なUSBメモリが失われた",
            "状況: 研究室内のドアは施錠されており、出入口には警備カメラが設置されていた",
        ]

        for text in details:
            label = QLabel(text)
            label.setWordWrap(True)
            label.setStyleSheet("QLabel { font-size: 16px; color: #e2e8f0; }")
            case_layout.addWidget(label)

        case_card.setLayout(case_layout)

        suspects = QFrame()
        suspects_layout = QHBoxLayout()
        suspects_layout.setContentsMargins(20, 18, 20, 18)

        for name, status in [("佐藤", "冷静な同僚"), ("田中", "研究室の友人"), ("山本", "警戒心が強い人物")]:
            person = QFrame()
            person_layout = QVBoxLayout()
            person_layout.setContentsMargins(12, 10, 12, 10)
            person_name = QLabel(name)
            person_name.setStyleSheet("QLabel { font-size: 20px; font-weight: bold; }")
            person_status = QLabel(status)
            person_status.setWordWrap(True)
            person_status.setStyleSheet("QLabel { font-size: 14px; color: #cbd5e1; }")
            person_layout.addWidget(person_name)
            person_layout.addWidget(person_status)
            person.setLayout(person_layout)
            suspects_layout.addWidget(person)

        suspects.setLayout(suspects_layout)

        buttons = QHBoxLayout()
        buttons.setSpacing(20)

        back_button = QPushButton("戻る")
        back_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.case_select_screen
            )
        )

        start_button = QPushButton("調査開始")
        start_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.investigation_screen
            )
        )

        buttons.addWidget(back_button)
        buttons.addWidget(start_button)

        layout.addWidget(title)
        layout.addWidget(case_card)
        layout.addWidget(QLabel("容疑者一覧"))
        layout.addWidget(suspects)
        layout.addLayout(buttons)

        self.setLayout(layout)
