#!/usr/bin/env python3

import serial
import time

uart = serial.Serial("/dev/ttyS0", 9600)

end = False
while end == False:
    try:
        data = uart.read()
        time.sleep(0.03)
        data_left = uart.inWaiting()
        data += uart.read(data_left)
        print(f"received data: {data}")
        end = True
    except Exception as e:
        print(f"Error reading data: {str(e)}")
    except KeyboardInterrupt:
        print(f"\nKeyboard Interrupt, terminating application")
        end = True
