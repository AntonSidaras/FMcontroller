# -*- coding: utf-8 -*-
import signal
import subprocess
import time
import os

from auxiliary import defaults
from auxiliary import foldbuilder

def makeshscript(file, frequency):
	fst = 'sox -q -t mp3 '
	txt = '\"'
	fst = fst + txt
	lst = ' -t wav -  | sudo '
	lst = lst + defaults.Transmitter + ' -freq '
	lst = lst + frequency
	lst = lst + ' -audio -'
	lst = txt + lst
	mystr = fst + file + lst
	f = open(defaults.PlayScript,'w')
	f.write(mystr)
	f.close()

def getsoxpidpath():
	f = open(defaults.SoxPidFilename, 'r')
	PID = f.read()
	f.close()
	path = "/proc/" + PID
	return path

def killwave():
	if (os.path.exists(defaults.SoxPidFilename) == False):
		return False
	path = getsoxpidpath()
	if (os.path.exists(path)):
		os.kill(int(path[6:]),signal.SIGKILL)
		return True
	else:
		return False
		
def checkwave():
	if (os.path.exists(defaults.SoxPidFilename) == False):
		return False
	path = getsoxpidpath()
	while (os.path.exists(path) == True):
	
		if (os.path.exists(defaults.KillFile) == True):
			os.remove(defaults.KillFile)
			return defaults.kill
			
		if (os.path.exists(defaults.NextFile) == True):
			os.remove(defaults.NextFile)
			return defaults.next
		
		if (os.path.exists(defaults.PrevFile) == True):
			os.remove(defaults.PrevFile)
			return defaults.previous
			
		if (os.path.exists(defaults.TouchFile) == True):
			index = open(defaults.TouchFile).read()
			os.remove(defaults.TouchFile)
			return defaults.touch + index
			
		time.sleep(1)
		
	return False

def stoptransmit(p):
    killwave()
    p.wait()

def starttransmit(musicfile, frequency):
	
	makeshscript(musicfile, frequency)
	cmd = "bash " + defaults.PlayScript
	p = subprocess.Popen(cmd, shell = True)
	time.sleep(2)
	strPID = subprocess.check_output(["pidof", "sox"]).decode("UTF-8")
	intPID = int(strPID[:5])
	f = open(defaults.SoxPidFilename, 'w')
	f.write(str(intPID))
	f.close()
		
	return p
