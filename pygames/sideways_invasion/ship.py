#! Module for ship class.
import pygame


class Ship:

    def __init__(self, ai_set, screen):
        """Инициализирует корабль и задаёт ему стартовую позицию."""
        self.screen = screen
        self.ai_set = ai_set

        # Загружает изображение корабля и get its rect.
        self.image = pygame.image.load('si_files/helicopter.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Запускает каждый новый корабль в центре низа экрана.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Хранит десятичное значение для центра корабля.
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect
        if self.moving_up and self.rect.top > 0:
            # Идёт проверка на границы экрана.
            self.center -= self.ai_set.ship_speed_factor
        # Используется if вместо elif, чтобы иметь возможность
        # нажимать клавиши одновременно.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_set.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centery = self.center

    def blitme(self):
        """Прорисовывает корабль и его текущее положение"""
        self.screen.blit(self.image, self.rect)
