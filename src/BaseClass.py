import pygame

class BaseClass(pygame.sprite.Sprite):

	allsprites = pygame.sprite.Group()
	def __init__(self,x,y,width,height,image_string):
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()

		self.width = width
		self.height = height

		self.rect.centerx = x
		self.rect.centery = y
