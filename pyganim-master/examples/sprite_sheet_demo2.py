# trex image from Wyverii on http://opengameart.org/content/unsealed-terrex

import sys
import os
sys.path.append(os.path.abspath('..'))
import pygame
from pygame.locals import *
import pyganim
import time

pygame.init()

# set up the window
screen = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Sprite Sheet Demo')

# create the animation objects
rects = [(1532, 1635,165 , 120),
         (1708, 1635, 170, 120),        
         (1112, 1635, 156, 126),
         (1898,1635, 155, 113),
         (2066, 1635, 118, 123),
        # (593, 1635, 115, 116),
        # (703, 1635, 115, 116),
        # (816, 1635, 115, 116),
#
        ]

allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
frames = list(zip(allImages, [100] * len(allImages)))

dinoAnim = pyganim.PygAnimation(frames,loop=True)

#time.sleep(1)
 
dinoAnim.play() # there is also a pause=() and stop() method

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)
while True:
    screen.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    dinoAnim.blit(screen, (100, 50))

    pygame.display.update()
    if dinoAnim._state!=pyganim.STOPPED:
        print "STOP"
    mainClock.tick(60) # Feel free to experiment with any FPS setting.
