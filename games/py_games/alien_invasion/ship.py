#! Module for ship class.
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_set, screen):
        """Инициализирует корабль и задаёт ему стартовую позицию."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_set = ai_set

        # Загружает изображение корабля и get its rect.
        self.image = pygame.image.load('ai_files/spaceship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Запускает каждый новый корабль в центре низа экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Хранит десятичное значение для центра корабля.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Идёт проверка на границы экрана.
            self.center += self.ai_set.ship_speed_factor
        # Используется if вместо elif, чтобы иметь возможность
        # нажимать клавиши одновременно.
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_set.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def blitme(self):
        """Прорисовывает корабль и его текущее положение"""
        self.screen.blit(self.image, self.rect)
