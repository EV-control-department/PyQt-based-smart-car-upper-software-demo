from demo_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.direction_2.valueChanged.connect(self.direction_2_clicked)
        self.v_2.valueChanged.connect(self.v_2_clicked)
        
        # 初始化显示
        self.v_2_clicked()
        self.direction_2_clicked()

    def direction_2_clicked(self):
        val = self.direction_2.value()
        print(f"Direction: {val}")
        self.direction.setText(f"角度: {val}")
        return val

    def v_2_clicked(self):
        val = self.v_2.value()
        print(f"Speed: {val}")
        self.v.setText(f"速度: {val}")
        return val

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Smart Car Control")
    window.show()
    sys.exit(app.exec())