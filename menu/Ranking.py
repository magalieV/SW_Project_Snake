"""Ranking.py: File that handle the display of the ranking screen"""


"""Import statement go there"""
import Menu
from pygame.locals import *
import pygame
import sys
__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Ranking:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.running = True
        self.to_another_screen = 0

        self.size = width, height = 1920, 1080

        self.screen = pygame.display.set_mode(self.size)

        self.background = pygame.image.load("assets/background.jpg")
        self.font_btn = pygame.font.Font("assets/Granjon.otf", 120)
        self.color_btn_text = (81, 73, 41)
        self.color_btn_bg = (8, 29, 30)
        self.color_btn_text_trigger = (113, 12, 26)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.ranks = []
        self.ranks_text = []

        with open('ranking.txt') as f:
            self.ranks = f.readlines()

        for rank in self.ranks:
            self.ranks_text.append(self.font_btn.render(
                rank, True, self.color_btn_text))

        self.text_exit = self.font_btn.render(
            'EXIT', True, self.color_btn_text)

    def load_and_play_music(self):
        pygame.mixer.music.load("assets/ranking_music.mp3")
        pygame.mixer.music.play(-1)

    def init_rect(self):
        self.ranks_rect = []
        height_rank = 120
        for rank in self.ranks:
            self.ranks_rect.append(
                Rect(self.width/3 - 50, height_rank, 300, 150))
            height_rank += 200
        self.rectExit = Rect(self.width/3 + 125, 860, 300, 150)

    def draw_rect(self):
        for rank_rect in self.ranks_rect:
            pygame.draw.rect(self.screen, self.color_btn_bg, rank_rect, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectExit, 1)

    def draw_text(self):
        height_rank = 100
        for rankText in self.ranks_text:
            self.screen.blit(rankText, (self.width/3 - 50, height_rank))
            height_rank += 150
        self.screen.blit(self.text_exit, (self.width/3 + 125, 860))

    def collide_point(self, mouse):
        if Rect.collidepoint(self.rectExit, mouse):
            self.text_exit = self.font_btn.render(
                'EXIT', True, self.color_btn_text_trigger)
        else:
            self.text_exit = self.font_btn.render(
                'EXIT', True, self.color_btn_text)

    def event_trigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Rect.collidepoint(self.rectExit, mouse):
                    self.to_another_screen = 1
            if event.type == pygame.QUIT:
                sys.exit()

    def init(self):
        self.load_and_play_music()
        self.init_rect()
        self.draw_rect()

    def display_ranking(self):
        while self.running:
            mouse = pygame.mouse.get_pos()
            self.screen.blit(self.background, (0, 0))

            self.draw_text()
            self.collide_point(mouse)
            self.event_trigger(mouse)
            if self.to_another_screen != 0:
                return self.to_another_screen
            pygame.display.update()


def start_ranking():
    ranking = Ranking()
    ranking.init()
    ranking.display_ranking()
    if ranking.to_another_screen == 1:
        Menu.start_menu()


if __name__ == '__main__':
    start_ranking()
