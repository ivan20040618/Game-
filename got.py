#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import pygame 
import math 
import pyganim
from Player import *#импорт библеотек 
from bot import *

size=(1200,700)#размер окна 
screen = pygame.display.set_mode(size)#создание окна

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.music.load('./ogg/background3.ogg')
pygame.mixer.music.play()
done=False
bgmap=pygame.image.load('map.png').convert()#приграды карты
bg=pygame.image.load('grees.png').convert()#карта	
Player0=Player(screen,445,500,bgmap)#1080,125

Skeleton=[]
Skeleton.append(Bot(screen,225,500,bgmap))
Skeleton.append(Bot(screen,540,190,bgmap))
Skeleton.append(Bot(screen,340,200,bgmap))
Skeleton.append(Bot(screen,540,230,bgmap))
Skeleton.append(Bot(screen,40,260,bgmap))

JOY_EXIST=False
SPEED=5

if  pygame.joystick.get_count()!=0:
    joy0 = pygame.joystick.Joystick(0)
    joy0.init()
    cb=joy0.get_numbuttons()
    JOY_EXIST= True 
else:	
    print "Connect joystick!"
x=y=0

while done==False:
    for event in pygame.event.get():#оброботка событей
        if event.type == pygame.QUIT:
                    done=True
        if event.type == pygame.KEYDOWN:#оброботка событей когда клавиша опущена
            if event.key == pygame.K_LEFT:#клавиша влево
                
                x=-1#двежение влево
                Player0.stopAll()
                Player0.StartLeftFly.play()#анимация влево
                
                Player0.State='StartLeftFly'#состояние игрока
            if event.key == pygame.K_b:#клавиша b (атака)

                for i in range(len(Skeleton)):
                    
                    if Player0.Rect.colliderect(pygame.Rect(Skeleton[i].x,Skeleton[i].y,Skeleton[i].width,Skeleton[i].height)):
                        
                        if Skeleton[i].NoDie==1:
                            Skeleton[i].NoDie=0

                Player0.stopAll()#остновка всех анимаций
                if  Player0.State.find('Right')!=-1:#cостояние игрока
                    Player0.State='FireRight'#состояние игрока
                    Player0.FireRight.play()#проигравание анимаций
                if  Player0.State.find('Left')!=-1:#состояние игрока
                    Player0.State='FireLeft'#состояние игрока
                    Player0.FireLeft.play()#проигрование анимаций
                    
            if event.key == pygame.K_RIGHT:#клавиша вправо
                x=1#двежение вправо
                Player0.stopAll()#остновка всех анимаций
                Player0.StartRightFly.play()
                Player0.State='StartRightFly'
            if event.key == pygame.K_UP:
                if Player0.State.find('Left')!=-1:
                    Player0.stopAll()#остновка всех анимаций
                    Player0.StartLeftFly.play()
                    Player0.State='StartLeftFly'
                if Player0.State.find('Right')!=-1:
                    Player0.stopAll()#остновка всех анимаций
                    Player0.StartRightFly.play()
                    Player0.State='StartRightFly'
                y=-1
            if event.key == pygame.K_DOWN:
                if Player0.State.find('Left')!=-1:
                    Player0.stopAll()#остновка всех анимаций
                    Player0.StartLeftFly.play()
                    Player0.State='StartLeftFly'
                if Player0.State.find('Right')!=-1:
                    Player0.stopAll()#остновка всех анимаций
                    Player0.StartRightFly.play()
                    Player0.State='StartRightFly'
                y=1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                x=0
                if y==0:
                    
                    Player0.stopAll()#остновка всех анимаций
                    Player0.StopLeftFly.play()
                    Player0.State='StopLeftFly'
            if event.key == pygame.K_b:
                Player0.stopAll()
                if Player0.State=='FireLeft':
                    Player0.StayLeft.play()
                    Player0.State='StayLeft'
                if Player0.State=='FireRight':
                    Player0.StayRight.play()
                    Player0.State='StayRight'
                
            if event.key == pygame.K_RIGHT:
                x=0
                if y==0:
                
                    Player0.stopAll()#остновка всех анимаций
                    Player0.StopRightFly.play()
                    Player0.State='StopRightFly'
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y=0
                if x==0:
                
                    if Player0.State.find('Left')!=-1:
                        Player0.stopAll()#остновка всех анимаций
                        Player0.StopLeftFly.play()
                        
                        Player0.State='StopLeftFly'
                    if Player0.State.find('Right')!=-1:
                        Player0.stopAll()#остновка всех анимаций
                        Player0.StopRightFly.play()
                        Player0.State='StopRightFly'

    if JOY_EXIST:
        x=joy0.get_axis(0)
        y=joy0.get_axis(1)

    if abs(x)>0.5:
        Player0.x+=math.copysign(SPEED,x)
    if abs(y)>0.5:
        Player0.y+=math.copysign(SPEED,y)

    if (Player0.StartLeftFly.isFinished()==True) and (Player0.State=='StartLeftFly'):
        Player0.stopAll()#остновка всех анимаций
        Player0.LeftFly.play()
        Player0.State='LeftFly'
    if (Player0.StopLeftFly.isFinished()==True) and (Player0.State=='StopLeftFly'):
        Player0.stopAll()#остновка всех анимаций
        Player0.StayLeft.play()
        Player0.State="StayLeft"

    if (Player0.StartRightFly.isFinished()==True) and (Player0.State=='StartRightFly'):
        Player0.stopAll()#остновка всех анимаций
        Player0.RightFly.play()
        Player0.State='RightFly'
    if (Player0.StopRightFly.isFinished()==True) and (Player0.State=='StopRightFly'):
        Player0.stopAll()#остновка всех анимаций
        Player0.StayRight.play()
        Player0.State="StayRight"

    screen.blit(bg,(0,0))
    for i in range(len(Skeleton)):
        Skeleton[i].enemy(Skeleton[i].x,Skeleton[i].y,bgmap)
    Player0.draw(Player0.x,Player0.y)
    pygame.display.flip()
    clock.tick(60)
    
