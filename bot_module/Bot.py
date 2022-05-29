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
    tick_start = 20

    def __init__(self, window, window_size):
        self._window = window
        sys.setrecursionlimit(6400)
        self._window_size = window_size
        self.snake_game = Snake(window, window_size)
        self.init_map()

    def init_map(self):
        del self.map[:]
        for i in range(0, 42):
            self.map.append([])
            for j in range(0, 82):
                if j == 0 or j == 81:
                    self.map[i].append(-5)
                elif i == 0 or i == 41:
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
            if self.apple_position_x > actual_position_x:
                order_possible.append(Movement.RIGHT)
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.UP)
            else:
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.RIGHT)
                order_possible.append(Movement.UP)
        elif self.apple_position_y < actual_position_y:
            order_possible.append(Movement.UP)
            if self.apple_position_x > actual_position_x:
                order_possible.append(Movement.RIGHT)
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.DOWN)
            else:
                order_possible.append(Movement.LEFT)
                order_possible.append(Movement.RIGHT)
                order_possible.append(Movement.DOWN)
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

    def find_one_possible_movement(self, actual_position_x, actual_position_y, mvt):
        order_possible = self.set_order_possible(actual_position_x, actual_position_y)
        if mvt is Movement.UP:
            order_possible.remove(Movement.DOWN)
        elif mvt is Movement.DOWN:
            order_possible.remove(Movement.UP)
        elif mvt is Movement.LEFT:
            order_possible.remove(Movement.RIGHT)
        else:
            order_possible.remove(Movement.LEFT)
        for element in order_possible:
            new_position_x = actual_position_x
            new_position_y = actual_position_y
            if element is Movement.DOWN:
                new_position_y += 1
            elif element is Movement.UP:
                new_position_y -= 1
            elif element is Movement.LEFT:
                new_position_x -= 1
            elif element is Movement.RIGHT:
                new_position_x += 1
            if new_position_y < 0 or new_position_y > 41 or new_position_x < 0 or new_position_x > 81:
                continue
            if self.map[new_position_y][new_position_x] == 3 or self.map[new_position_y][new_position_x] == 0:
                return element
        return order_possible[0]

    def find_possible_movement(self, mvt, actual_position_x, actual_position_y, list_mvt, counter, first_recursion):
        order_possible = self.set_order_possible(actual_position_x, actual_position_y)
        if mvt is Movement.UP:
            order_possible.remove(Movement.DOWN)
        elif mvt is Movement.DOWN:
            order_possible.remove(Movement.UP)
        elif mvt is Movement.LEFT:
            order_possible.remove(Movement.RIGHT)
        else:
            order_possible.remove(Movement.LEFT)
        for element in order_possible:
            new_position_x = actual_position_x
            new_position_y = actual_position_y
            end = False
            counter += 1
            if element is Movement.DOWN:
                new_position_y += 1
            elif element is Movement.UP:
                new_position_y -= 1
            elif element is Movement.LEFT:
                new_position_x -= 1
            elif element is Movement.RIGHT:
                new_position_x += 1
            if new_position_y < 0 or new_position_y > 41 or new_position_x < 0 or new_position_x > 81:
                continue
            elif self.map[new_position_y][new_position_x] == 0:
                self.map[new_position_y][new_position_x] = 4
                list_mvt.append(element)
                if counter > 750:
                    return True, list_mvt, counter
                end, list_mvt, counter = self.find_possible_movement(element, new_position_x, new_position_y, list_mvt, counter, first_recursion + 1)
                if end is False:
                    list_mvt.pop()
                    self.map[new_position_y][new_position_x] = 0
            elif self.map[new_position_y][new_position_x] == 3:
                list_mvt.append(element)
                end = True
            if end:
                if first_recursion == 0 and len(list_mvt) <= 0:
                    list_mvt.append(self.find_one_possible_movement(actual_position_x, actual_position_y, mvt))
                return True, list_mvt, counter
        return False, list_mvt, counter

    def run_snake_game_bot(self):
        final_tick = round(len(self.snake_game.snake_body.body_part) / 10) + self.tick_start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return MenuRedirection.QUIT, final_tick
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return MenuRedirection.PAUSE, final_tick
        self.init_map()
        mvt = []
        state, mvt, tmp = self.find_possible_movement(self.snake_game.snake_head.actual_head,
                                                 self.head_position_x, self.head_position_y, mvt, 0, 0)
        if state is not None and len(mvt) > 0:
            self.snake_game.snake_head.next_head_movement.append(mvt[0])
        else:
            self.snake_game.snake_head.next_head_movement.append(self.find_one_possible_movement(self.head_position_x, self.head_position_y, mvt))
        self.snake_game.update()
        state = self.snake_game.collide(self.snake_game.apple)
        if state is CollideType.BORDER:
            return MenuRedirection.OVER, final_tick
        self.snake_game.display()
        return MenuRedirection.BOT, final_tick

    def get_score(self):
        return self.snake_game.get_result_board()
