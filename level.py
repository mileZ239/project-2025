# imports
from player import Player
from sounds import sounds


# level class
class Level:
    def __init__(self, display, gameStateManager, background):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = background
        self.player = Player(display)
        self.paused = False

        self.walls = []
        self.bats = []
        self.thorns = []

    def drawWalls(self):
        for wall in self.walls:
            wall.run()

    def drawBats(self):
        for bat in self.bats:
            bat.run()

    def drawThorns(self):
        for thorn in self.thorns:
            thorn.run()

    def checkCollisionsBats(self):
        for bat in self.bats:
            if self.player.rect.colliderect(bat.rect):
                sounds.play('gameOver')
                self.gameStateManager.set_state('gameOver')

    def checkCollisionsThorns(self):
        for thorn in self.thorns:
            if self.player.rect.colliderect(thorn.rect) and self.player.facing == thorn.facing:
                sounds.play('gameOver')
                self.gameStateManager.set_state('gameOver')

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

    def pause(self):
        self.paused = True
        self.gameStateManager.setState('pause')
