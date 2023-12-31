import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # initialize game and create a scren object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # make a ship
    ship = Ship(ai_settings, screen)
    
    # make a group to store bullets in
    bullets = Group()
    
    # set the background color
    bg_color = (230,230,230)
    
    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        
        print(len(bullets))
        
        gf.update_screen(ai_settings, screen, ship, bullets)
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()