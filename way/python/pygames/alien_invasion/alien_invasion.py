#! Main file of the game.  Creates a number of important objects used
# throughout the game, stored main loop.
import pygame
from ai_settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


# functions block
def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()
    ai_set = Settings()
    screen = pygame.display.set_mode((ai_set.screen_width,
                                      ai_set.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play buttton.
    play_button = Button(ai_set, screen, "Play")
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_set)
    sb = Scoreboard(ai_set, screen, stats)
    # Make a ship.
    ship = Ship(ai_set, screen)
    # Make a group to store bullets and a group of aliens.
    bullets = Group()
    aliens = Group()

    # Music
    pygame.mixer.init()
    pygame.mixer.music.load("ai_files/bensound-summer.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    # Sounds
    stats.shot_sound = pygame.mixer.Sound("ai_files/shot_laser.wav")
    stats.shot_sound.set_volume(0.7)
    stats.exp_ship = pygame.mixer.Sound("ai_files/explosion_ship.wav")
    stats.exp_ship.set_volume(0.7)
    stats.exp_fun = pygame.mixer.Sound("ai_files/explosion_fun.wav")
    stats.exp_fun.set_volume(0.7)


    # Create the fleet of aliens.
    gf.create_fleet(ai_set, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_set, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_set, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_set, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_set, screen, stats, sb, ship, aliens, bullets,
                         play_button)


# Инициализация игры и запуск главного цикла.
run_game()
