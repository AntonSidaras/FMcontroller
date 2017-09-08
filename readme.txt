version 1.6.2

[basic]

Raspberry Pi version: 2B/3

Required OS: Raspbian
Required software (some of them you can get with a help of command "apt-get"): 
1. python 3 interpreter
2. sudo apt-get install sox
3. sudo apt-get install libsox-fmt-mp3
4. sudo apt-get install libsndfile1-dev
5. PiFmRds script, you can get it by this link https://github.com/ChristopheJacquet/PiFmRds
There is all information how to make it and run in https://github.com/ChristopheJacquet/PiFmRds

When the preparation is over it's time to edit the config file, before it I recommend to rename PiFmRds script 
to "fm" and place it in "important" directory. You can find config in "important" directory. Simply open it with
a help of text editor. Now, change the values as you like. Note this rules:

There is two main sections in config : [music] and [output]. In section [music] you can add music folder in Unix
format. Each new folder must be added to new line, like this:
[music]
/etc/Music
/ect/NewMusic
/home/username/Music

In section [output] you can just edit existing parameters Frequency, Duration, Shuffle. Here are some
examples how to do it right:

Frequency = 100.5
Duration = 0
Extention = mp3
Shuffle = on

It means that frequency of carrier is 100.5 MHz. Duration = 0 means that songs will be played entirely,
extention = mp3 means that only .mp3 files in your music dirs will be played. 

Attenton! In current version ONLY .mp3 files in your music dirs will be played, DON'T change the Extention value,
be sure that Extention = mp3.

Shuffle = on means that files in your music dirs will be played in random order.

Frequency = 88.7
Duration = 30
Extention = mp3
Shuffle = off

It means that frequency of carrier is 88.7 MHz. Duration = 30 means that songs will be played 30 seconds length,
extention = mp3 means that only .mp3 files in your music dirs will be played. 

Attenton! In current version ONLY .mp3 files in your music dirs will be played, DON'T change the Extention value,
be sure that Extention = mp3.

Shuffle = on means that files in your music dirs will be played in direct lexicographic order.

As a result a config file must be kind of

[music]
/etc/Music
[output]
Frequency = 102.8
Duration = 0
Extention = mp3
Shuffle = on

Now, be shure, that all files, which were downloaded are exist. 
Finally, go to the auxillary folder and open defaults.py with text editor. Change the value of efaultmusicdirs 
variable to your default music directories or leave it, but if your music directories in config file don't not exist 
programm will crash. If you didn't rename PiFmRds script to "fm" and place it in "important" directory change 
the value of Transmitter variable to your path to the PiFmRds script.

Now you can start the script like this:

>> python3 player.py

In main section you can use such commands:
just type the

exit - to quit the programm
renew - to update information from config file
stop - to stop the transmission (valid for play command)
play - find music file you like in your music directories by words that you type, confirm
to continue use founded results (y/д) with rememder in file (y+/д+) or not (n/н), choose one
needed file by typing id number (id will be displayed) and start transmit. 
For example:

main>play bad boys blue

some results:
1 - /etc/Music/bad boys blue - you're woman.mp3
2 - /etc/Music/bad boys blue - pretty young girl.mp3

continue? (y/д, n/н, y+/д+): y+
type id: 1

list - to display files in memory file
mem - to play files from memory, 
For example:

main>mem

some results:
1 - /etc/Music/bad boys blue - you're woman.mp3
2 - /etc/Music/bad boys blue - pretty young girl.mp3
type id: 1

playlist - find music directories you like, confirm to continue use founded results (y/д) with rememder 
in file (y+/д+) or not (n/н) and start transmit. Also ind music files you like in your music directories 
by words that you type, confirm to continue use founded results (y/д) with rememder in file (y+/д+) or not (n/н)
and start transmit. 
For example:

main>playlist bad boys blue

some results:
1- /etc/Music/bad boys blue - you're woman.mp3
2- /etc/Music/bad boys blue - pretty young girl.mp3
continue? (y/д, n/н, y+/д+): y+

Or

main>playlist

some results:
1 - /etc/Music/bonus
2 - /etc/Music/random music
continue? (y/д, n/н, y+/д+): y+
type id: 1

In playlist section you can use such commands:
just type the

next - to get next song
prev - to get previous song
kill - to stop playing playlist
leave - to back in main section

Also you can choose next and previous songs by using signals in GPIO 35 and 37 pins. 
Logical "1" in 35 pin chooses previous song
Logical "1" in 37 pin chooses next song
Choose your own way to chang logical values on pins numer 35 and 37. If you need change
pin numers - edit the 433tuner.py

Note the scripts displays the information in Russian, in next version English version vill be added.