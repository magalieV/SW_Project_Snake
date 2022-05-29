"""main_snake.py: File that all the game"""

import pygame
from menu_module.Menu import Menu
from menu_module.Ranking import Ranking
from menu_module.MenuRedirection import MenuRedirection
from game_module.gameplay.Snake import Snake
from save_module.GameSave import GameSave
from menu_module.Pause import Pause
from menu_module.GameOver import GameOver
from bot_module.Bot import BotSnake

__author__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


def pause_menu(menu_pause, window_state, last_state, save_game, snake_game):
    while window_state is MenuRedirection.PAUSE:
        last_state = window_state
        window_state = menu_pause.run_pause()
        pygame.display.update()

    if window_state is MenuRedirection.SAVE and snake_game is not None:
        save_game.save(snake_game, snake_game.apple)
        window_state = MenuRedirection.MENU
    return window_state, last_state


def solo_game(window_state, last_state, window, window_size, snake_game, save_game, menu_pause, ranking_score):
    if (window_state is MenuRedirection.PLAY or window_state is MenuRedirection.RESTART) and \
            last_state is not MenuRedirection.PLAY and last_state is not MenuRedirection.RESTART \
            and last_state is not MenuRedirection.LOAD and last_state is not MenuRedirection.RESUME:
        snake_game = Snake(window, window_size)
        window_state = MenuRedirection.PLAY
    have_played = False
    while window_state is MenuRedirection.PLAY or window_state is MenuRedirection.RESUME:
        have_played = True
        last_state = window_state
        window_state = snake_game.run_snake_game()
        window_state, last_state = pause_menu(menu_pause, window_state, last_state, save_game, snake_game)
        if window_state is MenuRedirection.RESTART:
            snake_game = Snake(window, window_size)
            window_state = MenuRedirection.PLAY
        clock.tick(15)
        pygame.display.update()

    if (have_played is True and last_state == MenuRedirection.PLAY or last_state == MenuRedirection.RESUME or
            last_state is MenuRedirection.PAUSE) \
            and window_state is not MenuRedirection.PLAY and window_state is not MenuRedirection.RESUME \
            and window_state is not MenuRedirection.PAUSE:
        ranking_score.save_ranking(snake_game.score())
    return snake_game, window_state, last_state


def multi_game(window_state, last_state, window, window_size, snake_game, save_game, pause_menu_multi):
    if (window_state is MenuRedirection.PLAY_MULTI or window_state is MenuRedirection.RESTART_MULTI) and \
            last_state is not MenuRedirection.PLAY_MULTI and last_state is not MenuRedirection.RESTART_MULTI \
            and last_state is not MenuRedirection.LOAD and last_state is not MenuRedirection.RESUME:
        snake_game = Snake(window, window_size, True)
        window_state = MenuRedirection.PLAY_MULTI

    while window_state is MenuRedirection.PLAY_MULTI or window_state is MenuRedirection.RESUME:
        last_state = window_state
        window_state = snake_game.run_snake_game()
        window_state, last_state = pause_menu(pause_menu_multi, window_state, last_state, save_game, snake_game)
        if window_state is MenuRedirection.RESTART:
            snake_game = Snake(window, window_size, True)
            window_state = MenuRedirection.PLAY_MULTI
        clock.tick(15)
        pygame.display.update()
    return snake_game, window_state, last_state


def end_game(window_game_over, window_state, last_state, snake_game, bot_game):
    if window_state is MenuRedirection.OVER and last_state is not MenuRedirection.OVER:
        window_game_over.play_sound_effect()
        if snake_game is not None:
            window_game_over.set_score_text(snake_game.get_result_board())
        else:
            window_game_over.set_score_text(bot_game.get_score())
    has_display = False

    while window_state is MenuRedirection.OVER:
        has_display = True
        last_state = window_state
        window_state = window_game_over.run_game_over()
        pygame.display.update()
    if has_display:
        return window_state, last_state, None, None
    else:
        return window_state, last_state, snake_game, bot_game


def auto_play(snake_bot, window_state, last_state, pause_menu_multi, window, window_size):
    if window_state is MenuRedirection.BOT and last_state is not MenuRedirection.BOT and last_state \
            is not MenuRedirection.LOAD and last_state is not MenuRedirection.RESUME:
        snake_bot = BotSnake(window, window_size)
        window_state = MenuRedirection.BOT

    tick_value = 20
    while window_state is MenuRedirection.BOT or window_state is MenuRedirection.RESUME:
        last_state = window_state
        window_state, tick_value = snake_bot.run_snake_game_bot()
        window_state, last_state = pause_menu(pause_menu_multi, window_state, last_state, save_game, None)
        if window_state is MenuRedirection.RESTART:
            snake_bot = BotSnake(screen, window_size)
            window_state = MenuRedirection.BOT
        clock.tick(tick_value)
        pygame.display.update()
    return snake_bot, window_state, last_state


if __name__ == '__main__':
    pygame.init()
    window_size = (1640, 840)
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
    menu_pause = Pause(screen, window_size)
    pause_menu_multi = Pause(screen, window_size, 200, [0, 1, 3])
    last_choice = MenuRedirection.MENU
    bot_snake = None

    while not game_over:
        if window_choice is MenuRedirection.MENU:
            window_choice = menu.run_menu()
        elif window_choice is MenuRedirection.RANKING:
            window_choice = ranking.run_ranking()
        elif window_choice is MenuRedirection.LOAD:
            snake = save_game.load(screen, window_size)
            if snake is None:
                window_choice = MenuRedirection.MENU
            else:
                window_choice = MenuRedirection.PLAY

        snake, window_choice, last_choice = solo_game(window_choice, last_choice, screen, window_size, snake, save_game, menu_pause, ranking)
        snake, window_choice, last_choice = multi_game(window_choice, last_choice, screen, window_size, snake, save_game, pause_menu_multi)
        bot_snake, window_choice, last_choice = auto_play(bot_snake, window_choice, last_choice, pause_menu_multi, screen, window_size)
        window_choice, last_choice, snake, bot_snake = end_game(game_over_window, window_choice, last_choice, snake, bot_snake)

        if window_choice is MenuRedirection.QUIT:
            game_over = True
            break
        if last_choice is not MenuRedirection.RANKING and window_choice is MenuRedirection.RANKING:
            ranking.load_ranking()
        if window_choice is MenuRedirection.MENU and last_choice is not MenuRedirection.MENU \
                and last_choice is not MenuRedirection.RANKING and last_choice is not MenuRedirection.LOAD:
            menu.load_and_play_music()
        last_choice = window_choice
        pygame.display.update()
    pygame.quit()
    quit()
