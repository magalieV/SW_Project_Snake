"""Snake.py: File that handle the snake display and movement"""

import pygame
from enum import Enum
from Apple import Apple

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Movement(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake:
    def __init__(self, screen, screen_size):
        self._heads = {}
        self._screen = screen
        self._actual_head = Movement.UP
        self._body_size = 1
        self._sprite_size = 32
        number_of_square_width = round(screen_size[0] / 32)
        number_of_square_height = round(screen_size[1] / 32)
        self._next_head_movement = []
        self._head_position = ((number_of_square_width / 2 * 32), (number_of_square_height / 2 * 32))
        self._heads[Movement.UP] = pygame.image.load("assets/snake/head_up.png").convert()
        self._heads[Movement.DOWN] = pygame.image.load("assets/snake/head_down.png").convert()
        self._heads[Movement.LEFT] = pygame.image.load("assets/snake/head_left.png").convert()
        self._heads[Movement.RIGHT] = pygame.image.load("assets/snake/head_right.png").convert()

    def collide(self, screen_size, apple):
        if self._head_position[0] < 0 or (self._head_position[0] + self._sprite_size) > screen_size[0] \
                or self._head_position[1] < 0 or (self._head_position[1] + self._sprite_size) > screen_size[1]:
            return True
        self.collide_apple(apple)
        return False

    def collide_apple(self, apple):
        middle_snake_x = self._head_position[0] + (self._sprite_size / 2)
        middle_snake_y = self._head_position[1] + (self._sprite_size / 2)
        middle_apple_x = apple.position[0] + (apple.sprite_size / 2)
        middle_apple_y = apple.position[1] + (apple.sprite_size / 2)
        if middle_snake_x == middle_apple_x and middle_snake_y == middle_apple_y:
            self._body_size += 1
            apple.generate()

    def display(self):
        self._screen.blit(self._heads[self._actual_head], self._head_position)
        pygame.display.update()

    def update(self):
        square_x = self._head_position[0] / 32
        square_y = self._head_position[1] / 32
        if square_x.is_integer() and square_y.is_integer() and len(self._next_head_movement) > 0:
            tmp = self._next_head_movement.pop(0)
            while tmp == self._actual_head:
                tmp = self._next_head_movement.pop(0)
            self._actual_head = tmp
        if self._actual_head == Movement.UP:
            self._head_position = (self._head_position[0], self._head_position[1] - 4)
        elif self._actual_head == Movement.DOWN:
            self._head_position = (self._head_position[0], self._head_position[1] + 4)
        elif self._actual_head == Movement.LEFT:
            self._head_position = (self._head_position[0] - 4, self._head_position[1])
        elif self._actual_head == Movement.RIGHT:
            self._head_position = (self._head_position[0] + 4, self._head_position[1])

    def event_trigger(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.LEFT):
                if self._actual_head == Movement.RIGHT:
                    self._actual_head = Movement.LEFT
                else:
                    self._next_head_movement.append(Movement.LEFT)
            elif event.key == pygame.K_RIGHT \
                    and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.RIGHT):
                if self._actual_head == Movement.LEFT:
                    self._actual_head = Movement.RIGHT
                else:
                    self._next_head_movement.append(Movement.RIGHT)
            elif event.key == pygame.K_UP \
                    and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.UP):
                if self._actual_head == Movement.DOWN:
                    self._actual_head = Movement.UP
                else:
                    self._next_head_movement.append(Movement.UP)
            elif event.key == pygame.K_DOWN \
                    and (len(self._next_head_movement) == 0 or self._next_head_movement[0] != Movement.DOWN):
                if self._actual_head == Movement.UP:
                    self._actual_head = Movement.DOWN
                else:
                    self._next_head_movement.append(Movement.DOWN)


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
        snake.update()
        if snake.collide(windows_size, apples):
            game_over = True
        screen.fill((0, 0, 0))
        apples.display()
        snake.display()
        clock.tick(30)
    pygame.quit()
    quit()
