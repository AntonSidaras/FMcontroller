# -*- coding: utf-8 -*-
import os
import subprocess
import time

from auxiliary import defaults
from auxiliary import foldbuilder
from auxiliary import fmcontrol

def checkdefaults():
	if os.path.exists(defaults.Sigfiles) == False:
		os.mkdir(defaults.Sigfiles)
		
	if os.path.exists(defaults.Service) == False:
		os.mkdir(defaults.Service)
		
	if os.path.exists(defaults.configuration) == False:
		print("Файл конфигурации не существует")
		return False
		
	if os.path.exists(defaults.Transmitter) == False:
		print("Скрипт передатчика не существует")
		return False
		
	for music in defaults.defaultmusicdirs:
		if os.path.exists(music) == False:
			print("Список музыкальных папок по-умолчанию содержит несуществующие пути")
			return False
	
	return True

def askforindex(hint):
	print(hint, end=' ')
	sindex = getanswer("Индекс это число! " + hint, defaults.answers, 1)
	return int(sindex)

def listmemory(memfile):
	if os.path.exists(memfile) == True:
		memory = (open(memfile,'r').read()).split("\n")
	else:
		return False
		
	if len(memory) == 0:
		print("Память пуста!")
		return False
	else:
		memoryWI = findfileinlist(memory, "", True)
		print("Вот что было в памяти")
		printfounded(memoryWI)
		return memory

def returnfilebyidwcheck(id, filelist):
	if  0 <= id < len(filelist):
		if os.path.exists(filelist[id]) == True:
			return filelist[id]
		else:
			return -1
	else:
		return -1

def findfileinlist(filelist, fragmentoffilename, numericlist):
	listfind = []
	index = -1
	if fragmentoffilename == "":
		for elem in filelist:
			mystr = elem
			mystr = mystr.lower()
			if numericlist == True:
				index = index + 1
				indstr = str(index) + " - " + elem
				listfind.append(indstr)
			else:
				listfind.append(elem)
		return listfind
		
	for elem in filelist:
		mystr = elem
		mystr = mystr.lower()
		if mystr.find(fragmentoffilename.lower()) != -1:
			if numericlist == True:
				index = index + 1
				indstr = str(index) + " - " + elem
				listfind.append(indstr)
			else:
				listfind.append(elem)
				
	return listfind
	
def makecontrolfile(filename, delay, info):
	f = open(filename, "w")
	if info != "":
		f.write(str(info))
	f.close()
	time.sleep(delay)

def getanswer(hint, answ, selector):
	if selector == 0:
		answer = ""
		while (answer not in answ):
			answer = str(input())
			if (answer not in answ):
				print(hint, end=' ')
		return answer
	if selector == 1:
		sindex = ""
		while (sindex.isdigit() == False):
			sindex = str(input())
			if (sindex.isdigit() == False):
				print(hint, end = ' ')
		return sindex

def printfounded(founded):
	for f in founded:
		print(f)
		
def playproc(foundedfilesNI, frequency, index, duration, sleeptime):
	mtp = returnfilebyidwcheck(index, foundedfilesNI)
	if mtp != -1:
		fmcontrol.killwave()
		time.sleep(sleeptime)
		p = fmcontrol.starttransmit(mtp, frequency)
		if duration != 0:
			time.sleep(duration)
			fmcontrol.stoptransmit(p)
	else:
		print("Музыкальный файл не существует или индекс неверен")
		
def findandplay(files, music, frequency, duration):
	foundedfilesWI = findfileinlist(files, music, True)
	foundedfilesNI = findfileinlist(files, music, False)
	if (len(foundedfilesWI) != 0):
		print("Вот что мне удалось найти по запросу", music)
		printfounded(foundedfilesWI)
		print("Будем проигрывать что-либо среди найденного? y(+)/n д(+)/н:", end=' ')
	else:
		print("Ничего не найдено по запросу", music)
		return False
		
	answer = getanswer("Ответь правильно! y(+)/n д(+)/н:", defaults.answers, 0)
				
	if (answer == defaults.no or answer == defaults.norus):
		return False
	else:
		if (answer == defaults.yesplus or answer == defaults.yesrusplus):
			foldbuilder.printtree(foundedfilesNI, defaults.MemoryFile)
		index = askforindex("Введи индекс песни: ")
		playproc(foundedfilesNI, frequency, index, duration, 2)
		return True
		
def playlistfindandplay(dirs, music):
	foundeddirsWI = findfileinlist(dirs, music, True)
	foundeddirsNI = findfileinlist(dirs, music, False)
	
	if (len(foundeddirsWI) != 0):
		print("Вот что мне удалось найти")
		printfounded(foundeddirsWI)
		print("Будем загружать плейлист? y(+)/n д(+)/н:", end=' ')
	else:
		print("Ничего не найдено по запросу", music)
		return False
	
	answer = getanswer("Ответь правильно! y(+)/n д(+)/н:", defaults.answers, 0)
				
	if (answer == defaults.no or answer == defaults.norus):
		return False
	else:
		if music == "":
			index = askforindex("Введи индекс плейлиста: ")
			playlistfiles = foldbuilder.getfilteredfilesdirslist([dirs[index]], ["mp3"])
			foldbuilder.printtree(playlistfiles, defaults.PlaylistFile)
			print("Играю плейлист: ")
			print(open(defaults.PlaylistFile,'r').read())
		else:
			foldbuilder.printtree(foundeddirsNI, defaults.PlaylistFile)
			playlistfiles = foundeddirsNI
			print("Играю плейлист")
		
		if (answer == defaults.yesplus or answer == defaults.yesrusplus):
			foldbuilder.printtree(playlistfiles, defaults.MemoryFile)
			
		print("Плейлист составлен и выгружен")
		p = subprocess.Popen("python3 " + defaults.PlaylistScript, shell = True)
		return playlistfiles