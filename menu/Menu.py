"""Menu.py: File that handle the display of the menu"""

from pygame.locals import *
import pygame
from menu.Ranking import Ranking
from menu.MenuRedirection import MenuRedirection

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Menu:
    def __init__(self, window_size, window):
        self.to_another_screen = MenuRedirection.MENU

        self.size = width, height = 1920, 1080

        self.screen = window

        self.background = pygame.image.load("menu/assets/background.jpg")
        self.font_btn = pygame.font.Font("menu/assets/Granjon.otf", 120)
        self.color_btn_text = (81, 73, 41)
        self.color_btn_bg = (8, 29, 30)
        self.color_btn_text_trigger = (113, 12, 26)

        self.text_play = self.font_btn.render(
            'PLAY', True, self.color_btn_text)
        self.text_load = self.font_btn.render(
            'LOAD', True, self.color_btn_text)
        self.text_ranking = self.font_btn.render(
            'RANKING', True, self.color_btn_text)
        self.text_exit = self.font_btn.render(
            'EXIT', True, self.color_btn_text)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def load_and_play_music(self):
        pygame.mixer.music.load("menu/assets/menu_music.mp3")
        pygame.mixer.music.play(-1)

    def init_rect(self):
        self.rectPlay = Rect(self.width/3 + 125, 120, 300, 150)
        self.rectLoad = Rect(self.width/3 + 125, 320, 300, 150)
        self.rectRanking = Rect(self.width/3, 520, 600, 150)
        self.rectExit = Rect(self.width/3 + 125, 720, 300, 150)

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectPlay, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectLoad, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectRanking, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectExit, 1)

    def draw_text(self):
        self.screen.blit(self.text_play, (self.width/3 + 125, 120))
        self.screen.blit(self.text_load, (self.width/3 + 125, 320))
        self.screen.blit(self.text_ranking, (self.width/3, 520))
        self.screen.blit(self.text_exit, (self.width/3 + 125, 720))

    def collide_point(self, mouse):
        if Rect.collidepoint(self.rectPlay, mouse):
            self.text_play = self.font_btn.render(
                'PLAY', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rectLoad, mouse):
            self.text_load = self.font_btn.render(
                'LOAD', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rectRanking, mouse):
            self.text_ranking = self.font_btn.render(
                'RANKING', True, self.color_btn_text_trigger)
        elif Rect.collidepoint(self.rectExit, mouse):
            self.text_exit = self.font_btn.render(
                'EXIT', True, self.color_btn_text_trigger)
        else:
            self.text_play = self.font_btn.render(
                'PLAY', True, self.color_btn_text)
            self.text_load = self.font_btn.render(
                'LOAD', True, self.color_btn_text)
            self.text_ranking = self.font_btn.render(
                'RANKING', True, self.color_btn_text)
            self.text_exit = self.font_btn.render(
                'EXIT', True, self.color_btn_text)

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Rect.collidepoint(self.rectPlay, mouse):
                    return MenuRedirection.PLAY
                elif Rect.collidepoint(self.rectLoad, mouse):
                    return MenuRedirection.LOAD
                elif Rect.collidepoint(self.rectRanking, mouse):
                    return MenuRedirection.RANKING
                elif Rect.collidepoint(self.rectExit, mouse):
                    return MenuRedirection.QUIT
            if event.type == pygame.QUIT:
                self.to_another_screen = MenuRedirection.QUIT
        return self.to_another_screen

    def init(self):
        self.load_and_play_music()
        self.init_rect()
        self.draw_rect()

    def run_menu(self):
        mouse = pygame.mouse.get_pos()
        self.screen.blit(self.background, (0, 0))

        self.draw_text()
        self.collide_point(mouse)
        self.to_another_screen = self.event_trigger(mouse)
        return self.to_another_screen