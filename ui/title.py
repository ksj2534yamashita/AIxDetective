from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
)
from PySide6.QtCore import Qt


class TitleScreen(QWidget):

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
            "border-radius: 12px;"
            "font-size: 18px;"
            "font-weight: bold;"
            "padding: 14px 20px;"
            "}"
            "QPushButton:hover { background-color: #2563eb; }"
            "QPushButton:pressed { background-color: #1e40af; }"
        )

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(18)
        layout.setContentsMargins(60, 40, 60, 40)

        title = QLabel("AI推理ゲーム")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 40px; font-weight: bold; }")

        subtitle = QLabel("AIは嘘をつく。あなたは真実を見抜けるか。")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("QLabel { font-size: 20px; color: #cbd5e1; }")

        start_button = QPushButton("ゲームスタート")
        howto_button = QPushButton("遊び方")
        exit_button = QPushButton("ゲーム終了")

        for button in (start_button, howto_button, exit_button):
            button.setMinimumHeight(60)
            button.setMinimumWidth(260)

        start_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.case_select_screen
            )
        )

        howto_button.clicked.connect(
            lambda: QMessageBox.information(
                self,
                "遊び方",
                "1. 事件を選びます\n2. 証拠と発言を確認します\n3. 推理をまとめて、真相を見つけます\n\nAIは嘘をつくことがあります。根拠を見て、最も筋が通る結論を選んでください。",
            )
        )

        exit_button.clicked.connect(
            self.main_window.close
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(start_button)
        layout.addWidget(howto_button)
        layout.addWidget(exit_button)

        self.setLayout(layout)