"""Map.py: File that display the map"""

import pygame

__author__ = "Irama Chaouch"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Map:
    def __init__(self, window, width, height):
        self.sprite = pygame.image.load(
            "interface_module/assets/map_back.png").convert()
        self.wall_sprite = pygame.image.load(
            "interface_module/assets/wall.png").convert()
        self.width = width + 2
        self.height = height + 2
        self.window = window
        self.square_color = (10, 19, 6)

    def display(self):
        x = 0
        y = 0
        for i in range(0, self.width):
            for j in range(0, self.height):
                if x == 0 or y == 0 or i == self.width - 1 or j == self.height - 1:
                    self.window.blit(self.wall_sprite, (x, y))
                else:
                    self.window.blit(self.sprite, (x, y))
                    pygame.draw.rect(self.window, self.square_color,
                                     pygame.Rect(x, y, 20, 20), 2)
                y += 20
            x += 20
            y = 0
