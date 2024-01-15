#!/usr/bin/env python3

import adafruit_dht
import time
import board

# Initialize sensor connected to GPIO17
sensor = adafruit_dht.DHT11(board.D17)

end = False
while not end:
    time.sleep(2)
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print(f"Temp: {temp}C    Humidity: {humidity}%")
    except RuntimeError as e:
        print(e.args[0])
        time.sleep(2.0)
        continue
    except KeyboardInterrupt:
        print(f"n\Keyboard Interrupt, terminating application")
        sensor.exit()
        end = True
    except Exception as e:
        sensor.exit()
        end = True
        print (f"Error: {str(e)}")

