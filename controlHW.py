#!/usr/bin/env python

"""controlHW.py: Control Hardware."""

__author__      = "Léonard Barras"
__copyright__   = "Copyright 2018"

import RPi.GPIO as GPIO
import time

class Raspberry():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)


    def StartPump(self):
        print("start pump")
        GPIO.output(18, GPIO.HIGH)
        
    def StopPump(self):
        print("stop pump")
        GPIO.output(18, GPIO.LOW)

    def Clean(self):
        GPIO.cleanup()
