"""Snake.py: File that handle the snake display and movement"""
import sys

import pygame
from game_module.gameplay.SnakeHead import SnakeHead
from game_module.gameplay.Apple import Apple
from game_module.gameplay.SnakeBody import SnakeBody
from game_module.gameplay.Enumerations import CollideType
from menu_module.MenuRedirection import MenuRedirection
from interface_module.Map import Map
from interface_module.Score import ScoreGame

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = ["Magalie Vandenbriele", "Irama Chaouch"]
__email__ = "magalie.vandenbriele@epitech.eu"


class Snake:
    corners = []
    snake_head = None
    snake_body = None
    apple = None
    map = None
    second_snake_head = None
    second_snake_body = None
    second_corners = []
    second_apple = None
    multi = None
    score_disp = None

    def __init__(self, window, window_size, multi=None, snake_head_save=None, snake_body_save=None, corner_save=None, apple_save=None):
        self._window = window
        self._loser = 1
        self._window_size = window_size
        self.eat_apple = pygame.mixer.Sound(
            "game_module/assets/sound/apple_sound.mp3")
        self.eat_apple.set_volume(1)
        self.turn_sound = pygame.mixer.Sound(
            "game_module/assets/sound/turn_sound.mp3")
        self.turn_sound.set_volume(1)
        pygame.mixer.music.load("game_module/assets/sound/game_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        self.map = Map(window, 80, 40)
        if snake_head_save is None:
            if multi is None:
                self.snake_head = SnakeHead(window, window_size)
                self.snake_body = SnakeBody(window, window_size)
                self.apple = Apple(window, window_size)
                self.apple.generate(self.snake_body.body_part,
                                    self.snake_head.head_position)
            else:
                self.multi = True
                self.snake_head = SnakeHead(self._window, window_size, 1)
                self.snake_body = SnakeBody(self._window, window_size, 1)
                self.second_snake_head = SnakeHead(
                    self._window, window_size, 2)
                self.second_snake_body = SnakeBody(
                    self._window, window_size, 2)
                self.second_apple = Apple(self._window, window_size)
                self.apple = Apple(self._window, window_size)
                self.apple.generate_multi(self.snake_body.body_part, self.snake_head.head_position,
                                          self.second_snake_body.body_part, self.second_snake_head.head_position, (0, 0))
                self.second_apple.generate_multi(self.snake_body.body_part, self.snake_head.head_position,
                                                 self.second_snake_body.body_part, self.second_snake_head.head_position, self.apple.position)
        else:
            self.snake_head = snake_head_save
            self.snake_body = snake_body_save
            self.corners = corner_save
            self.apple = apple_save
        if multi is None:
            self.score_disp = ScoreGame(self._window)
            self.score_disp.set_score(len(self.snake_body.body_part) - 1)

        def get_result_board(self):
            if self.multi is None:
                return str(len(self.snake_body.body_part) - 1)
            elif self._loser == 2:
                if len(sys.argv) < 2:
                    return "Player 1"
                else:
                    return sys.argv[1]
            elif self._loser == 1:
                if len(sys.argv) < 3:
                    return "Player 2"
                return sys.argv[2]

    def score(self):
        return len(self.snake_body.body_part) - 1

    def display(self):
        self.map.display()
        self.apple.display()
        if self.multi is not None:
            self.second_apple.display()
            self.second_snake_head.display()
            self.second_snake_body.display()
        else:
            self.score_disp.display()
        self.snake_head.display()
        self.snake_body.display()

    def event_trigger(self, evnt):
        if self.snake_head.event_trigger(evnt):
            self.turn_sound.play()
        if self.multi is not None:
            if self.second_snake_head.event_trigger_player_two(evnt):
                self.turn_sound.play()

    def collide_apple_multi(self, apple, snake_head, snake_body, second_apple):
        collide_type = snake_head.collide(apple)
        if collide_type == CollideType.APPLE:
            self.eat_apple.play()
            apple.generate_multi(self.snake_body.body_part, self.snake_head.head_position, self.second_snake_body.body_part,
                                 self.second_snake_head.head_position, second_apple.position)
            snake_body.add_body()
        return collide_type

    def collide(self, apple):
        collide_type = self.snake_head.collide(apple)
        if collide_type == CollideType.APPLE:
            self.score_disp.score_up()
            self.eat_apple.play()
            self.apple.generate(self.snake_body.body_part,
                                self.snake_head.head_position)
            self.snake_body.add_body()
        for part in self.snake_body.body_part:
            if part.collide(self.snake_head.head_position):
                return CollideType.BORDER
        return collide_type

    def collide_two_player(self):
        if self.collide_apple_multi(self.apple, self.snake_head, self.snake_body, self.second_apple) is CollideType.BORDER\
                or self.collide_apple_multi(self.second_apple, self.snake_head, self.snake_body, self.apple)\
                is CollideType.BORDER:
            self._loser = 1
            return CollideType.BORDER
        if self.collide_apple_multi(self.apple, self.second_snake_head, self.second_snake_body, self.second_apple) is CollideType.BORDER\
                or self.collide_apple_multi(self.second_apple, self.second_snake_head, self.second_snake_body, self.apple)\
                is CollideType.BORDER:
            self._loser = 2
            return CollideType.BORDER
        collide_type = CollideType.NONE
        for part in self.snake_body.body_part:
            if part.collide(self.snake_head.head_position):
                self._loser = 1
                return CollideType.BORDER
            if part.collide(self.second_snake_head.head_position):
                self._loser = 2
                return CollideType.BORDER
        for part in self.second_snake_body.body_part:
            if part.collide(self.second_snake_head.head_position):
                self._loser = 2
                return CollideType.BORDER
            if part.collide(self.snake_head.head_position):
                self._loser = 1
                return CollideType.BORDER
        return collide_type

    def update(self):
        new_corner = self.snake_head.update()
        if new_corner is not None:
            self.corners.append(new_corner)
        self.corners = self.snake_body.update(self.corners)
        if self.multi is not None:
            new_second_corner = self.second_snake_head.update()
            if new_second_corner is not None:
                self.second_corners.append(new_second_corner)
            self.second_corners = self.second_snake_body.update(
                self.second_corners)

    def run_snake_game(self):
        for event in pygame.event.get():
            self.event_trigger(event)
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return MenuRedirection.QUIT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return MenuRedirection.PAUSE
        self.update()
        if self.multi is None:
            state = self.collide(self.apple)
        else:
            state = self.collide_two_player()
        if state is CollideType.BORDER:
            return MenuRedirection.OVER
        self.display()
        if self.multi is not None:
            return MenuRedirection.PLAY_MULTI
        return MenuRedirection.PLAY
