from level import Level
from levelParser import LevelParser


class Level1(Level):
    def __init__(self, display, gameStateManager, background):
        super().__init__(display, gameStateManager, background)
        self.player.x = 60
        self.player.y = 30
        self.elements = LevelParser(display, 'assets/levels/level1.txt').parse()
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
            if self.player.rect.colliderect(wall.rect) and \
                wall not in self.player.ignoredWalls and \
                (wall.x // 30 != self.player.ignoreX and
                 wall.y // 30 != self.player.ignoreY):
                hasCollisions = True
                self.player.ignoredWalls.append(wall)
                if self.player.speedX != 0:
                    self.player.ignoreY = wall.y // 30
                elif self.player.speedY != 0:
                    self.player.ignoreX = wall.x // 30
                self.player.speedX = 0
                self.player.speedY = 0
                self.player.moving = False
        return hasCollisions

    def checkCollisionsEntities(self):
        for entity in self.entities:
            if self.player.rect.colliderect(entity.rect):
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
        if not self.checkCollisionsWalls():
            self.player.ignoredWalls = []
        self.drawWalls()
        self.drawEntities()
        self.checkCollisionsEntities()
        self.player.run()
