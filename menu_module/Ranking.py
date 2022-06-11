"""Ranking.py: File that handle the display of the ranking screen"""

import sys
from menu_module.MenuRedirection import MenuRedirection
from pygame.locals import *
import pygame
import os

__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"

FONT_SIZE = 60

class Ranking:
    def __init__(self, window_size, window):

        self._window_size = window_size
        self._back_size = (0.60 * window_size[0], 0.80 * window_size[1])

        self.screen = window

        self.background = pygame.image.load("menu_module/assets/background.jpg")
        self.font_btn = pygame.font.Font("menu_module/assets/Granjon.otf", FONT_SIZE)
        self.color_btn_text = (161, 144, 75)
        self.color_btn_bg = (8, 29, 30)
        self.color_btn_text_trigger = (113, 12, 26)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.ranks = []
        self.ranks_text = []

        self._rank_back = pygame.Surface((self._back_size[0], self._back_size[1]), pygame.SRCALPHA)
        self._rank_back.fill((0, 0, 0, 170))

        self._file_path = f'menu_module/ranking.txt'

        self.load_ranking()

        self.text_exit = self.font_btn.render(
            'EXIT', True, self.color_btn_text)

    def load_ranking(self):
        self.ranks = {}
        self._player_name = []
        self._player_score = []
        if os.path.exists(self._file_path):
            with open(self._file_path) as file_input:
                lines = file_input.readlines()
                for line in lines:
                    line = line.strip()
                    ranks_save = line.split(',')
                    self.ranks[ranks_save[0]] = int(ranks_save[1])
                    self._player_name.append(self.font_btn.render(ranks_save[0], False, (255, 255, 255)))
                    self._player_score.append(self.font_btn.render(ranks_save[1], False, (255, 40, 40)))

    def init_rect(self):
        self.ranks_rect = []
        self.rectExit = Rect((self._window_size[0]/2 - (self.text_exit.get_width() / 2)), 0.80 * self._window_size[1], 150, 75)

    def draw_rect(self):
        for rank_rect in self.ranks_rect:
            pygame.draw.rect(self.screen, self.color_btn_bg, rank_rect, 1)
        pygame.draw.rect(self.screen, self.color_btn_bg, self.rectExit, 1)

    def draw_text(self):
        height_rank = 0.10 * self._window_size[1] + 10
        self.screen.blit(self._rank_back, (self._window_size[0]/2 - self._back_size[0]/2, 0.10 * self._window_size[1]))
        for name in self._player_name:
            self.screen.blit(name, (self.width/4, height_rank))
            height_rank += 75
        height_rank = 0.10 * self._window_size[1] + 10
        for name in self._player_score:
            self.screen.blit(name, (self.width / 4 * 3 - name.get_width(), height_rank))
            height_rank += 75
        self.screen.blit(self.text_exit, ((self._window_size[0]/2 - (self.text_exit.get_width() / 2)), 0.80 * self._window_size[1]))

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
                    return MenuRedirection.MENU
            if event.type == pygame.QUIT:
                return MenuRedirection.QUIT
        return MenuRedirection.RANKING

    def init(self):
        self.init_rect()
        self.draw_rect()

    def run_ranking(self):
        mouse = pygame.mouse.get_pos()
        self.screen.blit(self.background, (0, 0))

        self.draw_text()
        self.collide_point(mouse)
        return self.event_trigger(mouse)

    def save_ranking(self, score):
        index = 0
        if len(sys.argv) < 2:
            name = "Player"
            while name in self.ranks:
                index += 1
                name = "Player" + str(index)
        else:
            name = sys.argv[1]
        if name in self.ranks and score > self.ranks[name]:
            self.ranks[name] = score
        elif name not in self.ranks:
            self.ranks[name] = score
        sorted_list = sorted(self.ranks.items(), key=lambda x: x[1], reverse=True)
        counter = 0
        with open(self._file_path, "w") as file_output:
            for element in sorted_list:
                file_output.write(element[0] + "," + str(element[1]) + "\n")
                counter += 1
                if counter == 7:
                    break


