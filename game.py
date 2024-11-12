import sys
import pygame
from gameStateManager import GameStateManager
from level1 import Level1
from menu import Menu
from gameOver import GameOver
from globalTime import GlobalTime

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60


# main class
class Game:
    def __init__(self):
        # initializing pygame
        pygame.init()

        # creating main display (surface)
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # creating a clock for managing FPS
        self.clock = pygame.time.Clock()

        # creating an instance of GameStateManager class
        self.gameStateManager = GameStateManager('menu')

        # creating instances of Menu and Level classes
        self.menu = Menu(self.display, self.gameStateManager)
        self.level1 = Level1(self.display, self.gameStateManager, pygame.image.load('assets/background.png'))
        self.gameOver = GameOver(self.display, self.gameStateManager)

        self.globalTime = GlobalTime()

        # creating a dictionary for our game states
        self.states = {'menu': self.menu, 'level': self.level1, 'gameOver': self.gameOver}

    # main function
    def run(self):
        # main loop
        while True:
            # looking for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # running stuff at current state
            self.states[self.gameStateManager.get_state()].run()

            self.globalTime.update()

            # updating display
            pygame.display.update()
            self.clock.tick(FPS)
