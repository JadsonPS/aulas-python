""" 
    Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
 """

import pygame

pygame.init()
#pygame.mixer.music.load('Python\scripts-python\desafios\desafio21mp4.mp4')
#pygame.mixer.music.load('desafio21mp4.mp4')
pygame.mixer.music.load('videoplayback.m4a')
pygame.mixer.music.play()
pygame.event.wait()