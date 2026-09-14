from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QTextEdit,
    QComboBox,
)
from PySide6.QtCore import Qt


class InterrogationScreen(QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.current_suspect = "佐藤"
        self.suspects = {
            "佐藤": {
                "default": "「それは覚えている。監視カメラの記録と、鍵の管理の時刻が重要だよ」",
                "usb": "「USBは研究室の机の上に置いていたはずだ。私は持っていない」",
                "key": "「鍵は私が最後に閉めた。田中が出ていくのを見たよ」",
                "camera": "「カメラの時間は21:32に一瞬止まっていた。あの時刻が気になる」",
                "alibi": "「21:30ごろ、会議室で資料を確認していた。目撃者がいるはずだ」",
                "people": "「田中はいつも急いでいたし、山本はあまり話さないから不安だった」",
                "generic": "「それについては、あまり詳しくはないけど、状況のほうが気になる」",
            },
            "田中": {
                "default": "「私はあの場面を見ていた。だが、証拠の順番がぐちゃぐちゃだと困る」",
                "usb": "「USBのことは聞いたことがある。だが自分が持っていた形跡はない」",
                "key": "「鍵は普段、研究室の前の棚に置いていたはずだ。私はそれを見ていた」",
                "camera": "「カメラは一瞬止まっていたが、誰が止めたかまでは知らない」",
                "alibi": "「21:20ごろに廊下で佐藤と話していた。そこからすぐに戻った」",
                "people": "「山本はいつも神経質だし、佐藤は冷静すぎて不自然だった」",
                "generic": "「その話は単独で判断するには危ない。条件を揃えて考えたほうがいい」",
            },
            "山本": {
                "default": "「私は話しているつもりだ。だが、真実は証拠でしか決まらない」",
                "usb": "「USBに触れた覚えはない。私が欲しいと思ったこともない」",
                "key": "「鍵のことは知っているが、勝手に触ったわけではない」",
                "camera": "「監視カメラの停止時間は、たまたま見ていなかっただけだ」",
                "alibi": "「21:30には自室にいた。誰かと話していたかは覚えている」",
                "people": "「佐藤は口数が少ないが、田中は話しすぎるタイプだ」",
                "generic": "「その質問は前提が曖昧だ。まず、証拠から整理しよう」",
            },
        }

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
            "QComboBox { background-color: #111827; color: #f8fafc; border: 1px solid #334155; border-radius: 8px; padding: 8px; min-height: 36px; }"
        )

        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(40, 30, 40, 30)

        title = QLabel("容疑者への尋問")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("QLabel { font-size: 30px; font-weight: bold; }")

        suspect_row = QHBoxLayout()
        suspect_label = QLabel("対象:")
        suspect_label.setStyleSheet("QLabel { font-size: 20px; }")
        self.suspect_combo = QComboBox()
        self.suspect_combo.addItems(["佐藤", "田中", "山本"])
        self.suspect_combo.currentTextChanged.connect(self.change_suspect)
        suspect_row.addWidget(suspect_label)
        suspect_row.addWidget(self.suspect_combo)
        suspect_row.addStretch()

        self.suspect_name = QLabel(f"対象: {self.current_suspect}")
        self.suspect_name.setStyleSheet("QLabel { font-size: 22px; color: #93c5fd; }")

        question_box = QFrame()
        question_layout = QVBoxLayout()
        question_layout.setContentsMargins(20, 18, 20, 18)
        question_title = QLabel("質問を入力")
        question_title.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; }")
        self.question_input = QTextEdit()
        self.question_input.setPlaceholderText("例: USBはどこに置いていたの？\n例: 21:30に誰といたの？")
        self.question_input.setMinimumHeight(100)
        question_layout.addWidget(question_title)
        question_layout.addWidget(self.question_input)
        question_box.setLayout(question_layout)

        answer_box = QFrame()
        answer_layout = QVBoxLayout()
        answer_layout.setContentsMargins(20, 18, 20, 18)
        answer_title = QLabel("容疑者の返答")
        answer_title.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; }")
        self.answer_text = QTextEdit()
        self.answer_text.setPlainText(self.suspects[self.current_suspect]["default"])
        self.answer_text.setReadOnly(True)
        answer_layout.addWidget(answer_title)
        answer_layout.addWidget(self.answer_text)
        answer_box.setLayout(answer_layout)

        buttons = QHBoxLayout()
        buttons.setSpacing(20)

        ask_button = QPushButton("質問する")
        ask_button.clicked.connect(self.ask_question)

        back_button = QPushButton("戻る")
        back_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.investigation_screen
            )
        )

        next_button = QPushButton("推理へ進む")
        next_button.clicked.connect(
            lambda: self.main_window.show_screen(
                self.main_window.deduction_screen
            )
        )

        buttons.addWidget(ask_button)
        buttons.addWidget(back_button)
        buttons.addWidget(next_button)

        layout.addWidget(title)
        layout.addLayout(suspect_row)
        layout.addWidget(self.suspect_name)
        layout.addWidget(question_box)
        layout.addWidget(answer_box)
        layout.addLayout(buttons)

        self.setLayout(layout)

    def change_suspect(self, suspect_name):
        self.current_suspect = suspect_name
        self.suspect_name.setText(f"対象: {suspect_name}")
        self.answer_text.setPlainText(self.suspects[suspect_name]["default"])

    def ask_question(self):
        question = self.question_input.toPlainText().strip()
        if not question:
            self.answer_text.setPlainText("質問を入力してください。")
            return

        answer = self.generate_answer(question)
        self.answer_text.setPlainText(answer)
        self.question_input.clear()

    def generate_answer(self, question):
        q = question.lower()
        suspect = self.suspects[self.current_suspect]

        if "usb" in q or "メモリ" in q or "持って" in q or "置い" in q:
            return suspect["usb"]
        if "鍵" in q or "閉め" in q or "施錠" in q or "戻し" in q:
            return suspect["key"]
        if "カメラ" in q or "監視" in q or "証拠" in q or "時間" in q:
            return suspect["camera"]
        if "アリバイ" in q or "どこ" in q or "いた" in q or "場所" in q:
            return suspect["alibi"]
        if "田中" in q or "佐藤" in q or "山本" in q or "他人" in q or "友人" in q:
            return suspect["people"]
        return suspect["generic"]
