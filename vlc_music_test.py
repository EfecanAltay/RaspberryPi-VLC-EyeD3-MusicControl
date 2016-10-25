# -*- coding: utf-8 -*-

import vlc_music as player

player.updateMusicList()
player.showMusicList()

index = raw_input("Müzik Şeçiniz : ")
player.playInList(int(index))
while(1):
 status = raw_input("pause : p ,play : c ,quit : q \n Seçim :")
 if(status == "p"):
  player.pauseMusic()
 elif(status == "c"):
  player.playInList(int(index))
 elif(status == "q"):
  player.stopMusic()
  player.showMusicList()
  index = raw_input("Müzik Şeçiniz : ")
  player.playInList(int(index))
