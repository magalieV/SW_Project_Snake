"""Bot.py: File that handle the bot"""

import pygame
import sys
from game_module.gameplay.Snake import Snake
from game_module.gameplay.Enumerations import Movement, CollideType
from menu_module.MenuRedirection import MenuRedirection

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class BotSnake:
    map = []
    case_size = 20
    head_position_x = 0
    head_position_y = 0
    apple_position_x = 0
    apple_position_y = 0

    def __init__(self, window, window_size):
        self._window = window
        sys.setrecursionlimit(6400)
        self._window_size = window_size
        self.snake_game = Snake(window, window_size)
        self.init_map()

    def init_map(self):
        del self.map[:]
        for i in range(0, 80):
            self.map.append([])
            for j in range(0, 80):
                if j == 0 or j == 79:
                    self.map[i].append(-5)
                elif i == 0 or i == 79:
                    self.map[i].append(-5)
                else:
                    self.map[i].append(0)
        head_position = self.snake_game.snake_head.head_position
        self.head_position_x = int(head_position[0] / self.case_size)
        self.head_position_y = int(head_position[1] / self.case_size)
        self.map[self.head_position_y][self.head_position_x] = 1
        body_parts = self.snake_game.snake_body.body_part
        for part in body_parts:
            x = int(part.x / self.case_size)
            y = int(part.y / self.case_size)
            self.map[y][x] = 2
        apple_position = self.snake_game.apple.position
        self.apple_position_x = int(apple_position[0] / self.case_size)
        self.apple_position_y = int(apple_position[1] / self.case_size)
        self.map[self.apple_position_y][self.apple_position_x] = 3

    def set_order_possible(self, actual_position_x, actual_position_y):
        order_possible = []
        if self.apple_position_y > actual_position_y:
            order_possible.append(Movement.DOWN)
            if self.apple_position_x < actual_position_x:
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.UP)
                order_possible.append(Movement.RIGHT)
            elif self.apple_position_x > actual_position_x:
                order_possible.append(Movement.RIGHT)
                order_possible.append(Movement.UP)
                order_possible.append(Movement.LEFT)
            else:
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.UP)
                order_possible.append(Movement.RIGHT)
        elif self.apple_position_y < actual_position_y:
            order_possible.append(Movement.UP)
            if self.apple_position_x < actual_position_x:
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.DOWN)
                order_possible.append(Movement.RIGHT)
            elif self.apple_position_x > actual_position_x:
                order_possible.append(Movement.RIGHT)
                order_possible.append(Movement.DOWN)
                order_possible.append(Movement.LEFT)
            else:
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.DOWN)
                order_possible.append(Movement.RIGHT)
        elif self.apple_position_x < actual_position_x:
            order_possible.append(Movement.LEFT)
            order_possible.append(Movement.UP)
            order_possible.append(Movement.DOWN)
            order_possible.append(Movement.RIGHT)
        else:
            order_possible.append(Movement.RIGHT)
            order_possible.append(Movement.UP)
            order_possible.append(Movement.DOWN)
            order_possible.append(Movement.LEFT)
        return order_possible

    def find_possible_movement(self, mvt, actual_position_x, actual_position_y, list_mvt):
        order_possible = self.set_order_possible(actual_position_x, actual_position_y)
        for element in order_possible:
            if (mvt is Movement.UP and element is Movement.DOWN) or\
                    mvt is Movement.DOWN and element is Movement.UP or\
                    mvt is Movement.LEFT and element is Movement.RIGHT or\
                    mvt is Movement.RIGHT and element is Movement.LEFT:
                continue
            new_position_x = actual_position_x
            new_position_y = actual_position_y
            end = False
            if element is Movement.DOWN:
                new_position_y += 1
            elif element is Movement.UP:
                new_position_y -= 1
            elif element is Movement.LEFT:
                new_position_x -= 1
            elif element is Movement.RIGHT:
                new_position_x += 1
            if new_position_y < 0 or new_position_y > 79 or new_position_x < 0 or new_position_x > 79:
                continue
            elif self.map[new_position_y][new_position_x] == 0:
                self.map[new_position_y][new_position_x] = 4
                list_mvt.append(element)
                end, list_mvt = self.find_possible_movement(element, new_position_x, new_position_y, list_mvt)
                if end is False:
                    list_mvt.pop()
                    self.map[new_position_y][new_position_x] = 0
            elif self.map[new_position_y][new_position_x] == 3:
                list_mvt.append(element)
                end = True
            if end:
                return True, list_mvt
        return False, list_mvt

    def test(self):
        mvt = []
        self.init_map()
        state, mvt = self.find_possible_movement(self.snake_game.snake_head.actual_head,
                                                 self.head_position_x, self.head_position_y, mvt)
        for index in self.map:
            print(index)
        print(mvt)
        print(state)

    def run_snake_game_bot(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return MenuRedirection.QUIT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return MenuRedirection.PAUSE
        self.init_map()
        mvt = []
        state, mvt = self.find_possible_movement(self.snake_game.snake_head.actual_head,
                                                 self.head_position_x, self.head_position_y, mvt)
        if state is not None and len(mvt) > 0:
            self.snake_game.snake_head.next_head_movement.append(mvt[0])
        else:
            self.snake_game.snake_head.next_head_movement.append(Movement.UP)
        self.snake_game.update()
        state = self.snake_game.collide(self.snake_game.apple)
        if state is CollideType.BORDER:
            return MenuRedirection.OVER
        self.snake_game.display()
        return MenuRedirection.BOT

