#!/usr/bin/env python

import argparse
from gpio import GPIO_Handler

parser = argparse.ArgumentParser(description='Run relay control',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-io', type=int, default=17)
parser.add_argument('-o', type=str, choices=['on', 'off'], default='off')

io = vars(parser.parse_args())['io']
cmd = vars(parser.parse_args())['o']

relay = GPIO_Handler(io)
relay.direction = "out"
if (cmd == "on"):
    relay.value = 1
else:
    relay.value = 0

relay.deinit()
