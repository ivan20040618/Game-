import pygame
import pyganim

class Player:
    State=''
    def __init__(self,screen,x,y,bgmap):
        self.bgmap=bgmap
        self.screen=screen
        self.oldx=x
        self.oldy=y
        self.x=x
        self.y=y
        rects = [(34, 18, 115, 116),
        (147, 18, 115, 116),        
        (262, 18, 115, 116),
        (370, 18, 115, 116),
        (482, 18, 115, 116),
        (593, 18, 115, 116),
        (703, 18, 115, 116),
        (816, 18, 115, 116),]
        
        self.State="RightStay"
        allImages = pyganim.getImagesFromSpriteSheet('AD.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.StayRight= pyganim.PygAnimation(frames)
        self.StayRight.play() 
        self.StayRight.blit(self.screen, (x,y))
        
        rects = [(1025,1400, 137, 176),
                (1185, 1400, 175, 184),        
                (1373, 1400, 175, 165),
                (1250, 1225, 155, 155),
                (1420, 1225, 175, 176),
                (1606, 1225, 160, 145),
                (1780,1225, 117, 155),
                (1917,1225, 90, 145),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))


        rects = [(1917,1225, 90, 145)]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))

  
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages,[100] * len(allImages)))
        self.FireRight = pyganim.PygAnimation(frames)
        self.FireRight.blit(self.screen,(x,y))  

        rects = [(38,1200,243,133,),
                 (293,1200,260,135,),
                 (576,1200,250,110,),
                                     ]


        allImages = pyganim.getImagesFromSpriteSheet('ADR.png', rects=rects)
        frames = list(zip(allImages,[100] * len(allImages)))
        self.FireLeft = pyganim.PygAnimation(frames)
        self.FireLeft.blit(self.screen,(x,y))  

        rects = [(2005,1400,190,198,),
                 (1767,1400,220,205,),
                 (1522,1400,220,150,),
                                     ]


        allImages = pyganim.getImagesFromSpriteSheet('ADR.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.FlyFireLeft = pyganim.PygAnimation(frames,loop=True)
        self.FlyFireLeft.blit(self.screen,(x,y))

        rects = [(2080, 18, 115, 115),
                 (1967, 18, 115, 115),       
                 (1852, 18, 115, 115),
                 (1744, 18, 112, 114),
                 (1632 ,18 ,112 ,114),
                 (1521 ,18,112, 114 ),] 
        allImages = pyganim.getImagesFromSpriteSheet('ADR.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.StayLeft = pyganim.PygAnimation(frames,loop=True)
        self.StayLeft.blit(self.screen,(x,y))


        rects = [(35,218, 120,130),
                 (150,218,170,135),        
                 (319,218,185,125),
                 (512,218,175,125),
                                   ]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
	self.StartRightFly = pyganim.PygAnimation(frames,loop=False)
	self.StartRightFly.blit(self.screen,(x,y))
        

	rects = [(690, 218, 180 ,115),
         (900, 218, 205, 125),
         (1121, 218, 200, 115),
         (1348, 218, 205, 140),
         (1570, 218, 190, 212),
                                ]
        
	allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
	frames = list(zip(allImages, [100] * len(allImages)))

        self.RightFly = pyganim.PygAnimation(frames,loop=True)
	self.RightFly.blit(self.screen,(x,y))

	rects = [(1570, 218, 190 ,212),
         (1757, 218, 140, 150),
         (1910, 218, 125, 150),
         (2055, 218, 105, 155),
                                ]
        

        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))

        self.StopRightFly = pyganim.PygAnimation(frames,loop=False)
	self.StopRightFly.blit(self.screen,(x,y))

        rects = [(39, 1635, 135, 120),
                 (165, 1635, 135, 120),        
                 (312, 1635, 140, 120),
                 (468, 1635, 190, 110),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.StartLeftFly = pyganim.PygAnimation(frames,loop=False)
        self.StartLeftFly.blit(self.screen,(x,y))

        rects = [(676, 1635, 206, 117),
                       ( 896, 1635, 205, 89),        
                       (1112, 1635, 202, 90),
                       (1329,1635, 195, 113),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.LeftFly = pyganim.PygAnimation(frames)
        self.LeftFly.blit(self.screen,(x,y))

        rects= [(  39, 1635, 135, 120),
                 (165, 1635, 135, 120),        
                 (312, 1635, 140, 120),
                 (468, 1635, 190, 110),]
        allImages = pyganim.getImagesFromSpriteSheet('AD1.png', rects=rects)
        frames = list(zip(allImages, [100] * len(allImages)))
        self.StopLeftFly = pyganim.PygAnimation(frames,loop=False)
        self.StopLeftFly.blit(self.screen,(x,y))


    def draw(self,x,y):
        width=100
        height=100
        kx=0
        ky=45
        
        xc=xc2=x
        yc=yc2=y
        #left
        if x < self.oldx:
            xc=xc2=x+kx
            yc=y+ky
            yc2=y+height
        #up
        if y < self.oldy:
            yc=yc2=y+ky
            xc=x+kx
            xc2=x+width
        #right
        if x > self.oldx:
            xc=xc2=x+width
            yc=y+ky
            yc2=y+height
        #down
        if y > self.oldy:
            yc=yc2=y+height
            xc=x+kx
            xc2=x+height
        if(x<=0 or x>=1200 or y<=0 or y>=700  ) or (self.bgmap.get_at((int(xc),int(yc))) == (255,0,0,255) or self.bgmap.get_at((int(xc2),int(yc2))) == (255,0,0,255)):
            x=self.oldx
            y=self.oldy
            self.x=self.oldx
            self.y=self.oldy
        self.StayLeft.blit(self.screen, (x,y))
        self.StayRight.blit(self.screen, (x,y))
        self.LeftFly.blit(self.screen,(x,y))
        self.StartLeftFly.blit(self.screen,(x,y))
        self.StopLeftFly.blit(self.screen,(x,y))
	self.StartRightFly.blit(self.screen,(x,y))
	self.RightFly.blit(self.screen,(x,y))
	self.StopRightFly.blit(self.screen,(x,y))
        self.FireLeft.blit(self.screen,(x,y))
        self.oldx=self.x=x
        self.oldy=self.y=y
    def stopAll(self):
        if self.StayLeft._state!=pyganim.STOPPED:
            self.StayLeft.stop()
        if self.StayRight._state!=pyganim.STOPPED:
            self.StayRight.stop()
        if self.LeftFly._state!=pyganim.STOPPED:
            self.LeftFly.stop()
        if self.StartLeftFly._state!=pyganim.STOPPED:
            self.StartLeftFly.stop()
        if self.StopLeftFly._state!=pyganim.STOPPED:
            self.StopLeftFly.stop()
	if self.StartRightFly._state!=pyganim .STOPPED:
	     self.StartRightFly.stop()
	if self.RightFly._state!=pyganim.STOPPED:
             self.RightFly.stop()
        if self.StopRightFly._state!=pyganim.STOPPED:
            self.StopRightFly.stop()
        if self.FireLeft._state!=pyganim.STOPPED:
            self.FireLeft.stop()
