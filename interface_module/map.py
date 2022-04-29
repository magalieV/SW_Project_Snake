
"""map.py: File that handle the display of the map"""


"""Import statement go there"""


import os
from random import randint
import pygame
from pygame.locals import *
import numpy as np
tile_width, tile_hight = 32, 32
named_tile = {"body": 0, "head": 1, "apple": 2}

debug = True


class Map():

    def __init__(self, screen):
        self.screen = screen
        self.load_tileset(os.path.join("snake_interface.png"))
        self.reset()
        self.randomize()

    def reset(self, tiles_x=40, tiles_y=40):
        self.tiles_x, self.tiles_y = tiles_x, tiles_y
        self.tiles = np.zeros((self.tiles_x, self.tiles_y), dtype=int)

        if debug:
            print("Map().reset(size={}, {})".format(tiles_x, tiles_y))

    def randomize(self):

        self.offset = (-200, -200)
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                self.tiles[x, y] = randint(0, len(named_tile.keys()))

        self.tiles[1:] = named_tile["apple"]
        self.tiles[:2] = named_tile["apple"]

        if debug:
            print("tiles = ", self.tiles)

    def load_tileset(self, image="snake_interface.png"):
        self.tileset = pygame.image.load(image)
        self.rect = self.tileset.get_rect()

    def draw(self):
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                cur = self.tiles[x][y]
                dest = Rect(x * tile_width, y * tile_hight,
                            tile_width, tile_hight)
                src = Rect(cur * tile_width, 0, tile_width, tile_hight)

                self.screen.blit(self.tileset, dest, src)
