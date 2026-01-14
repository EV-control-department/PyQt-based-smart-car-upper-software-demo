from demo_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
import sys
import pygame

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.direction_2.valueChanged.connect(self.direction_2_clicked)
        self.v_2.valueChanged.connect(self.v_2_clicked)
        
        # 初始化显示
        self.v_2_clicked()
        self.direction_2_clicked()
        
        # 初始化手柄
        self.init_joystick()

    def init_joystick(self):
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"已连接手柄: {self.joystick.get_name()}")
            
            # 创建定时器定期轮询手柄状态
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.poll_joystick)
            self.timer.start(30) # 30ms 刷新一次
        else:
            self.joystick = None
            print("未检测到手柄，请连接手柄后重启程序")

    def poll_joystick(self):
        if not self.joystick:
            return
            
        pygame.event.pump()
        

        x_val = self.joystick.get_axis(0)
        y_val = self.joystick.get_axis(1)


        # 映射到 Slider 范围
        d_min = self.direction_2.minimum()
        d_max = self.direction_2.maximum()
        # 简单的线性映射: (-1, 1) -> (min, max)
        d_target = round(((x_val + 1) / 2) * (d_max - d_min) + d_min)
        self.direction_2.setValue(d_target)

        v_min = self.v_2.minimum()
        v_max = self.v_2.maximum()
        # 简单的线性映射: (-1, 1) -> (min, max)
        v_target = round(((-y_val + 1) / 2) * (v_max - v_min) + v_min)
        self.v_2.setValue(v_target)

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