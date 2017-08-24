import pygame
import pyganim

class Player:
    State=''
    def __init__(self,screen,x,y):
        self.screen=screen
        self.x=x
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
        self.PlayerStay.blit(self.screen, (x,y))

        rectsStartFlyLeft = [(39, 1635, 135, 120),
                 (165, 1635, 135, 120),        
                 (312, 1635, 140, 120),
                 (468, 1635, 190, 110),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rectsStartFlyLeft)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.PlayerStartFlyLeft = pyganim.PygAnimation(frames,loop=False)
        self.PlayerStartFlyLeft.blit(self.screen,(x,y))

        rectsFlyLeft = [(676, 1635, 206, 117),
                       ( 896, 1635, 205, 89),        
                       (1112, 1635, 202, 90),
                       (1329,1635, 195, 113),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rectsFlyLeft)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.PlayerFlyLeft = pyganim.PygAnimation(frames)
        self.PlayerFlyLeft.blit(self.screen,(x,y))

        rectsStopFlyLeft = [(  39, 1635, 135, 120),
                 (165, 1635, 135, 120),        
                 (312, 1635, 140, 120),
                 (468, 1635, 190, 110),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rectsStopFlyLeft)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.PlayerStopFlyLeft = pyganim.PygAnimation(frames,loop=False)
        self.PlayerStopFlyLeft.blit(self.screen,(x,y))


    def draw(self,x,y):
        self.x=x
        self.y=y
        self.PlayerStay.blit(self.screen, (x,y))
        self.PlayerFlyLeft.blit(self.screen,(x,y))
        self.PlayerStartFlyLeft.blit(self.screen,(x,y))
        self.PlayerStopFlyLeft.blit(self.screen,(x,y))

    def stopAll(self):
        if self.PlayerStay._state!=pyganim.STOPPED:
            self.PlayerStay.stop()
        if self.PlayerFlyLeft._state!=pyganim.STOPPED:
            self.PlayerFlyLeft.stop()
        if self.PlayerStartFlyLeft._state!=pyganim.STOPPED:
            self.PlayerStartFlyLeft.stop()
        if self.PlayerStopFlyLeft._state!=pyganim.STOPPED:
            self.PlayerStopFlyLeft.stop()
