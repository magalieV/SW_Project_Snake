"""SnakeBody.py: File that handle the snake body display and movement"""

import pygame
from game_module.gameplay.Enumerations import Position, Movement, Turn
from game_module.gameplay.Apple import Apple
from game_module.gameplay.Settings import Grill

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = ["Magalie Vandenbriele", "Irama Chaouch"]
__email__ = "magalie.vandenbriele@epitech.eu"

BODY_PATH_HORIZONTAL = "game_module/assets/snake/body_horizontal.png"
BODY_PATH_VERTICAL = "game_module/assets/snake/body_vertical.png"

TURN_LEFT_UPPER = "game_module/assets/snake/upper_left.png"
TURN_RIGHT_UPPER = "game_module/assets/snake/upper_right.png"
TURN_LEFT_BOTTOM = "game_module/assets/snake/bottom_left.png"
TURN_RIGHT_BOTTOM = "game_module/assets/snake/bottom_right.png"

SPEED = 20
TICK_SIZE = SPEED / SPEED


class SnakeBody:
    body_part = []

    def __init__(self, window, window_size, multi=None, body_part_save=None):
        self._window = window
        self._window_size = window_size
        self._sprite_size = 20
        self._turn = {}
        self._turn_sprite = {Turn.UP_LEFT: pygame.image.load(TURN_LEFT_UPPER).convert_alpha(),
                             Turn.UP_RIGHT: pygame.image.load(TURN_RIGHT_UPPER).convert_alpha(),
                             Turn.DOWN_LEFT: pygame.image.load(TURN_LEFT_BOTTOM).convert_alpha(),
                             Turn.DOWN_RIGHT: pygame.image.load(TURN_RIGHT_BOTTOM).convert_alpha()}
        self._sprites = {Position.VERTICAL: pygame.image.load(BODY_PATH_VERTICAL).convert_alpha(),
                         Position.HORIZONTAL: pygame.image.load(BODY_PATH_HORIZONTAL).convert_alpha()}
        self._associate = {Movement.UP: Position.VERTICAL, Movement.DOWN: Position.VERTICAL,
                           Movement.LEFT: Position.HORIZONTAL, Movement.RIGHT: Position.HORIZONTAL}
        if body_part_save is None:
            if multi is None:
                self.body_part = [Grill(Movement.UP,
                                        (round(round(window_size[0] / self._sprite_size) / 2) * self._sprite_size),
                                        (round(round(window_size[1] / self._sprite_size) / 2) * self._sprite_size) + self._sprite_size)]
            elif multi == 1:
                self.body_part = [(Grill(Movement.DOWN, self._sprite_size, self._sprite_size))]
            elif multi == 2:
                self.body_part = [(Grill(Movement.UP, self._sprite_size * 80 - self._sprite_size, self._sprite_size * 40 - (self._sprite_size * 2)))]

        else:
            self.body_part = body_part_save

    def load_snake(self, body_part_save):
        self.body_part = body_part_save

    def display(self):
        for element in self.body_part:
            if element.turn is not Turn.NONE:
                self._window.blit(self._turn_sprite[element.turn], (element.x, element.y))
            else:
                self._window.blit(self._sprites[self._associate[element.movement]], (element.x, element.y))

    def move_corner(self, element, corners):
        if element.movement == Movement.UP:
            element.y -= SPEED
        elif element.movement == Movement.DOWN:
            element.y += SPEED
        elif element.movement == Movement.LEFT:
            element.x -= SPEED
        elif element.movement == Movement.RIGHT:
            element.x += SPEED
        square_x = element.x / self._sprite_size
        square_y = element.y / self._sprite_size
        find_corner = False
        for corner in corners:
            if corner.x == square_x and corner.y == square_y:
                before_corner = element.movement
                element.movement = corner.movement
                find_corner = True
                element.turn = Turn.NONE
                if (corner.movement == Movement.DOWN and before_corner == Movement.LEFT) \
                        or (before_corner == Movement.UP and corner.movement == Movement.RIGHT) \
                        or (element.turn is Turn.UP_LEFT and corner.movement is Movement.DOWN) or \
                        (element.turn is Turn.DOWN_LEFT and corner.movement is Movement.DOWN):
                    element.turn = Turn.DOWN_RIGHT
                elif (corner.movement == Movement.DOWN and before_corner == Movement.RIGHT) \
                        or (before_corner == Movement.UP and corner.movement == Movement.LEFT) \
                        or (element.turn is Turn.UP_RIGHT and corner.movement is Movement.DOWN) or \
                        (element.turn is Turn.DOWN_RIGHT and corner.movement is Movement.DOWN):
                    element.turn = Turn.DOWN_LEFT
                elif (corner.movement == Movement.UP and before_corner == Movement.LEFT) \
                        or (before_corner == Movement.DOWN and corner.movement == Movement.RIGHT) \
                        or (element.turn is Turn.UP_LEFT and corner.movement is Movement.UP) or \
                        (element.turn is Turn.DOWN_LEFT and corner.movement is Movement.UP):
                    element.turn = Turn.UP_RIGHT
                elif (corner.movement == Movement.UP and before_corner == Movement.RIGHT) \
                        or (before_corner == Movement.DOWN and corner.movement == Movement.LEFT) \
                        or (element.turn is Turn.UP_RIGHT and corner.movement is Movement.UP) or \
                        (element.turn is Turn.DOWN_RIGHT and corner.movement is Movement.UP):
                    element.turn = Turn.UP_LEFT
        if find_corner and element == self.body_part[-1]:
            corners.pop(0)
        if not find_corner:
            element.turn = Turn.NONE
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
