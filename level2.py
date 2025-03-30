# imports
from level import Level
from levelParser import LevelParser


class Level2(Level):
    def __init__(self, display, gameStateManager, background, stats):
        # basic init
        super().__init__(display, gameStateManager, background, stats)

        # player starting position
        self.player.x = 30 * 1
        self.player.y = 30 * 25

        # walls and entities
        self.elements = LevelParser(display, 'assets/levels/2.txt').parse()
        self.name = 'level2'

        self.parseElements()

    # doing stuff
    def run(self):
        result = self.runEverything()
        if result is not None:
            return result
