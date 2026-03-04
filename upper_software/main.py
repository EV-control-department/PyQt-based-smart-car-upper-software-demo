import mainwindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pygame
import serial

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ser = serial.Serial('COM6', 9600, timeout=0)  # 根据实际情况修改串口号和波特率
        self.joystick_init()
        self.acc_slider.valueChanged.connect(self.acc_slider_value_changed)
        self.dir_slider.valueChanged.connect(self.dir_slider_value_changed)
        self.arm_slider.valueChanged.connect(self.arm_slider_value_changed)

    def joystick_init(self):
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"已连接手柄: {self.joystick.get_name()}")

        else:
            self.joystick = None
            print("未检测到手柄，请连接手柄后重启程序")
    
    def joystick_update(self):
        if not self.joystick:
            return
        pygame.event.pump()
        x_val = self.joystick.get_axis(0)
        y_val = self.joystick.get_axis(1)
        hat = self.joystick.get_hat(0)
        button_shoulder = [self.joystick.get_button(4), self.joystick.get_button(5)]
        shoulder = button_shoulder[0] - button_shoulder[1]  # 左肩键为 -1，右肩键为 +1

        self.dir_slider_value_changed(round(x_val * 45))
        self.acc_slider_value_changed(round(y_val * 100))

        if hat[1] == 1:
            self.arm_slider.setValue(self.arm_slider.value() + 1)
        elif hat[1] == -1:
            self.arm_slider.setValue(self.arm_slider.value() - 1)

        if shoulder == 1:
            self.arm_slider.setValue(self.arm_slider.value() + 1)
        elif shoulder == -1:
            self.arm_slider.setValue(self.arm_slider.value() - 1)

        frame = self.build_frame()
        self.ser.write(frame)

        date = self.ser.readline()
        print(date.hex(' ').upper())

    def build_frame(self):

        acc = self.acc_slider.value()+100
        dir = self.dir_slider.value()+45
        arm = self.arm_slider.value()
        sum = (acc + dir + arm) % 256

        frame = bytes([0xFF, acc, dir, arm, sum, 0xFA])

        return frame

    
    def acc_slider_value_changed(self, value):
        self.accelerator.setText(f"油门：{value}")
        self.acc_slider.setValue(value)
    def dir_slider_value_changed(self, value):
        self.direction.setText(f"方向：{value}")
        self.dir_slider.setValue(value)
    def arm_slider_value_changed(self, value):
        self.arm.setText(f"机械臂位置：{value}")
        self.arm_slider.setValue(value)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Smart Car Control")
    window.show()
    time = QTimer()
    time.timeout.connect(window.joystick_update)
    time.start(100)
    app.exec()