#!/usr/bin/env python

import RPi.GPIO as GPIO
import argparse

class Relay:
    def __init__(self, gpio, cmd):
        self.gpio = gpio
        # Uses the IO number of the pi
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.gpio, GPIO.OUT)
        self._close() if cmd == 'on' else self._open()

    # Private methods
    def _close(self):
        GPIO.output(self.gpio, GPIO.HIGH)
        print(f'Output on {self.gpio} is HIGH, relay is closed')

    def _open(self):
        GPIO.output(self.gpio, GPIO.LOW)
        print(f'Output on {self.gpio} is LOW, relay is open')

parser = argparse.ArgumentParser(description='Run relay control',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-io', type=int, default=17)
parser.add_argument('-a', type=str, choices=['on', 'off'], default='off')

io = vars(parser.parse_args())['io']
cmd = vars(parser.parse_args())['a']

obj = Relay(io, cmd)