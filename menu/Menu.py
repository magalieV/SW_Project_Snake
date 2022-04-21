"""Menu.py: File that handle the display of the menu"""


"""Import statement go there"""
from pygame.locals import *
import pygame
import sys
__author__ = "Pierre Ghyzel"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Menu:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.running = True

        self.size = width, height = 1920, 1080

        self.screen = pygame.display.set_mode(self.size)

        self.background = pygame.image.load("assets/background.jpg")
        self.fontBtn = pygame.font.Font("assets/Granjon.otf", 120)
        self.colorBtnText = (81, 73, 41)
        self.colorBtnBg = (8, 29, 30)
        self.colorBtnTextTrigger = (113, 12, 26)

        self.textPlay = self.fontBtn.render('PLAY', True, self.colorBtnText)
        self.textLoad = self.fontBtn.render('LOAD', True, self.colorBtnText)
        self.textRanking = self.fontBtn.render(
            'RANKING', True, self.colorBtnText)
        self.textExit = self.fontBtn.render('EXIT', True, self.colorBtnText)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def loadAndPlayMusic(self):
        pygame.mixer.music.load("assets/bg_music.mp3")
        pygame.mixer.music.play(-1)

    def initRect(self):
        self.rectPlay = Rect(self.width/3 + 125, 120, 300, 150)
        self.rectLoad = Rect(self.width/3 + 125, 320, 300, 150)
        self.rectRanking = Rect(self.width/3, 520, 600, 150)
        self.rectExit = Rect(self.width/3 + 125, 720, 300, 150)

    def drawRect(self):
        pygame.draw.rect(self.screen, self.colorBtnBg, self.rectPlay, 1)
        pygame.draw.rect(self.screen, self.colorBtnBg, self.rectLoad, 1)
        pygame.draw.rect(self.screen, self.colorBtnBg, self.rectRanking, 1)
        pygame.draw.rect(self.screen, self.colorBtnBg, self.rectExit, 1)

    def drawText(self):
        self.screen.blit(self.textPlay, (self.width/3 + 125, 120))
        self.screen.blit(self.textLoad, (self.width/3 + 125, 320))
        self.screen.blit(self.textRanking, (self.width/3, 520))
        self.screen.blit(self.textExit, (self.width/3 + 125, 720))

    def collidePoint(self, mouse):
        if Rect.collidepoint(self.rectPlay, mouse):
            self.textPlay = self.fontBtn.render(
                'PLAY', True, self.colorBtnTextTrigger)
        elif Rect.collidepoint(self.rectLoad, mouse):
            self.textLoad = self.fontBtn.render(
                'LOAD', True, self.colorBtnTextTrigger)
        elif Rect.collidepoint(self.rectRanking, mouse):
            self.textRanking = self.fontBtn.render(
                'RANKING', True, self.colorBtnTextTrigger)
        elif Rect.collidepoint(self.rectExit, mouse):
            self.textExit = self.fontBtn.render(
                'EXIT', True, self.colorBtnTextTrigger)
        else:
            self.textPlay = self.fontBtn.render(
                'PLAY', True, self.colorBtnText)
            self.textLoad = self.fontBtn.render(
                'LOAD', True, self.colorBtnText)
            self.textRanking = self.fontBtn.render(
                'RANKING', True, self.colorBtnText)
            self.textExit = self.fontBtn.render(
                'EXIT', True, self.colorBtnText)

    def eventTrigger(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                """provisional line, change it when you want to start the game developpement"""
                if Rect.collidepoint(self.rectExit, mouse) or Rect.collidepoint(self.rectLoad, mouse) or Rect.collidepoint(self.rectRanking, mouse) or Rect.collidepoint(self.rectPlay, mouse):
                    self.running = False
            if event.type == pygame.QUIT:
                sys.exit()

    def init(self):
        self.loadAndPlayMusic()
        self.initRect()
        self.drawRect()

    def displayMenu(self):
        while self.running:
            mouse = pygame.mouse.get_pos()
            self.screen.blit(self.background, (0, 0))

            self.drawText()
            self.collidePoint(mouse)
            self.eventTrigger(mouse)
            pygame.display.update()


def startMenu():
    menu = Menu()
    menu.init()
    menu.displayMenu()


if __name__ == '__main__':
    startMenu()
