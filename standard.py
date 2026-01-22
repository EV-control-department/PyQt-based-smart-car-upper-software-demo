from demo_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
import sys
import pygame
import serial
import serial.tools.list_ports

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 串口相关
        self.ser = None
        self.last_sent_cmd = None
        self.init_serial()

        # 设置 Slider 范围为 -100 到 100
        self.direction_2.setRange(-100, 100)
        self.v_2.setRange(-100, 100)

        self.direction_2.valueChanged.connect(self.direction_2_clicked)
        self.v_2.valueChanged.connect(self.v_2_clicked)
        
        # 初始化显示
        self.v_2_clicked()
        self.direction_2_clicked()

        # 串口接收定时器

        # 串口接收定时器
        self.recv_timer = QTimer(self)
        self.recv_timer.timeout.connect(self.read_from_serial)
        self.recv_timer.start(20) # 20ms Check once

        # 初始化手柄
        self.init_joystick()

    def init_serial(self):
        # 尝试自动寻找串口或使用默认
        ports = list(serial.tools.list_ports.comports())
        target_port = None
        
        if len(ports) > 0:
            # 默认选择第一个
            target_port = ports[0].device
            print(f"检测到串口: {[p.device for p in ports]}，选择 {target_port}")
        else:
            print("未检测到串口")
            target_port = 'COM3'

        try:
            self.ser = serial.Serial(target_port, 9600, timeout=0.1)
            print(f"已打开串口: {target_port}")
            self.state.setText(f"已连接: {target_port}")
        except Exception as e:
            print(f"打开串口 {target_port} 失败: {e}")
            self.state.setText("串口错误")

    def send_command(self):
        if not self.ser or not self.ser.is_open:
            return

        speed = self.v_2.value()
        direction = self.direction_2.value()
        
        cmd = b'\x00' # Default Stop

        # 逻辑优先级：方向 > 移动 (或者互斥)
        # 根据下位机 switch-case 结构，同一时间只能响应一个动作
        # 这里定义优先级：如果有转向，则发转向；否则看速度
        
        if direction == 100:
            cmd = b'\x04' # Right
        elif direction == -100:
            cmd = b'\x03' # Left
        elif speed == 100:
            cmd = b'\x01' # Forward
        elif speed == -100:
            cmd = b'\x02' # Back
        else:
            cmd = b'\x00' # Stop

        # 只有指令变化时才发送
        if cmd != self.last_sent_cmd:
            try:
                self.ser.write(cmd)
                print(f"已发送: {cmd.hex()}")
                self.last_sent_cmd = cmd
            except Exception as e:
                print(f"串口写入错误: {e}")

    def read_from_serial(self):
        if self.ser and self.ser.is_open and self.ser.in_waiting:
            try:
                data = self.ser.read(1)
                if data:
                    hex_val = data.hex()
                    print(f"接收: {hex_val}")
                    # 更新状态显示
                    status_map = {
                        '00': "停止",
                        '01': "前进",
                        '02': "后退",
                        '03': "左转",
                        '04': "右转",
                        '05': "上升",
                        '06': "下降"
                    }
                    status_text = status_map.get(hex_val, f"未知({hex_val})")
                    self.state.setText(f"状态: {status_text}")
            except Exception as e:
                print(f"串口读取错误: {e}")

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

        
        # Direction
        if x_val > 0.5:
            d_target = 100
        elif x_val < -0.5:
            d_target = -100
        else:
            d_target = 0
        self.direction_2.setValue(d_target)

        # Speed
        if y_val < -0.5: # 推杆向上
            v_target = 100
        elif y_val > 0.5: # 推杆向下
            v_target = -100
        else:
            v_target = 0
        self.v_2.setValue(v_target)

    def direction_2_clicked(self):
        val = self.direction_2.value()
        self.direction.setText(f"角度: {val}")
        self.send_command()
        return val

    def v_2_clicked(self):
        val = self.v_2.value()
        self.v.setText(f"速度: {val}")
        self.send_command()
        return val

    def closeEvent(self, event):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("串口已关闭。")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Smart Car Control Standard")
    window.show()
    sys.exit(app.exec())