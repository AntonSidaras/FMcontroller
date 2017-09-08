# -*- coding: utf-8 -*-
import random
import subprocess

from auxiliary import defaults
from auxiliary import fmcontrol
from auxiliary import dialogcontrol
from auxiliary import parser
from auxiliary import foldbuilder

pairs = parser.getparametersandvals(parser.getvalfromconfigbykeyword(defaults.output,defaults.keywords,defaults.configuration,[""]), defaults.parameters, "=", [" ", "	"], ",")

frequency = parser.extractvaluebyparam(defaults.Frequency, pairs)

subprocess.Popen("python3 " + defaults.TunerScript, shell = True)

shuffle = False

if parser.extractvaluebyparam(defaults.Shuffle, pairs)[0] == "on":
	shuffle = True
else:
	shuffle = False

music = (open(defaults.PlaylistFile,'r').read()).split("\n")
index = 0
wasstate = False
first = True

while (index <= len(music)):

	state = fmcontrol.checkwave()
	
	if state == False:
	
		if wasstate == False:
			if first == False:
				if shuffle == False:
					index = index + 1
				else:
					index = random.randint(0,len(music)-1)
		else:
			wasstate = False
		
		dialogcontrol.playproc(music, frequency[0], index, 0, 3)
			
		first = False
			
	else:
		if state == defaults.kill:
			fmcontrol.killwave()
			dialogcontrol.makecontrolfile(defaults.KillTunerFile, 1, "")
			exit()
			
		if state == defaults.next:
			fmcontrol.killwave()
			wasstate = True
			if shuffle == False:
				index = (index + 1) % len(music)
			else:
				index = random.randint(0,len(music)-1)
				
		if state == defaults.previous:
			fmcontrol.killwave()
			wasstate = True
			if shuffle == False:
				index = (index - 1) % len(music)
			else:
				index = random.randint(0,len(music)-1)
				
		if state.find(defaults.touch) != -1:
			wasstate = True
			if 0 <= int(state[len(defaults.touch):]) <= len(music):
				fmcontrol.killwave()
				index = int(state[len(defaults.touch):])
			else:
				print("Неверный индес, индекс не изменён!")

dialogcontrol.makecontrolfile(defaults.KillTunerFile, 1, "")
print("Проигрывание плейлиста завершено")