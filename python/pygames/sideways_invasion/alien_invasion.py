#! Main file of the game.

import pygame
from ai_settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


# functions block
def run_game():
    pygame.init()
    pygame.mixer.init()
    ai_set = Settings()
    screen = pygame.display.set_mode((ai_set.screen_width,
                                      ai_set.screen_height))
    pygame.display.set_caption("Sideways Invasion")
    ship = Ship(ai_set, screen)
    bullets = Group()
    stars = Group()

    # Create the fleet of aliens.
    gf.create_starlight(ai_set, screen, ship, stars)

    # Play music
    pygame.mixer.music.load("si_files/bensound-creativeminds.mp3")
    pygame.mixer.music.set_volume(0.30)
    pygame.mixer.music.play(-1)


    # Start the main loop for the game.
    while True:
        gf.check_events(ai_set, screen, ship, stars, bullets)
        ship.update()
        gf.update_bullets(ai_set, screen, ship, stars, bullets)
        gf.update_stars(ai_set, stars)
        gf.update_screen(ai_set, screen, ship, stars, bullets)


run_game()
