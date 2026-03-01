import mainwindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pygame
from pygame import joystick

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.acc_slider.valueChanged.connect(self.acc_slider_value_changed)
        self.dir_slider.valueChanged.connect(self.dir_slider_value_changed)
        self.arm_slider.valueChanged.connect(self.arm_slider_value_changed)
        self.joystick_init()
        
    
    def joystick_init(self):
        pygame.init() # 初始化 pygame 所有模块，包括事件系统
        joystick.init()
        if joystick.get_count() > 0:
            self.joystick = joystick.Joystick(0)
            self.joystick.init()
            print(f"已连接手柄: {self.joystick.get_name()}")
        else:
            self.joystick = None
            print("未检测到手柄，请连接手柄后重启程序")

    def update(self):
        self.joystick_update()
        self.button_update()
        self.hat_update()

    def hat_update(self):
        if self.joystick:
            hat_val = self.joystick.get_hat(0)    # 通常 0 是方向键
            print(f"\r方向键: {hat_val}   ", end="")
            if hat_val[1] == 1:
                self.arm_slider.setValue(self.arm_slider.value() + 1)  # 向上增加机械臂位置
                self.joystick.rumble(0.5, 0.5, 200)  # 震动反馈，持续200ms
            elif hat_val[1] == -1:
                self.arm_slider.setValue(self.arm_slider.value() - 1)  # 向下减少机械臂位置
                self.joystick.rumble(0.5, 0.5, 200)  # 震动反馈，持续200ms

    def joystick_update(self):
        if self.joystick:
            pygame.event.pump()
            x_val = self.joystick.get_axis(0)    # 通常 0 是左摇杆横向 (Left/Right)
            y_val = self.joystick.get_axis(1)    # 通常 1 是左摇杆纵向 (Up/Down)
            print(f"\rX轴: {x_val:.3f}, Y轴: {y_val:.3f}   ", end="")
            self.acc_slider.setValue(round(x_val * 100))
            self.dir_slider.setValue(round(y_val * 45))

    def button_update(self):
        if self.joystick:
            if self.joystick.get_button(4):
                self.arm_slider.setValue(self.arm_slider.value() - 1)  # 向上增加机械臂位置
                self.joystick.rumble(0.5, 0.5, 200)  # 震动反馈，持续200ms
            elif self.joystick.get_button(5):
                self.arm_slider.setValue(self.arm_slider.value() + 1)  # 向下减少机械臂位置
                self.joystick.rumble(0.5, 0.5, 200)  # 震动反馈，持续200ms

            


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
    time = QTimer()
    time.timeout.connect(window.update)
    time.start(100)  # 每100ms触发一次
    app.exec()
