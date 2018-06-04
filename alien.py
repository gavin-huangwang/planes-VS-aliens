import pygame
from pygame.sprite import Sprite
class Alien(Sprite):	
	def __init__ (self,ai_Settings,screen):
		super(Alien,self).__init__()
		self.ai_Settings=ai_Settings
		self.screen=screen
		self.image=pygame.image.load('images/alien.bmp')
		self.rect=self.image.get_rect()
		
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)
	
	def check_edges(self):
		screen_rect=self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			
	def update(self):
		self.x+=self.ai_Settings.alien_speed_factor
		self.rect.x=self.x
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
