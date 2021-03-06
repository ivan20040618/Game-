# -*- coding: utf-8 -*-
import pyganim 
import pygame 

class Bot:
    width=100
    height=120
    NoDie=1
    def __init__(self,screen,x,y,bgmap):
        self.Die=pygame.mixer.Sound("./ogg/Die2.ogg")
        self.bgmap=bgmap
        self.screen=screen
        self.oldx=x
        self.oldy=y
        self.x=x
        self.y=y


        rects = [(23,945, 95, 132),
                (150, 945, 95, 125),        
                (307, 945, 55, 136),
                (464, 945, 155, 135),
                (620, 945, 94, 87),
                (758, 945, 88, 149),]
        allImages = pyganim.getImagesFromSpriteSheet('skelet.png', rects=rects)
        frames = list(zip(allImages, [300] * len(allImages)))
        self.SkeletDie= pyganim.PygAnimation(frames,loop=False)
        
        rects = [(0, 0, 94, 125),
                (101, 0, 94, 145),        
                (213, 0, 94, 150),
                (335, 0, 94, 153)]

        allImages = pyganim.getImagesFromSpriteSheet('skelet.png', rects=rects)
        frames = list(zip(allImages, [600] * len(allImages)))
        self.SkeletStay = pyganim.PygAnimation(frames,loop=True)
        self.SkeletStay.play()     
        
    def enemy(self,x,y):
        if self.NoDie==1:
            pygame.draw.rect(self.bgmap,(255,0,0),(x+25,y+25,self.width-35,self.height-20))
        if self.NoDie==0:
            
            self.SkeletStay.stop()
            self.SkeletDie.play()
            self.Die.play()
            pygame.draw.rect(self.bgmap,(255,255,255),(x+15,y+25,self.width-15,self.height-20))
            #self.SkeletDie.blit(self.screen,(x,y))
            self.NoDie=2

        if self.SkeletDie.isFinished()==False:
            self.SkeletDie.blit(self.screen,(x,y))
        if self.SkeletStay.isFinished()==False:
            self.SkeletStay.blit(self.screen,(x,y))
        
