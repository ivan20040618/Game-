#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import pygame 
import math 
import pyganim
import time
from Player import *#импорт библеотек 
from bot import *

size=(1200,700)#размер окна 
screen = pygame.display.set_mode(size)#создание окна

pygame.init()
clock = pygame.time.Clock()
#pygame.mixer.music.play()
done=False
bgmap=pygame.image.load('map.png').convert()#приграды карты
bg=pygame.image.load('grees.png').convert()#карта	
Player0=Player(screen,445,400,bgmap)#1080,125

pygame.mixer.music.load('./ogg/background.ogg')
pygame.mixer.music.play()
zastavka=pygame.image.load('zastavka.png').convert()
screen.blit(zastavka,(0,0))
pygame.display.flip()
pausa=False

while pausa==False:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            pausa=True   
Skeleton=[]
Skeleton.append(Bot(screen,225,500,bgmap))
Skeleton.append(Bot(screen,540,190,bgmap))
Skeleton.append(Bot(screen,340,200,bgmap))
Skeleton.append(Bot(screen,540,230,bgmap))
Skeleton.append(Bot(screen,40,260,bgmap))

JOY_EXIST=False
JOY_DOWN=False
JOY_SENSITIVE=0.9
XJ=YJ=0
SPEED=5

if  pygame.joystick.get_count()!=0:
    joy0 = pygame.joystick.Joystick(0)
    joy0.init()
    cb=joy0.get_numbuttons()
    JOY_EXIST= True 
else:	
    print "Connect joystick!"
x=y=0
pygame.mixer.music.load('./ogg/background3.ogg')
event=None
while done==False:
#Этот блок позволяет узнать какая ось была отпущена
    if JOY_EXIST and JOY_DOWN:
        nx=joy0.get_axis(0)
        ny=joy0.get_axis(1)
        if abs(nx)<JOY_SENSITIVE and abs(ny)<JOY_SENSITIVE:
            if XJ<=-JOY_SENSITIVE:
               pygame.event.post(pygame.event.Event(pygame.KEYUP,key=pygame.K_LEFT))
            if XJ>=JOY_SENSITIVE:
                pygame.event.post(pygame.event.Event(pygame.KEYUP,key=pygame.K_RIGHT))
            if YJ<=-JOY_SENSITIVE:
               pygame.event.post(pygame.event.Event(pygame.KEYUP,key=pygame.K_UP))
            if YJ>=JOY_SENSITIVE:
                pygame.event.post(pygame.event.Event(pygame.KEYUP,key=pygame.K_DOWN))
            XJ=YJ=0
            JOY_DOWN=False
            
#Если музыка закончилась начинаем сначала

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
#Цикл приема сообщений
    for event in pygame.event.get():#оброботка событей
        if event.type == pygame.QUIT:
                    done=True
#Joy button to key
        if event.type == pygame.JOYBUTTONDOWN:
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_b))
        if event.type == pygame.JOYBUTTONUP:
            pygame.event.post(pygame.event.Event(pygame.KEYUP,key=pygame.K_b))
#Joy axis to key
        if event.type == pygame.JOYAXISMOTION :
           # print event.axis,event.value
            if event.axis==0:
                if event.value<-JOY_SENSITIVE:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_LEFT))
                    XJ=event.value
                if event.value>JOY_SENSITIVE:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_RIGHT))
                    XJ=event.value
            if event.axis==1:
                if event.value<-JOY_SENSITIVE:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_UP))
                    YJ=event.value
                if event.value>JOY_SENSITIVE:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_DOWN))
                    YJ=event.value
            JOY_DOWN=True

        if event.type != pygame.KEYDOWN and event.type != pygame.KEYUP:
           # print "CONTINUE"
            continue
        print "KEY_DOWN"

        if event.type == pygame.KEYDOWN:#оброботка событей когда клавиша нажата 
            if event.key == pygame.K_ESCAPE:
                done=True

            if event.key == pygame.K_LEFT:#клавиша влево
                x=-1#двежение влево
                Player0.stopAll()
                Player0.StartLeftFly.play()#анимация влево
                Player0.State='StartLeftFly'#состояние игрока

            if event.key == pygame.K_b:#клавиша b (атака)
                Player0.stopAll()#остновка всех анимаций
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

        if event.type == pygame.KEYUP:#Обработка события когда клавиша отпущена
            print "KEY_UP"
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
        Skeleton[i].enemy(Skeleton[i].x,Skeleton[i].y)
    Player0.draw(Player0.x,Player0.y)
    pygame.display.flip()
    clock.tick(60)
    #x=y=0


end=pygame.image.load('end.png').convert()
screen.blit(end,(0,0))
pygame.display.flip()
pausa=False
pygame.mixer.music.load('./ogg/Poxoronay.ogg')
pygame.mixer.music.play()
while pausa==False:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            pausa=True
            clock.tick(1)

