# -*- coding: utf-8 -*-
import os
import time

from auxiliary import defaults
from auxiliary import fmcontrol
from auxiliary import dialogcontrol
from auxiliary import parser
from auxiliary import foldbuilder

if dialogcontrol.checkdefaults() == False:
	exit()

strinput = ""
memory = []
firstlaunch = True

while (strinput != defaults.exit):
	print("main>",  end=' ')
	
	if firstlaunch == False:
		strinput = str(input())
	else:
		strinput = defaults.renew
		firstlaunch = False
	
	command = parser.commandparcer(strinput, defaults.singlecommands, defaults.multiplecommands, " ")
	
	if len(command) == 0:
		print("Неверная команда")
		continue
	
	if (command[0] == defaults.renew):
	
		dirtyvaluelist = parser.getvalfromconfigbykeyword(defaults.output,defaults.keywords,defaults.configuration,[""])
		pairs = parser.getparametersandvals(dirtyvaluelist, defaults.parameters, "=", [" ", "	"], ",")

		musdir = parser.getvalfromconfigbykeyword(defaults.music, defaults.keywords, defaults.configuration, defaults.defaultmusicdirs)
		frequency = parser.extractvaluebyparam(defaults.Frequency,pairs)
		duration = int(parser.extractvaluebyparam(defaults.Duration,pairs)[0])
		ext = parser.extractvaluebyparam(defaults.Extention,pairs)
		
		files = foldbuilder.getfilteredfilesdirslist(musdir, ext)
		dirs =  foldbuilder.getfilteredfilesdirslist(musdir, [""])
		print(" Обновлено!")
	
	if (command[0] == defaults.stop):
		fmcontrol.killwave()
		
	if (command[0] == defaults.playlist):
		if (command[1] == ""):
			value = dialogcontrol.playlistfindandplay(dirs, "")
		else:
			value = dialogcontrol.playlistfindandplay(files, command[1])
		
		if value == False:
			continue
		else:
			if (len(value) > 0):
				time.sleep(1)
				sig = ""
				while (sig != defaults.kill):
					print("Ожидание ввода команды: ", end=' ')
					sig = dialogcontrol.getanswer("Разрешено только: (kill, next, prev, leave, touch):", defaults.plsignals, 0)
					if (sig == defaults.kill):
						dialogcontrol.makecontrolfile(defaults.KillFile, 1, "")
						
					if (sig == defaults.next):
						dialogcontrol.makecontrolfile(defaults.NextFile, 1, "")
						
					if (sig == defaults.previous):
						dialogcontrol.makecontrolfile(defaults.PrevFile, 1, "")
						
					if (sig == defaults.touch):
						print("Введи индекс песни: ", end=' ')
						sindex = dialogcontrol.getanswer("Индекс это число! Введи индекс песни: ", defaults.answers, 1)
						index = int(sindex)
						dialogcontrol.makecontrolfile(defaults.TouchFile, 1, index)
						
					if (sig == defaults.leave):
						print("Уверен? y/n д/н:", end=' ')
						answer = dialogcontrol.getanswer("Ответь правильно! y/n д/н:", defaults.answers, 0)
						if (answer == defaults.no or answer == defaults.norus):
							continue
						else:
							break
				continue
			
	if (command[0] == defaults.play):
		if (command[1] == ""):
			print("Нечего проигрывать")
			continue
		else:
			dialogcontrol.findandplay(files, command[1], frequency[0], duration)
	
	if (command[0] == defaults.mem):
		memory = dialogcontrol.listmemory(defaults.MemoryFile)
		if memory != False:
			index = dialogcontrol.askforindex("Введи индекс песни: ")
			dialogcontrol.playproc(memory, frequency[0], index, duration, 2)
	
	if (command[0] == defaults.list):
		dialogcontrol.listmemory(defaults.MemoryFile)

fmcontrol.killwave()