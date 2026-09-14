from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QTextEdit,
)
from PySide6.QtCore import Qt


class DeductionScreen(QWidget):

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
            "QComboBox, QTextEdit { background-color: #111827; color: #f8fafc; border: 1px solid #334155; border-radius: 10px; padding: 10px; }"
        )

        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(40, 30, 40, 30)

        title = QLabel("最終推理")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 30px; font-weight: bold; }")

        suspect_select = QComboBox()
        suspect_select.addItems(["佐藤", "田中", "山本"])
        suspect_select.setStyleSheet("QComboBox { min-height: 40px; }")

        reason = QTextEdit()
        reason.setPlaceholderText("犯人を選んだ理由を入力してください")

        buttons = QHBoxLayout()
        buttons.setSpacing(20)

        back_button = QPushButton("戻る")
        back_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.interrogation_screen
            )
        )

        submit_button = QPushButton("結論を確定")
        submit_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.result_screen
            )
        )

        buttons.addWidget(back_button)
        buttons.addWidget(submit_button)

        layout.addWidget(title)
        layout.addWidget(QLabel("犯人候補"))
        layout.addWidget(suspect_select)
        layout.addWidget(QLabel("推理理由"))
        layout.addWidget(reason)
        layout.addLayout(buttons)

        self.setLayout(layout)
