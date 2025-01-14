import sys
import time

import pygame
from gameStateManager import GameStateManager
from menu import Menu
from gameOver import GameOver
from sounds import sounds
from settings import Settings
from pause import Pause
from records import Records
from globalStuff import globalStuff
from stats import Stats
from level0 import Level0
from level1 import Level1


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
        self.gameOver = GameOver(globalStuff.display, self.gameStateManager)
        self.settings = Settings(globalStuff.display)
        self.pause = Pause(globalStuff.display, self.gameStateManager)
        self.records = Records(globalStuff.display)
        self.stats = Stats()

        # levels
        self.level0 = Level0(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'),
                             self.stats)
        self.level1 = Level1(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'),
                             self.stats)

        # creating a dictionary for our game states
        self.states = {'menu': self.menu,
                       'gameOver': self.gameOver,
                       'settings': self.settings,
                       'pause': self.pause,
                       'records': self.records,
                       'level0': self.level0,
                       'level1': self.level1}

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
            match result:
                case None:
                    pass
                case 'menu':
                    sounds.play('stop')
                    self.gameStateManager.set_state('menu')
                case 'settings':
                    sounds.play('stop')
                    self.gameStateManager.appendState('settings')
                case 'records':
                    self.states['records'] = Records(globalStuff.display)
                    self.gameStateManager.appendState('records')
                case 'pause':
                    self.gameStateManager.appendState('pause')
                case 'back':
                    self.gameStateManager.prevState()
                case _:             # level
                    sounds.play('stop')
                    self.gameStateManager.appendState(result)
                    time.sleep(0.07)
                    if result != 'level0':
                        self.stats.updatePasses(1)
                    if result == 'level0':
                        self.states[result] = Level0(globalStuff.display, self.gameStateManager,
                                                     pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level1':
                        self.states[result] = Level1(globalStuff.display, self.gameStateManager,
                                                     pygame.image.load('assets/background.png'), self.stats)
                    else:
                        self.gameStateManager.appendState('menu')

            globalStuff.updateTime()

            # updating display
            pygame.display.update()
            self.clock.tick(globalStuff.FPS)
