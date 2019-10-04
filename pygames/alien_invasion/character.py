#! Module for char class.
import pygame
from pygame.sprite import Sprite


class Char(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_set, screen):
        """Инициализирует пришелюгу и задаёт ему стартовую позицию."""
        super(Char, self).__init__()
        self.screen = screen
        self.ai_set = ai_set

        # Загружает изображение элиена и get its rect.
        self.image = pygame.image.load('ai_files/ufo2.bmp')
        self.rect = self.image.get_rect()

        # Запускает корабль рядом с верним левым углом.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Хранит точную позицию алиена.
        self.x = float(self.rect.x)

    def blitme(self):
        """Прорисовывает пришеля и его текущее положение"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_set.alien_speed_factor * self.ai_set.fleet_direction)
        self.rect.x = self.x
