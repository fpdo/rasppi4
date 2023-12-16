#!/usr/bin/env python3

"""
Simple application to get data from Grove PIR MOtion Sensor.
Init GPIO17 and set it to input to read data from the sensor
Read date every 500ms until keyboard exists
"""

from gpio import GPIO_Handler
import time

sensor = GPIO_Handler(17)
sensor.direction = "in"
end = False

while end == False:
    try:
        is_motion_detected = sensor.value

        if (is_motion_detected == 1):
            print("Motion detected")
        else:
            print(" ")

        time.sleep(0.5)
    except Exception as e:
        print(f"Error reading sensor data: {str(e)}")
    except KeyboardInterrupt:
        print(f"n\Keyboard Interrupt, terminating application")
        end = True

sensor.deinit()
