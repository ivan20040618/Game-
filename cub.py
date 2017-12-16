import pygame
rect_x=0
rect_y=0
pygame.init()
size=(700,700)
clock = pygame.time.Clock()
screen=pygame.display.set_mode(size)
done=False
#bg=pygame.Surface(size).convert()
bg=pygame.image.load('grees.png')
screen.fill((0,255,0))
bg.fill((255,0,0))
while done==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

	bg.fill((255,0,0))
#	screen.blit(bg,(0,0))
	pygame.draw.rect(screen,(200,200,200),[rect_x,rect_y,50,50])
	rect_x+=3
	rect_y+=3
#	pygame.display.flip()
	pygame.display.flip()
	clock.tick(60)
#	screen.blit(s,(0,0))
#	pygame.display.update()
	if rect_x>=650 and rect_y>=650:
		screen.fill((255,0,0))
		rect_x=0
		rect_y=0
pygame.quit()
