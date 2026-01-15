import serial

# 打开串口
ser = serial.Serial('COM5', 9600, timeout=1)  # 根据实际情况修改串口号和波特率

# 发送数据
ser.write(b'Hello, World!\n')

# 接收数据
data = ser.readline()
print(data.decode().strip())

# 关闭串口
ser.close()
