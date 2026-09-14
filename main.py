import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from ui.title import TitleScreen
from ui.case_select import CaseSelectScreen
from ui.case_detail import CaseDetailScreen
from ui.investigation import InvestigationScreen
from ui.interrogation import InterrogationScreen
from ui.deduction import DeductionScreen
from ui.result import ResultScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ai推理ゲーム")
        self.resize(1280, 720)
        self.setStyleSheet("QMainWindow { background-color: #0f172a; }")

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # 画面を作成
        self.title_screen = TitleScreen(self)
        self.case_select_screen = CaseSelectScreen(self)
        self.case_detail_screen = CaseDetailScreen(self)
        self.investigation_screen = InvestigationScreen(self)
        self.interrogation_screen = InterrogationScreen(self)
        self.deduction_screen = DeductionScreen(self)
        self.result_screen = ResultScreen(self)

        # 画面を登録
        self.stack.addWidget(self.title_screen)
        self.stack.addWidget(self.case_select_screen)
        self.stack.addWidget(self.case_detail_screen)
        self.stack.addWidget(self.investigation_screen)
        self.stack.addWidget(self.interrogation_screen)
        self.stack.addWidget(self.deduction_screen)
        self.stack.addWidget(self.result_screen)

        # 最初はタイトル画面
        self.stack.setCurrentWidget(self.title_screen)

    def show_screen(self, screen):
        self.stack.setCurrentWidget(screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())