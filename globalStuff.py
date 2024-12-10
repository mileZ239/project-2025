import pygame


class GlobalStuff:
    def __init__(self):
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 800
        self.FPS = 60
        self.display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.globalTime = 0

    def updateTime(self):
        self.globalTime += 1


globalStuff = GlobalStuff()