#!/usr/bin/env python3

"""
This is a simple test application that will toogle a LED on GPIO18
every second for 10 seconds
"""

from gpio import GPIO_Handler
import time

led = GPIO_Handler(18)
led.direction = "out"

for i in range(0, 11):
    led.value = (i % 2)
    time.sleep(1)

# Set direction back to default
led.direction = "in"
led.deinit()
