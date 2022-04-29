"""GameSave.py: File that handle the save of the game"""

from game.gameplay.Snake import Snake
from game.gameplay.SnakeHead import SnakeHead
from game.gameplay.SnakeBody import SnakeBody
from game.gameplay.Settings import Grill
from game.gameplay.Enumerations import Movement
from game.gameplay.Apple import Apple

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class SavingState:
    HEAD = 1
    BODY = 2
    CORNER = 3
    APPLE = 4


class GameSave:
    def __init__(self):
        self._file_path = "save.txt"

    def save(self, snake, apple):
        with open(self._file_path, "w") as file_output:
            file_output.write("HEAD\n")
            file_output.write(snake.snake_head.get_head_info().to_write_str())
            body_parts = snake.snake_body.body_part
            file_output.write("BODY\n")
            for part in body_parts:
                file_output.write(part.to_write_str())
            file_output.write("CORNERS\n")
            corners = snake.corners
            for corner in corners:
                file_output.write(corner.to_write_str())
            file_output.write("APPLE\n")
            file_output.write(str(apple.position[0]) + "," + str(apple.position[1]))

    def load(self, window, window_size):
        snake_head = None
        snake_body = None
        corner = []
        snake_body_part = []
        apple_position = None
        with open(self._file_path, "r") as file_input:
            lines = file_input.readlines()
            state = SavingState.HEAD
            for line in lines:
                line = line.strip()
                if line == "HEAD":
                    state = SavingState.HEAD
                elif line == "BODY":
                    state = SavingState.BODY
                elif line == "CORNERS":
                    state = SavingState.CORNER
                elif line == "APPLE":
                    state = SavingState.APPLE
                elif state == SavingState.HEAD:
                    info = line.split(',')
                    snake_head = SnakeHead(window, window_size, Movement(int(info[0])), (float(info[1]), float(info[2])))
                elif state == SavingState.BODY:
                    info = line.split(',')
                    snake_body_part.append(Grill(Movement(int(info[0])), float(info[1]), float(info[2])))
                elif state == SavingState.CORNER:
                    info = line.split(',')
                    corner.append(Grill(Movement(int(info[0])), float(info[1]), float(info[2])))
                elif state is SavingState.APPLE:
                    info = line.split(',')
                    apple_position = (float(info[0]), float(info[1]))
        snake_body = SnakeBody(window, window_size, snake_body_part)
        return Snake(window, window_size, snake_head, snake_body, corner), Apple(window, window_size, apple_position)


