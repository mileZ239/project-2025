# imports
from level import Level
from levelParser import LevelParser
import pygame


# testing level class
class Level1(Level):
    def __init__(self, display, gameStateManager, background, stats):
        # basic init
        super().__init__(display, gameStateManager, background, stats)

        # player starting position
        self.player.x = 300
        self.player.y = 300

        # walls and entities
        self.elements = LevelParser(display, 'assets/levels/1.txt').parse()
        self.name = 'level1'
        for element in self.elements:
            if element.name == 'wall':
                self.walls.append(element)
            elif element.name == 'bat':
                self.bats.append(element)
            elif element.name == 'thorn':
                self.thorns.append(element)
            elif element.name == 'endPortal' or element.name == 'portal':
                self.portals.append(element)
            elif element.name == 'cannon':
                self.cannons.append(element)
                self.walls.append(element)
            else:
                pass

    # doing stuff
    def run(self):
        self.stats.updateTime(1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return 'pause'
        self.display.blit(self.background, (0, 0))

        self.drawStuff()
        collisionResult = self.checkCollisions()

        self.player.run()

        if collisionResult is not None:
            return collisionResult
