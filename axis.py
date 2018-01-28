import sys
import os
import pygame 
import math 
import pyganim
import time
import pygame.display
pygame.init()
pygame.display.init()
pygame.font.init()
JOY_EXIST=False
done=False
joy0 = pygame.joystick.Joystick(0)
joy0.init()
size= (600,300)
font = pygame.font.Font(None, 60)
screen = pygame.display.set_mode(size)
axis1=font.render("text1",0,(55,55,55),(95,95,95))
screen.blit(axis1,(0,0,))

#print joy0.get_name()
#print pygame.joystick.get_count()    

JOY_EXIST= True 
n=1
y=1
while done==False:
    pygame.event.pump()        
    #print joy0.get_axis(0), joy0.get_axis(1)
    if joy0.get_axis(0)>=0.1:
        n-=1
        y=2
        if n==0:
            axis1=font.render("text2",0,(55,55,55),(95,95,95))
            screen.blit(axis1,(0,0,))

    if joy0.get_axis(0)==0:
        y-=1
        n=1
    if y==1:
        axis1=font.render("text3",0,(55,55,55),(95,95,95))
        screen.blit(axis1,(0,0,))
    pygame.display.flip()
