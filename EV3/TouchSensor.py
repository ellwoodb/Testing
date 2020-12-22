#!/usr/bin/env python3
from ev3dev.ev3 import*
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import os
os.system('setfont Lat15-TerminusBold14')

ts = TouchSensor()
leds = Leds()

print("Press the touch sensor to change the LED color!")
Sound.speak('Press the touch sensor to change the LED color!')

while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
