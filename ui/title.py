from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PySide6.QtCore import Qt


class TitleScreen(QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("AI × DETECTIVE")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("AIは嘘をつく。あなたは真実を見抜けるか。")
        subtitle.setAlignment(Qt.AlignCenter)

        start_button = QPushButton("GAME START")
        howto_button = QPushButton("HOW TO PLAY")
        exit_button = QPushButton("EXIT")

        start_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.case_select_screen
            )
        )

        exit_button.clicked.connect(
            self.main_window.close
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addSpacing(40)

        layout.addWidget(start_button)
        layout.addWidget(howto_button)
        layout.addWidget(exit_button)

        self.setLayout(layout)