import pygame
import time
import sys
# 初始化 pygame 和手柄模块
pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("未检测到任何手柄，请连接手柄后再运行本程序。")
    sys.exit(1)
# 获取第一个手柄
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"已连接手柄: {joystick.get_name()}")
print("按 Ctrl+C 退出程序")

while True:
    # 必须处理事件队列，否则手柄数据不会更新
    pygame.event.pump()

    x_val = joystick.get_axis(0)    # 通常 0 是左摇杆横向 (Left/Right)
    y_val = joystick.get_axis(1)    # 通常 1 是左摇杆纵向 (Up/Down)
    
    # 使用 \r 可以在同一行刷新打印，避免刷屏
    print(f"\rX轴: {x_val:.3f}, Y轴: {y_val:.3f}   ", end="")
    time.sleep(0.1)
