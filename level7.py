# imports
from level import Level
from levelParser import LevelParser


class Level7(Level):
    def __init__(self, display, gameStateManager, background, stats):
        # basic init
        super().__init__(display, gameStateManager, background, stats)

        # player starting position
        self.player.x = 30 * 19
        self.player.y = 30 * 12

        # walls and entities
        self.elements = LevelParser(display, 'assets/levels/7.txt').parse()
        self.name = 'level7'

        self.parseElements()

    # doing stuff
    def run(self):
        result = self.runEverything()
        if result is not None:
            return result
