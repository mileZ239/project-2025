# imports
from level import Level
from levelParser import LevelParser
import pygame


# testing level class
class Level0(Level):
    def __init__(self, display, gameStateManager, background):
        # basic init
        super().__init__(display, gameStateManager, background)

        # player starting position
        self.player.x = 60
        self.player.y = 30

        # walls and entities
        self.elements = LevelParser(display, 'assets/levels/0.txt').parse()
        for element in self.elements:
            if element.name == 'wall':
                self.walls.append(element)
            elif element.name == 'bat':
                self.bats.append(element)
            elif element.name == 'thorn':
                self.thorns.append(element)
            elif element.name == 'endPortal' or element.name == 'portal':
                self.portals.append(element)
            else:
                pass

    # doing stuff
    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return 'pause 0'
        self.display.blit(self.background, (0, 0))

        self.drawPortals()
        self.drawWalls()
        self.drawThorns()
        self.drawBats()

        self.checkCollisionsPortals()
        self.checkCollisionsBats()
        self.checkCollisionsWalls()
        self.checkCollisionsThorns()

        self.player.run()
