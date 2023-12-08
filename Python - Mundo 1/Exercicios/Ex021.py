'''
Faça um porgram me python que abra e 
reporduza o aúdio de um arquivo em MP3
'''

import pygame

pygame.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

