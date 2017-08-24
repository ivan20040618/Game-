# trex image from Wyverii on http://opengameart.org/content/unsealed-terrex

import sys
import os
sys.path.append(os.path.abspath('..'))
import pygame
from pygame.locals import *
import pyganim

import time
import threading
SimbaX=10
SimbaY=365
Keep=True

def SimbaMove():
	global SimbaX
	while Keep:
#	Simbax=SimbaX+40
		if	SimbaX>=10 and SimbaX<=550
			dinoAnim.play() # there is also a pause() and stop() method
			dinoAnim1.pause()
			SimbaX=SimbaX+40# there is also a pause() and stop() method
			time.sleep(0.2)
		if SimbaX<=560:
			dinoAnim.pause() # there is also a pause() and stop() method
			dinoAnim1.play()
#	SimbaX=SimbaX-40# there is also a pause() and stop() method
			time.sleep(0.2)
			
		print SimbaX

SimProc=threading.Thread(target=SimbaMove)


pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Sprite Sheet Demo')
sleft1 =	[(480, 0, 115, 56),
         (360, 0,115, 56),
         (240, 0, 115, 56),
         (120, 0, 115, 56),
         (0, 0, 115, 56),]


right =	 [(0, 0, 115, 56),
         (120, 0,115, 56),
         (240, 0, 115, 56),
         (360, 0, 115, 56),
         (480, 0, 115, 56),]

 

allImages1 = pyganim.getImagesFromSpriteSheet('Simba1.png',rects=sleft1)
frames1 = list(zip(allImages1, [100] * len(allImages1)))

dinoAnim1 = pyganim.PygAnimation(frames1)
dinoAnim1.play()

allImages = pyganim.getImagesFromSpriteSheet('Simba.png', rects=right)
frames = list(zip(allImages, [100] * len(allImages)))

dinoAnim = pyganim.PygAnimation(frames)
dinoAnim.play() # there is also a pause() and stop() method

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)
SimProc.start()
while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			Keep=False
			pygame.quit()
			sys.exit()

    dinoAnim.blit(windowSurface, (SimbaX,SimbaY))

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.
