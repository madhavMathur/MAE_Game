import pygame


class Player(BaseClass):
    def show(self, img, x, y):
        img = pygame.transform.scale(img, (25, 25))
        screen.blit(img, (x, y))

    def move(self, event):
        mov_x_change = 0
        mov_y_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mov_x_change = - 10
            elif event.key == pygame.K_RIGHT:
                mov_x_change = 10
            elif event.key == pygame.K_UP:
                mov_y_change = -10
            elif event.key == pygame.K_DOWN:
                mov_y_change = 10
        return mov_x_change, mov_y_change
