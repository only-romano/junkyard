#! Module for a bullet class.
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    # When you use sprites, you can group related elements in your game
    # and act on all the grouped elements at once.

    def __init__(self, ai_set, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_set.bullet_width,
                                ai_set.bullet_height)
        # The bullet is not based on an image so we have to build a rect
        # from scratch using the  pygame.Rect() class.  This class
        # requires the x- and y-coordinates of the top-left corner of
        # the rect , and the width and height of the rect.

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_set.bullet_color
        self.speed_factor = ai_set.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
