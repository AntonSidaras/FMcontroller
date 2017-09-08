# -*- coding: utf-8 -*-
import time
import os
import RPi.GPIO as GPIO

from auxiliary import dialogcontrol
from auxiliary import defaults
from auxiliary import parser

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.IN) #previous
GPIO.setup(37, GPIO.IN) #next
prev = False
next = False

while (os.path.exists(defaults.KillTunerFile) == False):

	time.sleep(1)
	prev = GPIO.input(35)
	next = GPIO.input(37)
	
	if prev == True:
		dialogcontrol.makecontrolfile(defaults.PrevFile, 5, "")
		prev = False
		continue
	
	if	next == True:
		dialogcontrol.makecontrolfile(defaults.NextFile, 5, "")
		next = False
		continue

os.remove(defaults.KillTunerFile)
exit()