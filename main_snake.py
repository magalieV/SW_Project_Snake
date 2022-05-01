"""main_snake.py: File that all the game"""

import pygame
from menu.Menu import Menu
from menu.Ranking import Ranking
from menu.MenuRedirection import MenuRedirection
from game_module.gameplay.Snake import Snake
from save_module.GameSave import GameSave
from menu.Pause import Pause
from menu.GameOver import GameOver

__author__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

if __name__ == '__main__':
    pygame.init()
    window_size = (840, 840)
    screen = pygame.display.set_mode(window_size)
    pygame.display.update()
    pygame.display.set_caption('Snake game Magalie Vandenbriele, Pierre Ghyzel, Irama Chaouch')
    game_over = False
    clock = pygame.time.Clock()

    window_choice = MenuRedirection.MENU
    snake = None

    game_over_window = GameOver(screen, window_size)
    game_over_window.init()

    menu = Menu(screen, window_size)
    menu.load_and_play_music()
    ranking = Ranking(window_size, screen)
    ranking.init()
    save_game = GameSave()
    pause_menu = Pause(screen, window_size)
    last_choice = MenuRedirection.MENU

    while not game_over:
        if window_choice is MenuRedirection.MENU:
            window_choice = menu.run_menu()
        elif window_choice is MenuRedirection.RANKING:
            window_choice = ranking.run_ranking()
        elif window_choice is MenuRedirection.PLAY or window_choice is MenuRedirection.RESUME:
            window_choice = snake.run_snake_game()
            clock.tick(10)
        elif window_choice is MenuRedirection.LOAD:
            snake = save_game.load(screen, window_size)
            if snake is None:
                window_choice = MenuRedirection.MENU
            else:
                window_choice = MenuRedirection.PLAY
        elif window_choice is MenuRedirection.PAUSE:
            window_choice = pause_menu.run_pause()
        elif window_choice is MenuRedirection.OVER:
            window_choice = game_over_window.run_game_over()
        elif window_choice is MenuRedirection.SAVE and snake is not None:
            save_game.save(snake, snake.apple)
            window_choice = MenuRedirection.MENU

        if window_choice is MenuRedirection.QUIT:
            game_over = True
            break

        if window_choice is MenuRedirection.OVER and last_choice is not MenuRedirection.OVER:
            game_over_window.play_sound_effect()

        if last_choice is not MenuRedirection.RANKING and window_choice is MenuRedirection.RANKING:
            ranking.load_ranking()

        if window_choice is MenuRedirection.OVER and last_choice is not MenuRedirection.OVER:
            game_over_window.set_score(snake.score())

        if window_choice is MenuRedirection.MENU and last_choice is not MenuRedirection.MENU \
                and last_choice is not MenuRedirection.RANKING and last_choice is not MenuRedirection.LOAD:
            menu.load_and_play_music()

        if (last_choice == MenuRedirection.PLAY or last_choice == MenuRedirection.RESUME or last_choice is MenuRedirection.PAUSE) \
                and window_choice is not MenuRedirection.PLAY and window_choice is not MenuRedirection.RESUME \
                and window_choice is not MenuRedirection.PAUSE:
            ranking.save_ranking(snake.score())
        if (window_choice is MenuRedirection.PLAY or window_choice is MenuRedirection.RESTART) and \
                last_choice is not MenuRedirection.PLAY and last_choice is not MenuRedirection.RESTART \
                and last_choice is not MenuRedirection.LOAD and last_choice is not MenuRedirection.RESUME:
            snake = Snake(screen, window_size)
            window_choice = MenuRedirection.PLAY
        last_choice = window_choice
        pygame.display.update()
    pygame.quit()
    quit()
