import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import Gamestats
  
def run_game():
	pygame.init()
	ai_Settings=Settings()
	
	screen=pygame.display.set_mode((ai_Settings.screen_width,ai_Settings.screen_height))
	pygame.display.set_caption('Alien COME')
	
	stats=Gamestats(ai_Settings)
	ship=Ship(ai_Settings,screen)
	bullets=Group()
	alien=Alien(ai_Settings,screen)
	aliens=Group()
	
	gf.create_fillet(ai_Settings,screen,ship,aliens)

	while True:
		gf.check_events(ai_Settings,screen,ship,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_Settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_Settings,stats,screen,ship,aliens,bullets)
		
		gf.update_screen(ai_Settings,screen,ship,aliens,bullets)
		
run_game()	
