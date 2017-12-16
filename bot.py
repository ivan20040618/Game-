import pygame 
import pyganim 

class Bot:
    def __init__(self,screen,x,y,bgmap):
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
        frames = list(zip(allImages, [100] * len(allImages)))
        self.SkeletDie= pyganim.PygAnimation(frames)
        #self.SkeletDie.play()
        
        rects = [(0, 0, 90, 125),
                (101, 0, 90, 145),        
                (210, 0, 92, 150),
                (325, 0, 94, 153),]

        allImages = pyganim.getImagesFromSpriteSheet('skelet.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.SkeletStay = pyganim.PygAnimation(frames,loop=True)
        self.SkeletStay.play()  
    


