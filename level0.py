# imports
from level import Level
from levelParser import LevelParser
from sounds import sounds


# first level class
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
        self.entities = []
        for element in self.elements:
            if element.name == 'wall':
                self.walls.append(element)
            elif element.name == 'bat' or element.name == 'cannon':
                self.entities.append(element)
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

    def checkCollisionsEntities(self):
        for entity in self.entities:
            if self.player.rect.colliderect(entity.rect):
                sounds.play('gameOver')
                self.gameStateManager.set_state('gameOver')

    def drawWalls(self):
        for wall in self.walls:
            wall.run()

    def drawEntities(self):
        for entity in self.entities:
            entity.run()

    # doing stuff
    def run(self):
        self.display.blit(self.background, (0, 0))
        self.checkCollisionsWalls()
        self.drawWalls()
        self.drawEntities()
        self.checkCollisionsEntities()
        self.player.run()
