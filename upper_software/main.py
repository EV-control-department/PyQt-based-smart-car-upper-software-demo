import mainwindow
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.acc_slider.valueChanged.connect(self.acc_slider_value_changed)
        self.dir_slider.valueChanged.connect(self.dir_slider_value_changed)
        self.arm_slider.valueChanged.connect(self.arm_slider_value_changed)
    
    def acc_slider_value_changed(self, value):
        self.accelerator.setText(f"油门：{value}")
    def dir_slider_value_changed(self, value):
        self.direction.setText(f"方向：{value}")
    def arm_slider_value_changed(self, value):
        self.arm.setText(f"机械臂位置：{value}")



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Smart Car Control")
    window.show()
    app.exec()