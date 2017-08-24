import sys
import os
import pygame 
import math 
import pyganim
from Player import *

size=(1200,700)
screen = pygame.display.set_mode(size)

pygame.init()
clock = pygame.time.Clock()
     
done=False
bg=pygame.image.load('grees.png').convert()	
Player0=Player(screen,500,200)

JOY_EXIST=False
SPEED=3
#screen.fill((0,255,0))
#screen.blit(bg,(0,0))
#pygame.display.flip()

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
