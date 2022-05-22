"""Snake.py: File that handle the snake display and movement"""

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
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Snake:
    corners = []
    snake_head = None
    snake_body = None
    apple = None
    map = None
  #  score_disp = None

    def __init__(self, window, window_size, snake_head_save=None, snake_body_save=None, corner_save=None, apple_save=None):
        self._window = window
        self._window_size = window_size
        self.map = Map(window, 40, 40)
        self.eat_apple = pygame.mixer.Sound(
            "game_module/assets/sound/apple_sound.mp3")
        self.eat_apple.set_volume(1)
        self.turn_sound = pygame.mixer.Sound(
            "game_module/assets/sound/turn_sound.mp3")
        self.turn_sound.set_volume(1)
        pygame.mixer.music.load("game_module/assets/sound/game_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        if snake_head_save is None:
            self.snake_head = SnakeHead(window, window_size)
            self.snake_body = SnakeBody(window, window_size)
            self.apple = Apple(window, window_size)
            self.apple.generate(self.snake_body.body_part,
                                self.snake_head.head_position)
        else:
            self.snake_head = snake_head_save
            self.snake_body = snake_body_save
            self.corners = corner_save
            self.apple = apple_save
        self.score_disp = ScoreGame(window)
        self.score_disp.set_score(len(self.snake_body.body_part) - 1)

    def score(self):
        return len(self.snake_body.body_part) - 1

    def display(self):
        self.map.display()
        self.score_disp.display()
        self.apple.display()
        self.snake_head.display()
        self.snake_body.display()

    def event_trigger(self, evnt, bot):
        if bot != None:
            if self.snake_head.algo(self.apple):
                self.turn_sound.play()
        else:
            if self.snake_head.event_trigger(evnt):
                self.turn_sound.play()

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

    def update(self):
        new_corner = self.snake_head.update()
        if new_corner is not None:
            self.corners.append(new_corner)
        self.corners = self.snake_body.update(self.corners)

    def run_snake_game(self, bot=None):
        if bot != None:
            self.event_trigger(0, bot)
        for event in pygame.event.get():
            if bot == None:
                self.event_trigger(event, bot)
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return MenuRedirection.QUIT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return MenuRedirection.PAUSE
        self.update()
        state = self.collide(self.apple)
        if state is CollideType.BORDER:
            return MenuRedirection.OVER
        self.display()
        return MenuRedirection.PLAY
