"""SnakeHead.py: File that handle the snake head display and movement"""

import pygame
from Enumerations import Movement, CollideType
from Apple import Apple
from Settings import Grill

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

HEAD_UP = "assets/snake/head_up.png"
HEAD_DOWN = "assets/snake/head_down.png"
HEAD_LEFT = "assets/snake/head_left.png"
HEAD_RIGHT = "assets/snake/head_right.png"
SPEED = 8


class SnakeHead:
    def __init__(self, window, window_size):
        self._heads = {Movement.UP: pygame.image.load(HEAD_UP).convert_alpha(),
                       Movement.DOWN: pygame.image.load(HEAD_DOWN).convert_alpha(),
                       Movement.LEFT: pygame.image.load(HEAD_LEFT).convert_alpha(),
                       Movement.RIGHT: pygame.image.load(HEAD_RIGHT).convert_alpha()}
        self._sprite_size = 32
        self._window = window
        self._window_size = window_size
        self._next_head_movement = []
        self._actual_head = Movement.UP
        self._head_position = ((round(window_size[0] / self._sprite_size) / 2 * self._sprite_size), (round(window_size[1] / self._sprite_size) / 2 * self._sprite_size))

    def collide(self, apple):
        if self._head_position[0] < 0 or (self._head_position[0] + self._sprite_size) > self._window_size[0] \
                or self._head_position[1] < 0 or (self._head_position[1] + self._sprite_size) > self._window_size[1]:
            return CollideType.BORDER
        middle_snake_x = self._head_position[0] + (self._sprite_size / 2)
        middle_snake_y = self._head_position[1] + (self._sprite_size / 2)
        middle_apple_x = apple.position[0] + (apple.sprite_size / 2)
        middle_apple_y = apple.position[1] + (apple.sprite_size / 2)
        if middle_snake_x == middle_apple_x and middle_snake_y == middle_apple_y:
            apple.generate()
            return CollideType.APPLE
        return CollideType.NONE

    def display(self):
        self._window.blit(self._heads[self._actual_head], self._head_position)

    def update(self):
        square_x = self._head_position[0] / self._sprite_size
        square_y = self._head_position[1] / self._sprite_size
        grill = None
        if square_x.is_integer() and square_y.is_integer() and len(self._next_head_movement) > 0:
            tmp = self._next_head_movement.pop(0)
            while tmp == self._actual_head and len(self._next_head_movement) > 0:
                tmp = self._next_head_movement.pop(0)
            if tmp is not self._actual_head:
                self._actual_head = tmp
                grill = Grill(tmp, square_x, square_y)
        if self._actual_head == Movement.UP:
            self._head_position = (self._head_position[0], self._head_position[1] - SPEED)
        elif self._actual_head == Movement.DOWN:
            self._head_position = (self._head_position[0], self._head_position[1] + SPEED)
        elif self._actual_head == Movement.LEFT:
            self._head_position = (self._head_position[0] - SPEED, self._head_position[1])
        elif self._actual_head == Movement.RIGHT:
            self._head_position = (self._head_position[0] + SPEED, self._head_position[1])
        return grill

    def event_trigger(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.LEFT):
                if self._actual_head is not Movement.RIGHT:
                    self._next_head_movement.append(Movement.LEFT)
            elif event.key == pygame.K_RIGHT \
                    and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.RIGHT):
                if self._actual_head is not Movement.LEFT:
                    self._next_head_movement.append(Movement.RIGHT)
            elif event.key == pygame.K_UP \
                    and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.UP):
                if self._actual_head is not Movement.DOWN:
                    self._next_head_movement.append(Movement.UP)
            elif event.key == pygame.K_DOWN \
                    and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.DOWN):
                if self._actual_head is not Movement.UP:
                    self._next_head_movement.append(Movement.DOWN)
