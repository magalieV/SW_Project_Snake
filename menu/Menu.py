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

pygame.init()


class init:
    running = True

    size = width, height = 1920, 1080

    screen = pygame.display.set_mode(size)

    background = pygame.image.load("assets/background.jpg")
    fontBtn = pygame.font.Font("assets/Granjon.otf", 120)
    colorBtnText = (81, 73, 41)
    colorBtnBg = (8, 29, 30)
    colorBtnTextTrigger = (113, 12, 26)

    textPlay = fontBtn.render('PLAY', True, colorBtnText)
    textLoad = fontBtn.render('LOAD', True, colorBtnText)
    textRanking = fontBtn.render('RANKING', True, colorBtnText)
    textExit = fontBtn.render('EXIT', True, colorBtnText)

    width = screen.get_width()
    height = screen.get_height()


def loadAndPlayMusic():
    pygame.mixer.music.load("assets/bg_music.mp3")
    pygame.mixer.music.play(-1)


def drawRect():
    pygame.draw.rect(init.screen, init.colorBtnBg, init.rectPlay, 1)
    pygame.draw.rect(init.screen, init.colorBtnBg, init.rectLoad, 1)
    pygame.draw.rect(init.screen, init.colorBtnBg, init.rectRanking, 1)
    pygame.draw.rect(init.screen, init.colorBtnBg, init.rectExit, 1)


def drawText():
    init.screen.blit(init.textPlay, (init.width/3 + 125, 120))
    init.screen.blit(init.textLoad, (init.width/3 + 125, 320))
    init.screen.blit(init.textRanking, (init.width/3, 520))
    init.screen.blit(init.textExit, (init.width/3 + 125, 720))


def initRect():
    init.rectPlay = Rect(init.width/3 + 125, 120, 300, 150)
    init.rectLoad = Rect(init.width/3 + 125, 320, 300, 150)
    init.rectRanking = Rect(init.width/3, 520, 600, 150)
    init.rectExit = Rect(init.width/3 + 125, 720, 300, 150)


def collidePoint(mouse):
    if Rect.collidepoint(init.rectPlay, mouse):
        init.textPlay = init.fontBtn.render(
            'PLAY', True, init.colorBtnTextTrigger)
    elif Rect.collidepoint(init.rectLoad, mouse):
        init.textLoad = init.fontBtn.render(
            'LOAD', True, init.colorBtnTextTrigger)
    elif Rect.collidepoint(init.rectRanking, mouse):
        init.textRanking = init.fontBtn.render(
            'RANKING', True, init.colorBtnTextTrigger)
    elif Rect.collidepoint(init.rectExit, mouse):
        init.textExit = init.fontBtn.render(
            'EXIT', True, init.colorBtnTextTrigger)
    else:
        init.textPlay = init.fontBtn.render('PLAY', True, init.colorBtnText)
        init.textLoad = init.fontBtn.render('LOAD', True, init.colorBtnText)
        init.textRanking = init.fontBtn.render(
            'RANKING', True, init.colorBtnText)
        init.textExit = init.fontBtn.render('EXIT', True, init.colorBtnText)


def eventTrigger(mouse):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            """provisional line, change it when you want to start the game developpement"""
            if Rect.collidepoint(init.rectExit, mouse) or Rect.collidepoint(init.rectLoad, mouse) or Rect.collidepoint(init.rectRanking, mouse) or Rect.collidepoint(init.rectPlay, mouse):
                init.running = False
        if event.type == pygame.QUIT:
            sys.exit()


def displayMenu():
    while init.running:
        mouse = pygame.mouse.get_pos()
        init.screen.blit(init.background, (0, 0))

        initRect()
        drawRect()
        drawText()
        collidePoint(mouse)
        eventTrigger(mouse)
        pygame.display.update()


def start():
    pygame.mixer.init()
    loadAndPlayMusic()
    displayMenu()


if __name__ == '__main__':
    start()
