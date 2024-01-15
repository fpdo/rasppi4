#!/usr/bin/env python3

# Application to control Tower Pro MicroServo99 SG90 motor
from gpio import GPIO_Handler

motor = GPIO_Handler(12, "pwm")
motor.direction = "out"
# 20ms~ 50Hz
motor.period = 20
motor.duty_cycle = 50
# motor.enable = 1
