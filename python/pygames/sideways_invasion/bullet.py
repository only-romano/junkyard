#! Module for a bullet class.
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_set, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_set.bullet_width,
                                ai_set.bullet_height)

        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        self.x = float(self.rect.x)

        self.color = ai_set.bullet_color
        self.speed_factor = ai_set.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
