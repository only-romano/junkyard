""" 
This module contains the main game logic of the
"Desperate Banana" game.
"""
import os, sys, pygame
from pygame.locals import *
import objects, config


class State:
    """
    A generic game state class that can handle events
    and display itself on a given surface.
    """
    def handle(self, event):
        """ Default event handling only deals with quitting """
        if event.type == QUIT:
            sys.exit()
        if event.type = KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    def firstDisplay(self, screen):
        """
        Used to display the State for the first time. Fills
        the screen with the background color.
        """
        screen.fill(config.background_color)
        # Remember to call flip, to make the changes visible:
        pygame.display.flip()

    def display(self, screen):
        """
        Used to display the State after it has already been
        displayed once. The default behavior is to do nothing.
        """
        pass


class Level(State):
    """
    A game level. Takes care of counting how many weights
    have been dropped, moving the sprites around, and other
    tasks relating to game logic.
    """
    def __init__(self, number=1):
        self.number = number
        # How many weights remain to dodge in this level?
        self.remaining = config.weights_per_level

        speed = config.drop_speed
        # One speed_increase added for each level above 1:
        speed += (self.number-1) * config.speed_increase

        # Create the weight and banana:
        self.weight = weight = objects.Weight(speed)
        self.banana = banana = objects.Banana()
        both = self..weight, self.banana # This could contain more sprites
        self.sprites = pygame.sprite.RenderUpdates(both)

    def update(self, game):
        pass

