from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import Qt


class ResultScreen(QWidget):

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
        )

        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(40, 50, 40, 50)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("推理結果")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 32px; font-weight: bold; }")

        verdict = QLabel("犯人は 佐藤 でした！")
        verdict.setAlignment(Qt.AlignCenter)
        verdict.setStyleSheet("QLabel { font-size: 26px; color: #fbbf24; font-weight: bold; }")

        summary = QLabel("鍵の管理の不自然さと、監視システム停止のタイミングが重要な手がかりでした。")
        summary.setWordWrap(True)
        summary.setAlignment(Qt.AlignCenter)
        summary.setStyleSheet("QLabel { font-size: 18px; color: #cbd5e1; }")

        retry_button = QPushButton("タイトルへ戻る")
        retry_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.title_screen
            )
        )

        layout.addWidget(title)
        layout.addWidget(verdict)
        layout.addWidget(summary)
        layout.addWidget(retry_button)

        self.setLayout(layout)
