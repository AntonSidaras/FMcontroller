# -*- coding: utf-8 -*-
defaultmusicdirs = ["/home/pi/g30kv90/Music"]
configuration = "important/config.txt"
keywords = ["[music]","[output]"]

parameters = ["Frequency", "Duration", "Extention", "Shuffle"]

music = keywords[0]
output = keywords[1]

Frequency = parameters[0]
Duration = parameters[1]
Extention = parameters[2]
Shuffle = parameters[3]

Sigfiles = "sigfiles"
Service = "service"

Transmitter = "important/./fm"

KillFile = "sigfiles/killfile"
NextFile = "sigfiles/nextfile"
PrevFile = "sigfiles/prevfile"
TouchFile = "sigfiles/touchfile"
KillTunerFile = "sigfiles/tunkill"

PlayScript = "service/./play.sh"
SoxPidFilename = "service/pid"
MemoryFile = "service/mem"
PlaylistFile = "service/playlist"

PlaylistScript = "playlist.py"
TunerScript = "tuner.py"

singlecommands = ("exit", "renew", "stop", "mem", "list", "help")
multiplecommands = ("play", "playlist")
answers = ("y", "n", "д", "н", "y+", "д+")
plsignals = ("kill", "next", "prev", "leave", "touch")

exit = singlecommands[0]
renew = singlecommands[1]
stop = singlecommands[2]
mem = singlecommands[3]
list = singlecommands[4]
help = singlecommands[5]

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