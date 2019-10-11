import pygame
import sys
from random import randint


class Settings:
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (255, 255, 255)
        self.dude_speed_factor = 1.5
        self.ball_speed_factor = 1.0
        self.ball_direction = 1


class Dude:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('ballfiles/dude.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.dude_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.dude_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Ball:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('ballfiles/ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def update(self, settings, screen, dude):
        self.y += self.settings.ball_speed_factor * self.settings.ball_direction
        self.rect.y = self.y
        check_ball_dude_collisions(settings, screen, dude, self)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def check_keydown_events(event, settings, screen, dude, ball):
    if event.key == pygame.K_RIGHT:
        dude.moving_right = True
    elif event.key == pygame.K_LEFT:
        dude.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, dude):
    if event.key == pygame.K_RIGHT:
        dude.moving_right = False
    elif event.key == pygame.K_LEFT:
        dude.moving_left = False


def check_events(settings, screen, dude, ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, dude, ball)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, dude)


def update_screen(settings, screen, dude, ball):
    screen.fill(settings.bg_color)
    dude.blitme()
    ball.blitme()
    pygame.display.flip()


def check_ball_dude_collisions(settings, screen, dude, ball):
    if not ball:
        create_ball(settings, screen)
    else:
    	collisions = pygame.sprite.spritecollideany(dude, [ball])

def create_ball(settings, screen):
    ball = Ball(settings, screen)
    ball.x = randint(20, 1000)
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height * 2


def update_ball(ball):
    ball.update()


def ball():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("The Ball")
    dude = Dude(settings, screen)
    ball = Ball(settings, screen)

    while True:
        check_events(settings, screen, dude, ball)
        dude.update()
        ball.update(settings, screen, dude)
        update_screen(settings, screen, dude, ball)


ball()
