#! File contains a number of functions that carry out the bulk of the
# work in the game.  Also contains update_screen().
import sys
import pygame
from bullet import Bullet
from character import Char
from time import sleep


def check_keydown_events(event, ai_set, screen, stats, sb, ship, aliens, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    # Можно использовать elif, потому что каждое событие
    # соединено со своей одной клавишей, если обе кнопки
    # будут нажаты - события определятся.
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Shots the bullet.
        fire_bullet(ai_set, screen, ship, bullets, stats)
    elif event.key == pygame.K_q:
        # Exit from the game.
        high_score(stats)
        sys.exit()
    elif event.key == pygame.K_p:
        # Start the game.
        start_game(ai_set, screen, stats, sb, ship, aliens, bullets)


def high_score(stats):
    """Write high score to text file score.txt"""
    with open('score.txt', 'r') as score:
        best = score.read()
    if int(stats.high_score) > int(best):
        with open('score.txt', 'w') as score:
            score.write(str(int(stats.high_score)))


def fire_bullet(ai_set, screen, ship, bullets, stats):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    # Limiting the Number of Bullets.
    if len(bullets) < ai_set.bullets_allowed:
        new_bullet = Bullet(ai_set, screen, ship)
        stats.shot_sound.play()
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_set, screen, stats, sb, play_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_set, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_set, screen, stats, sb, play_button, ship, aliens,
                              bullets, mouse_x, mouse_y)


def check_play_button(ai_set, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_set, screen, stats, sb, ship, aliens, bullets)


def start_game(ai_set, screen, stats, sb, ship, aliens,
                      bullets):
    """Start a new game"""
    # Reset the game settings.z
    ai_set.initialize_dynamic_settings()
    # Hide the mouse cursor.
    pygame.mouse.set_visible(False)
    # Reset the game statistics.
    stats.reset_stats()
    # Pygame detects a  MOUSEBUTTONDOWN event when the player clicks
    # anywhere on the screen u, but we want to restrict our game to
    # respond to mouse clicks only on the Play button.
    stats.game_active = True

    # Reset the scoreboard images.
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    # Create a new fleet and center the ship.
    create_fleet(ai_set, screen, ship, aliens)
    ship.center_ship()


def update_screen(ai_set, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update images in the screen and flip to the new screen."""

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_set.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # draw - автоматически прорисовывает каждый элемент в группе на
    # позиции, установленной атрибутом rect.
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_set, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        # Нельзя удалять элементы внутри цикла for, для этого
        # использутся копия.  Это позволяет модифицировать объект
        # внутри цикла.
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_set, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_set, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    # Check for any bullets that have hit aliens.  If so, get rid of the
    # bullet and the alien.  Новая строка циклирует через каждую пулю и
    # пришельца.  groupcollide() добавляет словарь.  Две True говорят о том,
    # что при столкновении оба объекта - пуля и пришелец исчезают (чтобы
    # сделать крутецкую пулю, которая пробивает всех - надо изменить первый
    # аргумент на False, если же наоборот - то пули не будут пробивать броню.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.exp_fun.play()
        for aliens in collisions.values():
            # Making Sure to Score All Hits.
            stats.score += ai_set.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        new_level(ai_set, screen, stats, sb, ship, aliens, bullets)


def new_level(ai_set, screen, stats, sb, ship, aliens, bullets):
    # If the entire fleet is destroyed, start a new level.
    # Destroy existing bullets and create new fleet.
    bullets.empty()  # Очищает группу снарядов.
    # Speed up game.
    ai_set.increase_speed()
    # Increase level.
    stats.level += 1
    sb.prep_level()
    # Создаёт новвый флот, если старый уничтожен.
    create_fleet(ai_set, screen, ship, aliens)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def create_fleet(ai_set, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Создаёт пришелька и находит колличество алинюг в ряду.
    # Пространство между каждым пришелем равен половине ширины аленюги.
    alien = Char(ai_set, screen)
    number_aliens_x = get_number_aliens_x(ai_set, alien.rect.width)
    number_rows = get_number_rows(ai_set, ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_set, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_set, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_set.screen_width - alien_width
    number_aliens_x = int(available_space_x / (1.3 * alien_width))
    return number_aliens_x


def get_number_rows(ai_set, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_set.screen_height - (1.3 * alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (3 * alien_height))
    return number_rows


def create_alien(ai_set, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Char(ai_set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + int(1.3 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height * 1.5 + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_fleet_edges(ai_set, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_set, aliens)
            break


def change_fleet_direction(ai_set, aliens):
    """Drop the entire fleet and change the fleet's durection"""
    for alien in aliens.sprites():
        alien.rect.y += ai_set.fleet_drop_speed
    ai_set.fleet_direction *= -1


def update_aliens(ai_set, stats, screen, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    Update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_set, aliens)
    aliens.update()
    # Look for alien-ship collusuons.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_set, stats, screen, sb, ship, aliens, bullets)
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_set, stats, screen, sb, ship, aliens, bullets)


def ship_hit(ai_set, stats, screen, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    stats.exp_ship.play()
    if stats.ships_left > 0:
        ship_revive(ai_set, stats, screen, sb, ship, aliens, bullets)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def ship_revive(ai_set, stats, screen, sb, ship, aliens, bullets):
    """Restrore defeault position"""
    # Decrement ships left.
    stats.ships_left -= 1
    #Update scoreboard.
    sb.prep_ships()
    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    # Create a new fleet and center the ship.
    create_fleet(ai_set, screen, ship, aliens)
    ship.center_ship()
    # Pause.
    sleep(0.5)



def check_aliens_bottom(ai_set, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_set, stats, screen, sb, ship, aliens, bullets)
            break
