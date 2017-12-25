import pygame
pygame.init()
Fire=pygame.mixer.Sound("./mp3/Fire.mp3")
ch=Fire.play(loops=5)
ch.set_volume(1.0, 1.0)
