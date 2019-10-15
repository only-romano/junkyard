#! Module for char class.
import pygame
from pygame.sprite import Sprite


class Char(Sprite):

    def __init__(self, ai_set, screen):
        """Инициализирует корабль и задаёт ему стартовую позицию."""
        super(Char, self).__init__()
        self.screen = screen
        self.ai_set = ai_set

        # Загружает изображение корабля Игрока и get its rect.
        self.image = pygame.image.load('si_files/ufo.bmp')
        self.rect = self.image.get_rect()

        # Запускает корабль Игрока в центре экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Хранит точную позицию алиена.
        self.y = float(self.rect.y)

    def blitme(self):
        """Прорисовывает корабль и его текущее положение"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        self.y -= (self.ai_set.alien_speed_factor * self.ai_set.fleet_direction)
        self.rect.y = self.y

