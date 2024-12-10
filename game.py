import sys
import pygame
from gameStateManager import GameStateManager
from level0 import Level0
from menu import Menu
from gameOver import GameOver
from sounds import sounds
from settings import Settings
from pause import Pause
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
        self.pause = Pause(globalStuff.display, self.gameStateManager)

        # creating a dictionary for our game states
        self.states = {'menu': self.menu,
                       'gameOver': self.gameOver,
                       'settings': self.settings,
                       'pause': self.pause,
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
            if result is not None:
                if result == 'menu':
                    sounds.play('stop')
                    self.gameStateManager.set_state('menu')
                elif result == 'level0':
                    sounds.play('stop')
                    self.states['level0'] = Level0(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'))
                    self.gameStateManager.set_state('level0')
                elif result == 'settings':
                    sounds.play('stop')
                    self.gameStateManager.set_state('settings')
                elif 'pause' in result:
                    result = result.replace('pause ', '')
                    self.gameStateManager.set_state('pause')
                    self.states['pause'].level = result

            globalStuff.updateTime()

            # updating display
            pygame.display.update()
            self.clock.tick(globalStuff.FPS)
