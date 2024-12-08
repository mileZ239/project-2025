import sys
import pygame
from gameStateManager import GameStateManager
from level0 import Level0
from menu import Menu
from gameOver import GameOver
from sounds import sounds
from settings import Settings
from globalStuff import globalStuff


# main class
class Game:

    def __init__(self):
        # initializing pygame
        pygame.init()

        # creating a clock for managing FPS
        self.clock = pygame.time.Clock()

        # creating an instance of GameStateManager class
        self.gameStateManager = GameStateManager('menu')

        # creating instances of Menu and Level classes
        self.menu = Menu(globalStuff.display)
        self.level0 = Level0(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'))
        self.gameOver = GameOver(globalStuff.display)
        self.settings = Settings(globalStuff.display)

        # creating a dictionary for our game states
        self.states = {'menu': self.menu,
                       'gameOver': self.gameOver,
                       'settings': self.settings,
                       'level0': self.level0}

    # main function
    def run(self):
        pygame.mixer.init()
        # main loop
        while True:
            # looking for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # running stuff at current state
            result = self.states[self.gameStateManager.get_state()].run()
            # print(result)
            if result == 'menu':
                sounds.play('stop')
                self.gameStateManager.set_state('menu')
            elif result == 'level':
                sounds.play('stop')
                self.states['level'] = Level0(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'))
                self.gameStateManager.set_state('level')
            elif result == 'settings':
                sounds.play('stop')
                self.gameStateManager.set_state('settings')

            globalStuff.updateTime()

            # updating display
            pygame.display.update()
            self.clock.tick(globalStuff.FPS)
