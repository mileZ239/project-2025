# imports
from player import Player
from sounds import sounds


# level class
class Level:
    def __init__(self, display, gameStateManager, background, stats):
        self.display = display
        self.gameStateManager = gameStateManager
        self.stats = stats
        self.background = background
        self.player = Player(display)
        self.paused = False
        self.name = 'level'

        self.walls = []
        self.bats = []
        self.thorns = []
        self.portals = []
        self.cannons = []

    def drawPortals(self):
        for portal in self.portals:
            portal.run()

    def drawWalls(self):
        for wall in self.walls:
            wall.run()

    def drawBats(self):
        for bat in self.bats:
            bat.run()

    def drawThorns(self):
        for thorn in self.thorns:
            thorn.run()

    def drawCannons(self):
        for cannon in self.cannons:
            cannon.run()

    def checkCollisionsPortals(self):
        for portal in self.portals:
            if self.player.rect.colliderect(portal.rect):
                if portal.name == 'endPortal':
                    nextLevel = 'level' + str(int(self.name[-1]) + 1)
                    return nextLevel
                    # self.gameStateManager.set_state('menu')

    def checkCollisionsBats(self):
        for bat in self.bats:
            if self.player.rect.colliderect(bat.rect):
                self.stats.updateDeaths(1)
                sounds.play('gameOver')
                self.gameStateManager.set_state('gameOver')

    def checkCollisionsThorns(self):
        for thorn in self.thorns:
            if self.player.rect.colliderect(thorn.rect) and self.player.facing == thorn.facing:
                sounds.play('gameOver')
                self.gameStateManager.set_state('gameOver')

    def checkCollisionsWalls(self):
        for wall in self.walls:
            ignoreX, ignoreY = self.player.ignoreX, self.player.ignoreY
            playerX, playerY = self.player.x, self.player.y
            facing = self.player.facing
            if ((facing == 'North' and playerY - 30 == wall.y and playerX == wall.x) or
                    (facing == 'South' and playerY + 30 == wall.y and playerX == wall.x) or
                    (facing == 'East' and playerX + 30 == wall.x and playerY == wall.y) or
                    (facing == 'West' and playerX - 30 == wall.x and playerY == wall.y)):
                self.player.speedX = 0
                self.player.speedY = 0
                self.player.moving = False
                continue
            if self.player.rect.colliderect(wall.rect) and not \
                    (ignoreX - 30 == wall.x or wall.x == ignoreX + 30 or
                     ignoreY - 30 == wall.y or wall.y == ignoreY + 30):
                self.player.speedX = 0
                self.player.speedY = 0
                self.player.moving = False

    def checkCollisionsProjectiles(self):
        for cannons in self.cannons:
            for projectile in cannons.projectiles:
                if self.player.rect.colliderect(projectile.rect):
                    self.stats.updateDeaths(1)
                    sounds.play('gameOver')
                    self.gameStateManager.set_state('gameOver')

    def pause(self):
        self.paused = True
        self.gameStateManager.setState('pause')

    def drawStuff(self):
        self.drawPortals()
        self.drawWalls()
        self.drawThorns()
        self.drawBats()
        self.drawCannons()

    def checkCollisions(self):
        endPortalCollision = self.checkCollisionsPortals()
        if endPortalCollision is not None:
            return endPortalCollision
        self.checkCollisionsBats()
        self.checkCollisionsWalls()
        self.checkCollisionsThorns()
        self.checkCollisionsProjectiles()
