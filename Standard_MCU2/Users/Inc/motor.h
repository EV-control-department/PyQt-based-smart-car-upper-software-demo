#ifndef MOTOR_H_
#define MOTOR_H_
#include "main.h"
#include "tim.h"

void stop(void);
typedef struct
{
	TIM_HandleTypeDef *htim;
	uint32_t Channel;
	GPIO_TypeDef *motor_gpio_port_a;
	uint16_t gpio_pin_a;
	GPIO_TypeDef *motor_gpio_port_b;
	uint16_t gpio_pin_b;
}motor;
typedef struct
{
	TIM_HandleTypeDef *htim;
	uint32_t Channel;
}servo;
void set_speed(int id, int speed,motor *Motor);

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart);
void turn_servo(servo *Servo,int id,float speed);
void forward (void);
void back (void);
void left (void);
void right (void);
#endif /* MOTOR_H_ */

