# -*- coding: utf-8 -*-
import os
import time

from auxiliary import defaults
from auxiliary import fmcontrol
from auxiliary import dialogcontrol
from auxiliary import parser
from auxiliary import foldbuilder

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
		scriptfilename = parser.extractvaluebyparam(defaults.PlayScript,pairs)
		plfile = parser.extractvaluebyparam(defaults.PlaylistFile,pairs)
		plscript = parser.extractvaluebyparam(defaults.PlaylistScript,pairs)
		freq = parser.extractvaluebyparam(defaults.Frequency,pairs)
		killfile = parser.extractvaluebyparam(defaults.KillFile,pairs)
		nextfile = parser.extractvaluebyparam(defaults.NextFile,pairs)
		prevfile = parser.extractvaluebyparam(defaults.PrevFile,pairs)
		touchfile = parser.extractvaluebyparam(defaults.TouchFile,pairs)
		SOXPIDfilename = parser.extractvaluebyparam(defaults.SoxPidFilename,pairs)
		duration = int(parser.extractvaluebyparam(defaults.Duration,pairs)[0])
		memfile = parser.extractvaluebyparam(defaults.MemoryFile,pairs)
		ext = parser.extractvaluebyparam(defaults.Extention,pairs)
		transmitter = parser.extractvaluebyparam(defaults.Transmitter,pairs)

		files = foldbuilder.getfilteredfilesdirslist(musdir, ext)
		dirs =  foldbuilder.getfilteredfilesdirslist(musdir, [""])
		print(" Обновлено!")
	
	if (command[0] == defaults.stop):
		fmcontrol.killwave(SOXPIDfilename[0])
		
	if (command[0] == defaults.playlist):
		if (command[1] == ""):
			value = dialogcontrol.playlistfindandplay(dirs, "", memfile, plfile, plscript)
		else:
			value = dialogcontrol.playlistfindandplay(files, command[1], memfile, plfile, plscript)
		
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
						dialogcontrol.makecontrolfile(killfile[0], 1, "")
						
					if (sig == defaults.next):
						dialogcontrol.makecontrolfile(nextfile[0], 1, "")
						
					if (sig == defaults.previous):
						dialogcontrol.makecontrolfile(prevfile[0], 1, "")
						
					if (sig == defaults.touch):
						print("Введи индекс песни: ", end=' ')
						sindex = dialogcontrol.getanswer("Индекс это число! Введи индекс песни: ", defaults.answers, 1)
						index = int(sindex)
						dialogcontrol.makecontrolfile(touchfile[0], 1, index)
						
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
			dialogcontrol.findandplay(files, command[1], memfile, freq, scriptfilename, transmitter, SOXPIDfilename, duration)
	
	if (command[0] == defaults.mem):
		memory = dialogcontrol.listmemory(memfile[0])
		if memory != False:
			index = dialogcontrol.askforindex("Введи индекс песни: ")
			dialogcontrol.playproc(memory, freq[0], scriptfilename[0], transmitter[0], SOXPIDfilename[0], duration, index, 2)
	
	if (command[0] == defaults.list):
		dialogcontrol.listmemory(memfile[0])

fmcontrol.killwave(SOXPIDfilename[0])