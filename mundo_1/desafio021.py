# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame # importa esse módulo de criação de jogos (jogos têm música)
pygame.init()
pygame.mixer.music.load('musica-exemplo.mp3')
pygame.mixer.music.play()
pygame.event.wait()