from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QTextEdit,
)
from PySide6.QtCore import Qt


class InvestigationScreen(QWidget):

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
            "QTextEdit { background-color: #111827; color: #f8fafc; border: 1px solid #334155; border-radius: 10px; padding: 10px; }"
        )

        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(40, 30, 40, 30)

        title = QLabel("捜査")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 30px; font-weight: bold; }")

        status = QLabel("USBが消えた現場には、3人の容疑者が残っていた。証拠と話の矛盾を確認しよう。")
        status.setWordWrap(True)
        status.setStyleSheet("QLabel { font-size: 18px; color: #cbd5e1; }")

        evidence_panel = QFrame()
        evidence_layout = QVBoxLayout()
        evidence_layout.setContentsMargins(20, 18, 20, 18)
        evidence_title = QLabel("証拠")
        evidence_title.setStyleSheet("QLabel { font-size: 20px; font-weight: bold; }")
        evidence_text = QTextEdit()
        evidence_text.setReadOnly(True)
        evidence_text.setPlainText(
            "- 研究室の鍵は施錠されていた\n- USBケースは床に落ちていた\n- 21:35に警備室の監視システムが一時的に停止した\n- 佐藤は21:20に鍵を返却したと話している"
        )
        evidence_layout.addWidget(evidence_title)
        evidence_layout.addWidget(evidence_text)
        evidence_panel.setLayout(evidence_layout)

        suspect_panel = QFrame()
        suspect_layout = QVBoxLayout()
        suspect_layout.setContentsMargins(20, 18, 20, 18)
        suspect_title = QLabel("容疑者候補")
        suspect_title.setStyleSheet("QLabel { font-size: 20px; font-weight: bold; }")
        suspect_name = QLabel("佐藤 / 田中 / 山本")
        suspect_name.setStyleSheet("QLabel { font-size: 18px; color: #93c5fd; }")
        suspect_layout.addWidget(suspect_title)
        suspect_layout.addWidget(suspect_name)
        suspect_panel.setLayout(suspect_layout)

        buttons = QHBoxLayout()
        buttons.setSpacing(20)

        back_button = QPushButton("戻る")
        back_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.case_detail_screen
            )
        )

        next_button = QPushButton("尋問へ進む")
        next_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.interrogation_screen
            )
        )

        buttons.addWidget(back_button)
        buttons.addWidget(next_button)

        layout.addWidget(title)
        layout.addWidget(status)
        layout.addWidget(evidence_panel)
        layout.addWidget(suspect_panel)
        layout.addLayout(buttons)

        self.setLayout(layout)
