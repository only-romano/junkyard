#! File contains a number of functions that carry out the bulk of the
# work in the game.  Also contains update_screen().
import sys
import pygame
from bullet import Bullet
from character import Char
from random import randint


def check_keydown_events(event, ai_set, screen, ship, char, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_set, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # Exit from the game.
        sys.exit()


def fire_bullet(ai_set, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_set.bullets_allowed:
        new_bullet = Bullet(ai_set, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_set, screen, ship, stars, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_set, screen, ship, stars, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_set, screen, ship, stars, bullets):
    """Update images in the screen and flip to the new screen."""
    screen.fill(ai_set.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    stars.draw(screen)
    pygame.display.flip()


def update_bullets(ai_set, screen, ship, stars, bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= 1024:
            bullets.remove(bullet)
    check_bullet_stars_collisions(ai_set, screen, ship, stars, bullets)


def check_bullet_stars_collisions(ai_set, screen, ship, stars, bullets):
    collisions = pygame.sprite.groupcollide(bullets, stars, True, True)
    if len(stars) == 0:
        bullets.empty()
        create_starlight(ai_set, screen, ship, stars)


def create_starlight(ai_set, screen, ship, stars):
    """Create a full fleet of aliens."""
    # Создаёт пришелька и находит колличество алинюг в ряду.
    # Пространство между каждым пришелем равен половине ширины аленюги.
    star = Char(ai_set, screen)
    number_stars_y = get_number_stars_y(ai_set, star.rect.height)
    number_rows = get_number_rows(ai_set, ship.rect.width, star.rect.width)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for star_number in range(number_stars_y):
            if randint(0,1) == 1:
                create_alien(ai_set, screen, stars, star_number, row_number)


def get_number_stars_y(ai_set, alien_height):
    """Determine the number of aliens that fit in a row."""
    available_space_y = ai_set.screen_height - alien_height
    number_stars_y = int(available_space_y / (2 * alien_height))
    return number_stars_y


def get_number_rows(ai_set, ship_width, star_width):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_x = (ai_set.screen_width - (2 * star_width) -
                         ship_width)
    number_rows = int(available_space_x / (3 * star_width))
    return number_rows


def create_alien(ai_set, screen, stars, star_number, row_number):
    """Create an alien and place it in the row."""
    star = Char(ai_set, screen)
    star_height = star.rect.height
    star.y = star_height + int(2 * star_height * star_number)
    star.rect.y = star.y
    star.rect.x = ai_set.screen_width - (star.rect.width + 2 * star.rect.width * row_number)
    stars.add(star)


def check_fleet_edges(ai_set, stars):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in stars.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_set, stars)
            break


def change_fleet_direction(ai_set, stars):
    """Drop the entire fleet and change the fleet's durection"""
    for star in stars.sprites():
        star.rect.x -= ai_set.fleet_drop_speed
    ai_set.fleet_direction *= -1


def update_stars(ai_set, stars):
    check_fleet_edges(ai_set, stars)
    stars.update()
