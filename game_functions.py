import pygame
import sys
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from time import sleep

def ship_hit(ai_Settings,stats,screen,ship,aliens,bullets):
	if stats.ships_left >= 0:
		stats.ships_left-=1
		aliens.empty()
		bullets.empty()
	
		create_fillet(ai_Settings,screen,ship,aliens)
		ship.center_ship()
	
		sleep(1)
	else:
		stats.game_active=False
	
def check_aliens_bottom(ai_Settings,stats,screen,ship,aliens,bullets):
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_Settings,stats,screen,ship,aliens,bullets)
			break
	
def check_KEYDOWN_events(event,ai_Settings,screen,ship,bullets):
	if event.key==pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key==pygame.K_LEFT:
		ship.moving_left = True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_Settings,screen,ship,bullets)
	elif event.key==pygame.K_Q:
		sys.exit()
		
def fire_bullet(ai_Settings,screen,ship,bullets):
	if len(bullets) < ai_Settings.bullet_max_numble:
		new_bullet=Bullet(ai_Settings,screen,ship)
		bullets.add(new_bullet)

def check_KEYUP_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key==pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_Settings,screen,ship,bullets):
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()	
			
			elif event.type==pygame.KEYDOWN:
				check_KEYDOWN_events(event,ai_Settings,screen,ship,bullets)
					
			elif event.type == pygame.KEYUP:
				check_KEYUP_events(event,ship)
				
def update_screen(ai_Settings,screen,ship,aliens,bullets):
	screen.fill(ai_Settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	pygame.display.flip()
	
def update_bullets(ai_Settings,screen,ship,aliens,bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_Settings,screen,ship,aliens,bullets)
	
def check_bullet_alien_collisions(ai_Settings,screen,ship,aliens,bullets):
	collisions=pygame.sprite.groupcollide(aliens,bullets,True,False)
	if len(aliens)==0:
		bullets.empty()
		create_fillet(ai_Settings,screen,ship,aliens)
		
def get_numble_aliens_x(ai_Settings,alien_width):
	alien_space_x=ai_Settings.screen_width-2*alien_width
	alien_numble_x=int(alien_space_x/(2*alien_width))
	return alien_numble_x
	
def get_number_rows(ai_Settings,ship_height,alien_height):
	alien_space_y=ai_Settings.screen_height-(alien_height+ship_height+2*alien_height)
	numbler_rows=int(alien_space_y/(2*alien_height))
	return numbler_rows
	
def create_alien(ai_Settings,screen,aliens,alien_number,row_numbler):
	alien=Alien(ai_Settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_numbler
	aliens.add(alien)
		
def create_fillet(ai_Settings,screen,ship,aliens):
	alien=Alien(ai_Settings,screen)
	number_aliens_x=get_numble_aliens_x(ai_Settings,alien.rect.width)
	bumbler_rows=get_number_rows(ai_Settings,ship.rect.height,alien.rect.height)
	
	for row_numbler in range(bumbler_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_Settings,screen,aliens,alien_number,row_numbler)

def check_fleet_edges(ai_Settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_Settings,aliens)
			break
		
def	change_fleet_direction(ai_Settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y+=ai_Settings.fleet_drop_speed
		ai_Settings.fleet_direction*=-1
		
def update_aliens(ai_Settings,stats,screen,ship,aliens,bullets):
	check_fleet_edges(ai_Settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_Settings,stats,screen,ship,aliens,bullets)
	check_aliens_bottom(ai_Settings,stats,screen,ship,aliens,bullets)

		



	
