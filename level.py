# imports
from player import Player
from button import Button
from sounds import sounds
import pygame


# level class
class Level:
    def __init__(self, display, gameStateManager, background, stats):
        self.display = display
        self.gameStateManager = gameStateManager
        self.stats = stats
        self.background = background
        self.player = Player(display)
        self.paused = False
        self.leftTime = 60 * 15
        self.timerLabel = Button(display, 1140, 760, 'assets/backgroundEmpty.png', str(self.leftTime), 52, pygame.Color(0, 154, 255))
        self.name = 'level'

        self.walls = []
        self.bats = []
        self.thorns = []
        self.portals = []
        self.cannons = []
        self.elements = []

    def parseElements(self):
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

    def drawTimer(self):
        self.timerLabel.text = str(self.leftTime // 60 + 1)
        self.timerLabel.draw()

    def checkCollisionsPortals(self):
        for portal in self.portals:
            if self.player.rect.colliderect(portal.rect):
                if portal.name == 'endPortal':
                    nextLevel = 'level' + str(int(self.name[-1]) + 1)
                    return nextLevel

    def checkCollisionsBats(self):
        for bat in self.bats:
            if self.player.rect.colliderect(bat.rect):
                self.gameOver()

    def checkCollisionsThorns(self):
        for thorn in self.thorns:
            if self.player.rect.colliderect(thorn.rect):
                self.gameOver()

    def checkCollisionsWalls(self):
        playerX, playerY = self.player.x, self.player.y
        facing = self.player.facing
        for wall in self.walls:
            if ((facing == 'North' and playerY - 30 == wall.y and playerX == wall.x) or
                    (facing == 'South' and playerY + 30 == wall.y and playerX == wall.x) or
                    (facing == 'East' and playerX + 30 == wall.x and playerY == wall.y) or
                    (facing == 'West' and playerX - 30 == wall.x and playerY == wall.y)):
                self.player.speedX = 0
                self.player.speedY = 0
                self.player.moving = False
                continue

    def checkCollisionsProjectiles(self):
        for cannons in self.cannons:
            for projectile in cannons.projectiles:
                if self.player.rect.colliderect(projectile.rect):
                    self.gameOver()

    def pause(self):
        self.paused = True
        self.gameStateManager.appendState('pause')

    def gameOver(self):
        self.stats.updateDeaths(1)
        sounds.play('gameOver')
        self.gameStateManager.appendState('gameOver')

    def drawStuff(self):
        self.drawPortals()
        self.drawWalls()
        self.drawThorns()
        self.drawBats()
        self.drawCannons()
        self.drawTimer()

    def checkCollisions(self):
        endPortalCollision = self.checkCollisionsPortals()
        if endPortalCollision is not None:
            return endPortalCollision
        self.checkCollisionsBats()
        self.checkCollisionsWalls()
        self.checkCollisionsThorns()
        self.checkCollisionsProjectiles()

    def runEverything(self):
        self.stats.updateTime(1)

        self.leftTime -= 1
        if self.leftTime <= 0:
            self.gameOver()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return 'pause'
        self.display.blit(self.background, (0, 0))

        self.drawStuff()
        collisionResult = self.checkCollisions()

        self.player.run()

        if collisionResult is not None:
            return collisionResult
