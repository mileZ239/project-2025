# imports
from level import Level
from levelParser import LevelParser


# testing level class
class Level0(Level):
    def __init__(self, display, gameStateManager, background, stats):
        # basic init
        super().__init__(display, gameStateManager, background, stats)

        # player starting position
        self.player.x = 60
        self.player.y = 30

        # walls and entities
        self.elements = LevelParser(display, 'assets/levels/0.txt').parse()
        self.name = 'level0'

        self.parseElements()

    # doing stuff
    def run(self):
        result = self.runEverything()
        if result is not None:
            return result
