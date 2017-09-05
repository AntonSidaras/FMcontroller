# -*- coding: utf-8 -*-
defaultmusicdirs = ["/home/pi/g30kv90/Music"]
configuration = "service/config.txt"
keywords = ["[music]","[output]"]

parameters = ["PlayScript","SoxPidFilename", "KillFile",
"NextFile", "PrevFile", "TouchFile", "MemoryFile", "PlaylistFile",
"Frequency", "PlaylistScript", "TunerScript", "Duration", "Extention", 
"Shuffle", "Transmitter", "KillTunerFile"]

music = keywords[0]
output = keywords[1]
PlayScript = parameters[0]
SoxPidFilename = parameters[1]
KillFile = parameters[2]
NextFile = parameters[3]
PrevFile = parameters[4]
TouchFile = parameters[5]
MemoryFile = parameters[6]
PlaylistFile = parameters[7]
Frequency = parameters[8]
PlaylistScript = parameters[9]
TunerScript = parameters[10]
Duration = parameters[11]
Extention = parameters[12]
Shuffle = parameters[13]
Transmitter = parameters[14]
KillTunerFile = parameters[15]

singlecommands = ("exit", "renew", "stop", "mem", "list")
multiplecommands = ("play", "playlist")
answers = ("y", "n", "д", "н", "y+", "д+")
plsignals = ("kill", "next", "prev", "leave", "touch")

exit = singlecommands[0]
renew = singlecommands[1]
stop = singlecommands[2]
mem = singlecommands[3]
list = singlecommands[4]

play = multiplecommands[0]
playlist = multiplecommands[1]

yes = answers[0]
no = answers[1]
yesrus = answers[2]
norus = answers[3]
yesplus = answers[4]
yesrusplus = answers[5]

kill = plsignals[0]
next = plsignals[1]
previous = plsignals[2]
leave = plsignals[3]
touch = plsignals[4]

