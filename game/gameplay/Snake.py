"""Snake.py: File that handle the snake display and movement"""

import pygame
from SnakeHead import SnakeHead
from Apple import Apple
from SnakeBody import SnakeBody
from Enumerations import CollideType

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Snake:
    def __init__(self, window, window_size):
        self._snake_head = SnakeHead(window, window_size)
        self._snake_body = SnakeBody(window, window_size)
        self._corners = []

    def display(self):
        self._snake_head.display()
        self._snake_body.display()

    def event_trigger(self, evnt):
        self._snake_head.event_trigger(evnt)

    def collide(self, apple):
        collide_type = self._snake_head.collide(apple)
        if collide_type == CollideType.APPLE:
            self._snake_body.add_body()
        return collide_type

    def update(self):
        new_corner = self._snake_head.update()
        if new_corner is not None:
            self._corners.append(new_corner)
        self._corners = self._snake_body.update(self._corners)




if __name__ == '__main__':
    pygame.init()
    windows_size = (640, 320)
    screen = pygame.display.set_mode(windows_size)
    pygame.display.update()
    pygame.display.set_caption('Snake game Magalie Vandenbriele, Pierre Ghyzel, Irama Chaouch')
    game_over = False
    clock = pygame.time.Clock()
    snake = Snake(screen, windows_size)
    apples = Apple(windows_size, screen)
    while not game_over:
        for event in pygame.event.get():
            snake.event_trigger(event)
            if event.type == pygame.QUIT:
                game_over = True
        if snake.collide(apples) == CollideType.BORDER:
            game_over = True
            break
        snake.update()
        screen.fill((0, 0, 0))
        apples.display()
        snake.display()
        pygame.display.update()
        clock.tick(20)
    pygame.quit()
    quit()
