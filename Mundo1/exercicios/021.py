# toca um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
input("\033[35mPressione Enter para parar...")