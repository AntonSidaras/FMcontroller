# -*- coding: utf-8 -*-
import time
import os
import RPi.GPIO as GPIO

from auxiliary import dialogcontrol
from auxiliary import defaults
from auxiliary import parser

pairs = parser.getparametersandvals(parser.getvalfromconfigbykeyword(defaults.output,defaults.keywords,defaults.configuration,[""]), defaults.parameters, "=", [" ", "	"], ",")
nextfile = parser.extractvaluebyparam(defaults.NextFile,pairs)
prevfile = parser.extractvaluebyparam(defaults.PrevFile,pairs)
killtunerfile = parser.extractvaluebyparam(defaults.KillTunerFile,pairs)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.IN) #previous
GPIO.setup(37, GPIO.IN) #next
prev = False
next = False

while (os.path.exists(killtunerfile[0]) == False):

	time.sleep(1)
	prev = GPIO.input(35)
	next = GPIO.input(37)
	
	if prev == True:
		dialogcontrol.makecontrolfile(prevfile[0], 5, "")
		prev = False
		continue
	
	if	next == True:
		dialogcontrol.makecontrolfile(nextfile[0], 5, "")
		next = False
		continue

os.remove(killtunerfile[0])