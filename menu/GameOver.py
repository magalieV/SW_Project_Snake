"""GameOver.py: File that handle the display of the GameOver screen"""


"""Import statement go there"""


from defer import return_value
from pygame.locals import *
import pygame
from Menu import *
__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class GameOver:
    def __init__(self):
        self.to_another_screen = MenuRedirection.GAMEOVER

        self.size = width, height = 1920, 1080

        self.screen = pygame.display.set_mode(self.size)

        self.background = pygame.image.load("assets/background.jpg")
        self.font_btn = pygame.font.Font("assets/Granjon.otf", 120)
        self.color_btn_text = (81, 73, 41)
        self.color_btn_bg = (8, 29, 30)
        self.color_btn_text_trigger = (113, 12, 26)

        self.text_game_over = self.font_btn.render(
            'GAME OVER', True, self.color_btn_text)
        self.text_to_menu = self.font_btn.render(
            'GO TO MENU', True, self.color_btn_text)
        self.text_quit = self.font_btn.render(
            'QUIT GAME', True, self.color_btn_text)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def load_and_play_music(self):
        pygame.mixer.music.load("assets/gameOver.mp3")
        pygame.mixer.music.play(-1)

    def init_rect(self):
        self.rect_game_over = Rect(self.width/3 + 50, 100, 600, 150)
        self.rect_to_menu = Rect(self.width/3, 520, 800, 150)
        self.rect_quit = Rect(self.width/3 + 200, 820, 300, 150)

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color_btn_bg,
                         self.rect_game_over, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rect_quit, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rect_to_menu, 1)

    def draw_text(self):
        self.screen.blit(self.text_game_over, (self.width/3 + 50, 100))
        self.screen.blit(self.text_to_menu, (self.width/3, 520))
        self.screen.blit(self.text_quit, (self.width/3 + 200, 820))

    def collide_point(self, mouse):
        if Rect.collidepoint(self.rect_to_menu, mouse):
            self.text_to_menu = self.font_btn.render(
                'GO TO MENU', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rect_quit, mouse):
            self.text_quit = self.font_btn.render(
                'QUIT', True, self.color_btn_text_trigger)
        else:
            self.text_to_menu = self.font_btn.render(
                'GO TO MENU', True, self.color_btn_text)
            self.text_quit = self.font_btn.render(
                'QUIT', True, self.color_btn_text)

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Rect.collidepoint(self.rect_to_menu, mouse):
                    return MenuRedirection.MENU
                elif Rect.collidepoint(self.rect_quit, mouse):
                    return MenuRedirection.QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
        return self.to_another_screen

    def init(self):
        self.load_and_play_music()
        self.init_rect()
        self.draw_rect()

    def run_game_over(self):
        mouse = pygame.mouse.get_pos()
        self.screen.blit(self.background, (0, 0))

        self.draw_text()
        self.collide_point(mouse)
        self.to_another_screen = self.event_trigger(mouse)
        if self.to_another_screen != MenuRedirection.GAMEOVER:
            return self.to_another_screen


def start_gameover():
    game_over = GameOver()
    # add this function before the game loop
    game_over.init()
    # add this function in the game loop
    game_over.run_game_over()
    #
    # if game_over.to_another_screen == MenuRedirection.MENU:
    #     Menu.init()
    #     Menu.run_menu()


if __name__ == '__main__':
    start_gameover()
