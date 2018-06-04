import pygame.font

class Botton():
	def __init__(self,ai_Settings,screen,msg):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.width,self.height = 200,50
		self.button_color = (255,255,0)
		self.text_color = (0,255,255)
		slef.font=pygame.font.SysFont(None,48)
		
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		
		self.prep_msg(msg)
	
	def prep_msg(self,msg):
		self.msg_image=self.font.render(msg)
