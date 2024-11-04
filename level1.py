from level import Level
from levelParser import LevelParser


class Level1(Level):
    def __init__(self, display, gameStateManager, background):
        super().__init__(display, gameStateManager, background)
        self.player.x = 81
        self.player.y = 81
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

    def checkCollisions(self):
        hasCollisions = False
        for wall in self.walls:
            if self.player.rect.colliderect(wall.rect) and \
                wall not in self.player.ignoredWalls and \
                (wall.x // 40 != self.player.ignoreX and
                 wall.y // 40 != self.player.ignoreY):
                hasCollisions = True
                self.player.ignoredWalls.append(wall)
                if self.player.speedX != 0:
                    self.player.ignoreY = wall.y // 40
                elif self.player.speedY != 0:
                    self.player.ignoreX = wall.x // 40
                self.player.speedX = 0
                self.player.speedY = 0
                self.player.moving = False
                # print(self.player.ignoreX, wall.x // 40)
                # print(self.player.ignoreY, wall.y // 40)
                # print('Collision')
        return hasCollisions

    def drawWalls(self):
        for wall in self.walls:
            wall.run()

    def drawEntities(self):
        for entity in self.entities:
            entity.run()

    # doing stuff
    def run(self):
        self.display.blit(self.background, (0, 0))
        self.drawWalls()
        self.drawEntities()
        self.player.run()
        if not self.checkCollisions():
            self.player.ignoredWalls = []
