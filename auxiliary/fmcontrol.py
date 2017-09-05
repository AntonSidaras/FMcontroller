# -*- coding: utf-8 -*-
import signal
import subprocess
import time
import os

from auxiliary import foldbuilder

def makeshscript(file, freq, transmitter, shfilename):
	fst = 'sox -q -t mp3 '
	txt = '\"'
	fst = fst + txt
	lst = ' -t wav -  | sudo '
	lst = lst + transmitter + ' -freq '
	lst = lst + freq
	lst = lst + ' -audio -'
	lst = txt + lst
	mystr = fst + file + lst
	f = open(shfilename,'w')
	f.write(mystr)
	f.close()

def getsoxpidpath(SOXPIDfilename):
	f = open(SOXPIDfilename, 'r')
	PID = f.read()
	f.close()
	path = "/proc/" + PID
	return path

def killwave(SOXPIDfilename):
	if (os.path.exists(SOXPIDfilename) == False):
		return False
	path = getsoxpidpath(SOXPIDfilename)
	if (os.path.exists(path)):
		os.kill(int(path[6:]),signal.SIGKILL)
		return True
	else:
		return False
		
def checkwave(SOXPIDfilename, killfile, nextfile, prevfile, touchfile, plsignals):
	if (os.path.exists(SOXPIDfilename) == False):
		return False
	path = getsoxpidpath(SOXPIDfilename)
	while (os.path.exists(path) == True):
	
		if (os.path.exists(killfile) == True):
			os.remove(killfile)
			return plsignals[0]
			
		if (os.path.exists(nextfile) == True):
			os.remove(nextfile)
			return plsignals[1]
		
		if (os.path.exists(prevfile) == True):
			os.remove(prevfile)
			return plsignals[2]
			
		if (os.path.exists(touchfile) == True):
			index = open(touchfile).read()
			os.remove(touchfile)
			return plsignals[4] + index
			
		time.sleep(1)
		
	return False

def stoptransmit(p, SOXPIDfilename):
    killwave(SOXPIDfilename)
    p.wait()

def starttransmit(musicfile, freq, transmitter, scriptfilename, SOXPIDfilename):
	
	makeshscript(musicfile, freq, transmitter, scriptfilename)
	cmd = "bash " + scriptfilename
	p = subprocess.Popen(cmd, shell = True)
	time.sleep(2)
	strPID = subprocess.check_output(["pidof", "sox"]).decode("UTF-8")
	intPID = int(strPID[:5])
	f = open(SOXPIDfilename, 'w')
	f.write(str(intPID))
	f.close()
		
	return p
