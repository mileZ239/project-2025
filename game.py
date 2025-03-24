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
from bestLevelTime import BestLevelTime
from chooseLevel import ChooseLevel
from globalStuff import globalStuff
from stats import Stats

from level0 import Level0
from level1 import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4
from level5 import Level5
from level6 import Level6
from level7 import Level7


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
        self.bestLevelTime = BestLevelTime(globalStuff.display)
        self.chooseLevel = ChooseLevel(globalStuff.display)
        self.stats = Stats()

        # levels
        self.level0 = Level0(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
        self.level1 = Level1(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
        self.level2 = Level2(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
        self.level3 = Level3(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
        self.level4 = Level4(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
        self.level5 = Level5(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
        self.level6 = Level6(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
        self.level7 = Level7(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)

        # creating a dictionary for our game states
        self.states = {'menu': self.menu,
                       'gameOver': self.gameOver,
                       'settings': self.settings,
                       'pause': self.pause,
                       'records': self.records,
                       'bestLevelTime': self.bestLevelTime,
                       'chooseLevel': self.chooseLevel,
                       'level0': self.level0,
                       'level1': self.level1,
                       'level2': self.level2,
                       'level3': self.level3,
                       'level4': self.level4,
                       'level5': self.level5,
                       'level6': self.level6,
                       'level7': self.level7,
                       }

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
                case 'bestLevelTime':
                    self.states['bestLevelTime'] = BestLevelTime(globalStuff.display)
                    self.gameStateManager.appendState('bestLevelTime')
                case 'chooseLevel':
                    self.states['chooseLevel'] = ChooseLevel(globalStuff.display)
                    self.gameStateManager.appendState('chooseLevel')
                case 'pause':
                    self.gameStateManager.appendState('pause')
                case 'back':
                    self.gameStateManager.prevState()
                case _:  # level
                    sounds.play('stop')
                    self.gameStateManager.appendState(result)
                    time.sleep(0.07)
                    if result != 'level0':
                        self.stats.updatePasses(1)
                    if result == 'level0':
                        self.states[result] = Level0(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level1':
                        self.states[result] = Level1(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level2':
                        self.states[result] = Level2(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level3':
                        self.states[result] = Level3(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level4':
                        self.states[result] = Level4(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level5':
                        self.states[result] = Level5(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level6':
                        self.states[result] = Level6(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)
                    elif result == 'level7':
                        self.states[result] = Level7(globalStuff.display, self.gameStateManager, pygame.image.load('assets/background.png'), self.stats)

                    else:
                        self.gameStateManager.appendState('menu')

            globalStuff.updateTime()

            # updating display
            pygame.display.update()
            self.clock.tick(globalStuff.FPS)
