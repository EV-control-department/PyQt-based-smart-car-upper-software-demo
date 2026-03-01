import demo
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow, demo.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.change_text)

    def change_text(self):
        self.label.setText("好的，我们成功了")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Smart Car Control")
    window.show()
    app.exec()