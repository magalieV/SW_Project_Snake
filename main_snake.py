"""main_snake.py: File that all the game"""

import pygame
from menu.Menu import Menu
from menu.Ranking import Ranking
from menu.MenuRedirection import MenuRedirection

__author__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

#def game():
#    for event in pygame.event.get():
#        snake.event_trigger(event)
#        if event.type == pygame.QUIT:
#            game_over = True
#    if snake.collide(apples) == CollideType.BORDER:
#        game_over = True
#        break
#    snake.update()
#    screen.fill((0, 0, 0))
#    apples.display()
#    snake.display()


if __name__ == '__main__':
    pygame.init()
    window_size = (990, 540)
    screen = pygame.display.set_mode(window_size)
    pygame.display.update()
    pygame.display.set_caption('Snake game Magalie Vandenbriele, Pierre Ghyzel, Irama Chaouch')
    game_over = False
    clock = pygame.time.Clock()

    window_choice = MenuRedirection.MENU

    menu = Menu(window_size, screen)
    menu.init()
    ranking = Ranking(window_size, screen)
    ranking.init()

    while not game_over:
        if window_choice is MenuRedirection.MENU:
            window_choice = menu.run_menu()
        elif window_choice is MenuRedirection.RANKING:
            window_choice = ranking.run_ranking()
        if window_choice is MenuRedirection.QUIT:
            game_over = True
            break
        pygame.display.update()
        #clock.tick(8)
    pygame.quit()
    quit()
