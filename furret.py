# Import libraries
import playsound
import winsound
import time
import os
import pygame

# Set variables
index = 0
images = {}
song_length = 184

# Set cmd size
os.system('mode con:cols=100 lines=40')

# Load ascii to ram
for index in range(0,95):
    ascii_file = 'ascii/' + str(index) + '.txt'
    ascii_image=open(ascii_file,'r')
    #images['index'] = ascii_image.read()
    images[index] = ascii_image.read()
    ascii_image.close()

#Play the song
pygame.mixer.init()
pygame.mixer.music.load('bms.mp3')
pygame.mixer.music.play(999)

while True:
   for index in range(0,95):
      position = (pygame.mixer.music.get_pos()/1000)
      precentage = position * 100 / song_length
      short = "%.1f" % precentage
      dots = '-' * int(precentage/2)
      space = ' '*(50-int(precentage/2))
      print('\n'*100)
      print(
         'Script made by Mattias Tofte'+'\n' +
         f'Progress: {short}%'+'\n' +
         f'[{dots}>{space}]' +
         images[index]
         )
      time.sleep(0.05)