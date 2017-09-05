version 1.6.1

[��������]

������ Raspberry Pi: 2B/3
������ �� ����� GPIO 4 ������ �� ����� 20 �� � �� ����� 100 ��
���������� ��������� ������:
os Raspbian
������������� python 3
sudo apt-get install sox
sudo apt-get install libsox-fmt-mp3
sudo apt-get install libsndfile1-dev
https://github.com/ChristopheJacquet/PiFmRds
make makefile (� ����� � PiFmRds)
������������� ������ � fm � �������� � ����� � ���������� ����������

[������ ���������]

http://icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter

sudo python
>>> import PiFm
>>> PiFm.play_sound("sound.wav")

sudo ./pifm left_right.wav 103.3 22050 stereo

# Example command lines
# play an MP3
ffmpeg -i input.mp3 -f s16le -ar 22.05k -ac 1 - | sudo ./pifm -

# Broadcast from a usb microphone (see arecord manual page for config)
arecord -d0 -c2 -f S16_LE -r 22050 -twav -D copy | sudo ./pifm -

sudo ./pifm sound.wav 100.0

aqualung -L "/home/pi/g30kv90/Music/ASP/ASP - Krabat.mp3" | sudo ./home/pi/fm/fm -freq 95.5 -audio -