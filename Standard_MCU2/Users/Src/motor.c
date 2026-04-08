#include "motor.h"

motor Motor[4] = 
{
	{&htim2, TIM_CHANNEL_2, AIN1_GPIO_Port, AIN1_Pin, AIN2_GPIO_Port, AIN2_Pin},//左前
	{&htim2, TIM_CHANNEL_3, BIN1_GPIO_Port, BIN1_Pin, BIN2_GPIO_Port, BIN2_Pin},//右前
	{&htim4, TIM_CHANNEL_1, CIN1_GPIO_Port, CIN1_Pin, CIN2_GPIO_Port, CIN2_Pin},//左后
	{&htim4, TIM_CHANNEL_2, DIN1_GPIO_Port, DIN1_Pin, DIN2_GPIO_Port, DIN2_Pin}//右后
};//存放驱动电机的引脚数据
servo Servo[4]=
{
	{&htim2,TIM_CHANNEL_1},
	{&htim1,TIM_CHANNEL_1},
	{&htim1,TIM_CHANNEL_2},
  {&htim1,TIM_CHANNEL_3}
};
void turn_servo(servo *Servo,int id,float angle)
{
	if (angle > 180) {
        angle = 180;
    }
    angle = (angle * 50) / 9 + 250;
		__HAL_TIM_SET_COMPARE(Servo[id].htim,Servo[id].Channel,angle ); 
}
uint8_t rx_index = 0;   // 缓冲区索引
uint8_t rx_byte;         // 中断接收缓冲区（单字节）
uint8_t rx_buf[1000];      //临时缓存区
uint8_t state = 0; // 状态机位置
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) {
    static uint8_t state = 0; // 状态机位置
    static uint8_t cnt = 0;   // 字节计数器

    if (huart->Instance == USART3) { // 确认是hc05/06的所连接的串口
        switch (state) {
            case 0: // 等待帧头
                if (rx_byte == 0xAA) state = 1;
                break;
            case 1:
                rx_buf[cnt++] = rx_byte;
                if (cnt >= 5) state = 2;//一共存储了5位
                break;

            case 2: // 等待帧尾
                if (rx_byte == 0x55) state=3;
                state = 0;//失败则重置状态机
                break;
        }
        HAL_UART_Receive_IT(huart, &rx_byte, 1);
    }
}
void set_speed(int id, int speed,motor *Motor)//速度范围-100--100
{
	if(speed>0)
	{
		HAL_GPIO_WritePin(Motor[id].motor_gpio_port_a,Motor[id].gpio_pin_a,GPIO_PIN_RESET);
		HAL_GPIO_WritePin(Motor[id].motor_gpio_port_b,Motor[id].gpio_pin_b,GPIO_PIN_SET);
		__HAL_TIM_SET_COMPARE(Motor[id].htim,Motor[id].Channel,speed*10); 
	}else if  (speed==0)
	{
		HAL_GPIO_WritePin(Motor[id].motor_gpio_port_a,Motor[id].gpio_pin_a,GPIO_PIN_RESET);
		HAL_GPIO_WritePin(Motor[id].motor_gpio_port_b,Motor[id].gpio_pin_b,GPIO_PIN_RESET);
		__HAL_TIM_SET_COMPARE(Motor[id].htim,Motor[id].Channel,speed);
	}
	else{
		HAL_GPIO_WritePin(Motor[id].motor_gpio_port_a,Motor[id].gpio_pin_a,GPIO_PIN_SET);
		HAL_GPIO_WritePin(Motor[id].motor_gpio_port_b,Motor[id].gpio_pin_b,GPIO_PIN_RESET);
		__HAL_TIM_SET_COMPARE(Motor[id].htim,Motor[id].Channel,(-speed));
	}
}
void stop(void){
		set_speed(0,0,Motor);
		set_speed(1,0,Motor);
		set_speed(2,0,Motor);
		set_speed(3,0,Motor);
}
void forward (void)
{
		set_speed(0,60,Motor);
		set_speed(1,60,Motor);
		set_speed(2,60,Motor);
		set_speed(3,60,Motor);
}
void right (void)
{
		set_speed(0,60,Motor);
		set_speed(1,30,Motor);
		set_speed(2,60,Motor);
		set_speed(3,30,Motor);
}
void left (void)
{
		set_speed(0,30,Motor);
		set_speed(1,60,Motor);
		set_speed(2,30,Motor);
		set_speed(3,60,Motor);
}
void back (void )
{
		set_speed(0,-60,Motor);
		set_speed(1,-60,Motor);
		set_speed(2,-60,Motor);
		set_speed(3,-60,Motor);
}
	