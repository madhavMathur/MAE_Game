import pygame, sys
# from pygame.locals import *

pygame.init()

black = 0,0,0
white = 255,255,255

dimensions = SCREENWIDTH,SCREENHEIGHT = 640,480
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
FPS = 60
total_frames = 0

GameRunning = True

pygame.display.set_caption("Space-Invaders")
# GAME LOOP
while True:
	# PROCESSES
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if GameRunning:

		total_frames+=1

		pygame.display.flip()
		clock.tick(FPS)
