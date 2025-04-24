from level import Level
from levelParser import LevelParser


class Level1(Level):
    def __init__(self, display, gameStateManager, background, stats):
        super().__init__(display, gameStateManager, background, stats)

        # начальная позиция игрока
        self.player.x = 30
        self.player.y = 30

        # объекты
        self.elements = LevelParser(display, 'assets/levels/1.txt').parse()
        self.name = 'level1'

        self.parseElements()

    def run(self):
        result = self.runEverything()
        if result is not None:
            return result
