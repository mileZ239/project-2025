from level import Level
from levelParser import LevelParser


class Level1(Level):
    def __init__(self, display, gameStateManager, background):
        super().__init__(display, gameStateManager, background)
        self.player.x = 101
        self.player.y = 101
        self.walls = LevelParser(display, 'assets/levels/level1.txt').parse()
        print(self.walls)

    def checkCollisions(self):
        for wall in self.walls:
            if self.player.rect.colliderect(wall.rect) and \
                    (self.player.ignoreX != wall.x // 40 and
                     self.player.ignoreY != wall.y // 40):
                self.player.speedX = 0
                self.player.speedY = 0
                self.player.moving = False
                self.player.ignoreX = wall.x // 40
                self.player.ignoreY = wall.y // 40
                print(self.player.ignoreX, wall.x // 40)
                print(self.player.ignoreY, wall.y // 40)
                print('Collision')

    def drawWalls(self):
        for wall in self.walls:
            wall.draw()

    # doing stuff
    def run(self):
        self.display.blit(self.background, (0, 0))
        self.drawWalls()
        self.player.run()
        self.checkCollisions()
