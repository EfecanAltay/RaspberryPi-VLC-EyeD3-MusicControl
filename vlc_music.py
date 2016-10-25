# -*- coding: utf-8 -*-
"""
 @Name = Muzik listeleme ve oynatma modülü 

 @auther=Efecan
 @version=0.0.1
 @system= raspberry_pi_2

 @python_version = 2

 Not:VLC ve Eyed3 programı gereklidir!!!
"""
import eyed3 as info
import subprocess as run

global muzikKonumum
muzikKonumum = "../../Müziklerim/"

list = "none"


def setLocate(locate):
 muzikKonumum = (locate).strip()

def updateMusicList():
 global list
 list = run.check_output("ls "+muzikKonumum ,shell=True).splitlines();

def showMusicList():
 updateMusicList()
 for x in range(0,len(list)):
  print  str(x+1) + " . : " + list[x]

def playInList(index):
 if(list[index-1]):
  music = (muzikKonumum + list[0].strip()).strip()
  audiofile = info.load(music)
  print str(audiofile.tag.album) + " Çalıyor..."
  status = run.Popen(["cvlc", music])
 else:
  print "liste güncel değil veya index numarası yanlış!!"

def stopMusic():
 run.Popen(["cvlc","vlc://quit"])

def pauseMusic():
 run.Popen(["cvlc","vlc://pause"])
