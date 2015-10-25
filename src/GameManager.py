import pygame, sys, Player
# from pygame.locals import *


pygame.init()
black = 0,0,0
white = 255,255,255
dimensions = SCREENWIDTH,SCREENHEIGHT = 640,480

screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()

FPS = 60
total_frames = 0
xpos = 300
ypos = 300

player = Player()

img = pygame.image.load('Player.png')

GameRunning = True

pygame.display.set_caption("MAE Game Testing")
# GAME LOOP
while True:
    # PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        mov_x_change, mov_y_change = player.move(event)
    xpos += mov_x_change
    ypos += mov_y_change

    if GameRunning:

        total_frames += 1

        pygame.display.flip()
        screen.fill(black)
        player.show(img, xpos, ypos)

        clock.tick(FPS)