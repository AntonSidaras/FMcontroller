# -*- coding: utf-8 -*-
import random
import subprocess

from auxiliary import defaults
from auxiliary import fmcontrol
from auxiliary import dialogcontrol
from auxiliary import parser
from auxiliary import foldbuilder

pairs = parser.getparametersandvals(parser.getvalfromconfigbykeyword(defaults.output,defaults.keywords,defaults.configuration,[""]), defaults.parameters, "=", [" ", "	"], ",")

plfile = parser.extractvaluebyparam(defaults.PlaylistFile, pairs)
freq = parser.extractvaluebyparam(defaults.Frequency, pairs)
SOXPIDfilename = parser.extractvaluebyparam(defaults.SoxPidFilename, pairs)
scriptfilename = parser.extractvaluebyparam(defaults.PlayScript, pairs)
killfile = parser.extractvaluebyparam(defaults.KillFile, pairs)
nextfile = parser.extractvaluebyparam(defaults.NextFile, pairs)
prevfile = parser.extractvaluebyparam(defaults.PrevFile, pairs)
touchfile = parser.extractvaluebyparam(defaults.TouchFile, pairs)
tuner = parser.extractvaluebyparam(defaults.TunerScript, pairs)
transmitter = parser.extractvaluebyparam(defaults.Transmitter,pairs)
killtunerfile = parser.extractvaluebyparam(defaults.KillTunerFile,pairs)

subprocess.Popen("python3 " + tuner[0], shell = True)

shuffle = False

if parser.extractvaluebyparam(defaults.Shuffle, pairs)[0] == "on":
	shuffle = True
else:
	shuffle = False

music = (open(plfile[0],'r').read()).split("\n")
index = 0
wasstate = False
first = True

while (index <= len(music)):

	state = fmcontrol.checkwave(SOXPIDfilename[0], killfile[0], nextfile[0], prevfile[0], touchfile[0], defaults.plsignals)
	
	if state == False:
	
		if wasstate == False:
			if first == False:
				if shuffle == False:
					index = index + 1
				else:
					index = random.randint(0,len(music)-1)
		else:
			wasstate = False
		
		dialogcontrol.playproc(music, freq[0], scriptfilename[0], transmitter[0], SOXPIDfilename[0], 0, index, 3)
			
		first = False
			
	else:
		if state == defaults.kill:
			fmcontrol.killwave(SOXPIDfilename[0])
			dialogcontrol.makecontrolfile(killtunerfile[0], 1, "")
			exit()
			
		if state == defaults.next:
			fmcontrol.killwave(SOXPIDfilename[0])
			wasstate = True
			if shuffle == False:
				index = (index + 1) % len(music)
			else:
				index = random.randint(0,len(music)-1)
				
		if state == defaults.previous:
			fmcontrol.killwave(SOXPIDfilename[0])
			wasstate = True
			if shuffle == False:
				index = (index - 1) % len(music)
			else:
				index = random.randint(0,len(music)-1)
				
		if state.find(defaults.touch) != -1:
			wasstate = True
			if 0 <= int(state[len(defaults.touch):]) <= len(music):
				fmcontrol.killwave(SOXPIDfilename[0])
				index = int(state[len(defaults.touch):])
			else:
				print("Неверный индес, индекс не изменён!")

dialogcontrol.makecontrolfile(killtunerfile[0], 1, "")
print("Проигрывание плейлиста завершено")