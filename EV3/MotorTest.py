#!/usr/bin/env python3
from ev3dev.ev3 import*
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import os
os.system('setfont Lat15-TerminusBold14')

ts = TouchSensor()
mL = LargeMotor('outB')
mL.stop_action = 'hold'
mR = LargeMotor('outC')
mL.stop_action = 'hold'

print('Press touchsensor ')
while True:
    if ts.is_pressed:
        mL.run_to_rel_pos(position_sp=1, speed_sp=250)
        mR.run_to_rel_pos(position_sp=840, speed_sp=250)
    else:
        pass
