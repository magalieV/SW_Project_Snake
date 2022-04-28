"""Apple.py: File that handle the apple display and collision"""

import pygame
import random

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Apple:
    position = (0, 0)
    sprite_size = 32

    def __init__(self, screen_size, screen):
        self._sprite = pygame.image.load("assets/elements/apple.png")
        self._screen_size = screen_size
        self._screen = screen
        self.generate()

    def generate(self):
        x = round(random.randrange(0, round(self._screen_size[0] / 32 - 1))) * 32.0
        y = round(random.randrange(0, round(self._screen_size[1] / 32 - 1))) * 32.0
        self.position = (x, y)

    def display(self):
        self._screen.blit(self._sprite, self.position)

