import pygame
import sys
from menu import Menu
from gameStateManager import GameStateManager
from level1 import Level1

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 120


# main class
class Game:
    def __init__(self):
        # initializing pygame
        pygame.init()

        # creating main display (surface)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # creating a clock for managing FPS
        self.clock = pygame.time.Clock()

        # creating an instance of GameStateManager class
        self.gameStateManager = GameStateManager('menu')

        # creating instances of Menu and Level classes
        self.menu = Menu(self.screen, self.gameStateManager)
        self.level1 = Level1(self.screen, self.gameStateManager, pygame.image.load('assets/background.png'))

        # creating a dictionary for our game states
        self.states = {'menu': self.menu, 'level': self.level1}

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

            # updating display
            pygame.display.update()
            self.clock.tick(FPS)
