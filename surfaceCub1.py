import sys
import os
import pygame 
import math 
import pyganim

size=(1200,700)
screen = pygame.display.set_mode(size)

class Player:
    State=''
    def __init__(self,x,y):
        self.x=x
        self.state="Stay"
        self.y=y
        rectsStay = [(34, 18, 115, 116),
        (147, 18, 115, 116),        
        (262, 18, 115, 116),
        (370, 18, 115, 116),
        (482, 18, 115, 116),
        (593, 18, 115, 116),
        (703, 18, 115, 116),
        (816, 18, 115, 116),]
        
        allImages = pyganim.getImagesFromSpriteSheet('AD.png', rects=rectsStay)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.PlayerStay= pyganim.PygAnimation(frames)
        self.PlayerStay.play() 
        self.PlayerStay.blit(screen, (x,y))

        rectsStartFlyLeft = [(39, 1635, 135, 120),
                 (165, 1635, 135, 120),        
                 (312, 1635, 140, 120),
                 (468, 1635, 190, 110),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rectsStartFlyLeft)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.PlayerStartFlyLeft = pyganim.PygAnimation(frames,loop=False)
        self.PlayerStartFlyLeft.blit(screen,(x,y))

        rectsFlyLeft = [(676, 1635, 206, 117),
                       ( 896, 1635, 205, 89),        
                       (1112, 1635, 202, 90),
                       (1329,1635, 195, 113),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rectsFlyLeft)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.PlayerFlyLeft = pyganim.PygAnimation(frames)
        self.PlayerFlyLeft.blit(screen,(x,y))

        rectsStopFlyLeft = [(  39, 1635, 135, 120),
                 (165, 1635, 135, 120),        
                 (312, 1635, 140, 120),
                 (468, 1635, 190, 110),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rectsStopFlyLeft)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.PlayerStopFlyLeft = pyganim.PygAnimation(frames,loop=False)
        self.PlayerStopFlyLeft.blit(screen,(x,y))


    def draw(self,x,y):
        self.x=x
        self.y=y
       # Player0.PlayerFlyLeft.play()
        self.PlayerStay.blit(screen, (x,y))
        self.PlayerFlyLeft.blit(screen,(x,y))
        self.PlayerStartFlyLeft.blit(screen,(x,y))
        self.PlayerStopFlyLeft.blit(screen,(x,y))

    def stopAll(self):
        if self.PlayerStay._state!=pyganim.STOPPED:
            self.PlayerStay.stop()
        if self.PlayerFlyLeft._state!=pyganim.STOPPED:
            self.PlayerFlyLeft.stop()
        if self.PlayerStartFlyLeft._state!=pyganim.STOPPED:
            self.PlayerStartFlyLeft.stop()
        if self.PlayerStopFlyLeft._state!=pyganim.STOPPED:
            self.PlayerStopFlyLeft.stop()
pygame.init()
clock = pygame.time.Clock()
     
done=False
bg=pygame.image.load('grees.png').convert()	
Player0=Player(500,200,)

JOY_EXIST=False
SPEED=3
screen.fill((0,255,0))
screen.blit(bg,(0,0))
pygame.display.flip()

if  pygame.joystick.get_count()!=0:
    joy0 = pygame.joystick.Joystick(0)
    joy0.init()
    cb=joy0.get_numbuttons()
    #print cb
    JOY_EXIST= True 
else:	
    print "Connect joystick!"
#	pygame.quit()
#	sys.exit()
x=y=0

while done==False:
    #x=y=0
    #print bg.get_at((int(Player0.x),int(Player0.y))) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    done=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print "LEFT"
                x=-1
                Player0.stopAll()
                Player0.PlayerStartFlyLeft.play()
                Player0.State='StartLeftFly'
            if event.key == pygame.K_RIGHT:
                x=1
            if event.key == pygame.K_UP:
                y=-1
            if event.key == pygame.K_DOWN:
                y=1
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x=0
                Player0.stopAll()
                Player0.PlayerStopFlyLeft.play()
                Player0.State='StopLeftFly'
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y=0
    if JOY_EXIST:
        x=joy0.get_axis(0)
        y=joy0.get_axis(1)

    if abs(x)>0.5:
        Player0.x+=math.copysign(SPEED,x)
    if abs(y)>0.5:
        Player0.y+=math.copysign(SPEED,y)
    #print Player0.PlayerStartFlyLeft._state,Player0.PlayerStartFlyLeft._loop,  Player0.StartFlyLeft
    if (Player0.PlayerStartFlyLeft.isFinished()==True) and (Player0.State=='StartLeftFly'):
        Player0.stopAll()
        Player0.PlayerFlyLeft.play()
        Player0.State='LeftFly'
    if (Player0.PlayerStopFlyLeft.isFinished()==True) and (Player0.State=='StopLeftFly'):
            Player0.stopAll()
            Player0.PlayerStay.play()
            Player0.State="LeftStay"

    screen.blit(bg,(0,0))
   # screen.blit(Player0.Surface,(Player0.x,Player0.y))
    Player0.draw(Player0.x,Player0.y)
    pygame.display.flip()
#	for i in range(cb):
#		print str(i)+" "+str(joy0.get_button(i))
#	print joy0.get_axis(0),joy0.get_axis(1), joy0.get_axis(2), joy0.get_axis(3)
    clock.tick(60)
bg.fill((0,255,0))

