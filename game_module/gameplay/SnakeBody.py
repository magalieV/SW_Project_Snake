"""SnakeBody.py: File that handle the snake body display and movement"""

import pygame
from game_module.gameplay.Enumerations import Position, Movement
from game_module.gameplay.Apple import Apple
from game_module.gameplay.Settings import Grill

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

BODY_PATH = "game/assets/snake/body.png"
SPEED = 8
TICK_SIZE = 32/8


class SnakeBody:
    body_part = []

    def __init__(self, window, window_size, body_part_save=None):
        self._window = window
        self._window_size = window_size
        self._sprite_size = 32
        self._turn = {}
        self._sprites = pygame.image.load(BODY_PATH).convert_alpha()
        if body_part_save is None:
            self.body_part = [Grill(Movement.UP, (round(window_size[0] / self._sprite_size) / 2 * self._sprite_size),
                                    (round(window_size[1] / self._sprite_size) / 2 * self._sprite_size) + self._sprite_size)]
        else:
            self.body_part = body_part_save

    def display(self):
        for element in self.body_part:
            self._window.blit(self._sprites, (element.x, element.y))

    def move_corner(self, element, corners):
        square_x = element.x / self._sprite_size
        square_y = element.y / self._sprite_size
        find_corner = False
        for corner in corners:
            if corner.x == square_x and corner.y == square_y:
                element.movement = corner.movement
                find_corner = True
        if element.movement == Movement.UP:
            element.y -= SPEED
        elif element.movement == Movement.DOWN:
            element.y += SPEED
        elif element.movement == Movement.LEFT:
            element.x -= SPEED
        elif element.movement == Movement.RIGHT:
            element.x += SPEED
        if find_corner and element == self.body_part[-1]:
            corners.pop(0)
        return corners

    def update(self, corners):
        for element in self.body_part:
            if element.tick != 0:
                element.tick -= 1
                continue
            corners = self.move_corner(element, corners)
        return corners

    def add_body(self):
        last = self.body_part[-1]
        self.body_part.append(Grill(last.movement, last.x, last.y, TICK_SIZE))

