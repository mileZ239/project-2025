# imports
from level import Level
from levelParser import LevelParser
from sounds import sounds
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
        self.walls = []
        self.bats = []
        self.thorns = []
        for element in self.elements:
            if element.name == 'wall':
                self.walls.append(element)
            elif element.name == 'bat':
                self.bats.append(element)
            elif element.name == 'thorn':
                self.thorns.append(element)
            else:
                pass

    def checkCollisionsWalls(self):
        hasCollisions = False
        for wall in self.walls:
            if self.player.rect.colliderect(wall.rect) and not \
                    (self.player.ignoreX - 30 == wall.x or wall.x == self.player.ignoreX + 30 or
                     self.player.ignoreY - 30 == wall.y or wall.y == self.player.ignoreY + 30):

                hasCollisions = True
                self.player.speedX = 0
                self.player.speedY = 0
                self.player.moving = False
        return hasCollisions

    def checkCollisionsBats(self):
        for bat in self.bats:
            if self.player.rect.colliderect(bat.rect):
                sounds.play('gameOver')
                self.gameStateManager.set_state('gameOver')

    def checkCollisionsTrorns(self):
        for thorn in self.thorns:
            if self.player.rect.colliderect(thorn.rect):
                pass

    def drawWalls(self):
        for wall in self.walls:
            wall.run()

    def drawBats(self):
        for bat in self.bats:
            bat.run()

    def drawThorns(self):
        for thorn in self.thorns:
            thorn.run()

    # doing stuff
    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return 'pause 0'
        self.display.blit(self.background, (0, 0))

        self.drawWalls()
        self.drawBats()
        self.drawThorns()

        self.checkCollisionsBats()
        self.checkCollisionsWalls()
        self.checkCollisionsTrorns()

        self.player.run()
