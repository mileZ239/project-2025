# imports
import pygame

from player import Player
from button import Button
from sounds import sounds
from settings import Settings


# level class
class Level:
    def __init__(self, display, gameStateManager, background, stats):
        # init
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = background

        # supporting classes
        self.stats = stats
        self.player = Player(display)
        self.settings = Settings(display)

        # difficulty correction
        self.leftTime = 60 * 30 // self.settings.difficulty

        self.paused = False
        self.timerLabel = Button(display, 1140, 760, 'assets/backgroundEmpty.png', str(self.leftTime), 52, pygame.Color(0, 154, 255))
        self.name = 'level'

        self.walls = []
        self.bats = []
        self.thorns = []
        self.thornsTrap = []
        self.portals = []
        self.cannons = []
        self.pufferfish = []
        self.stars = []
        self.elements = []

    def parseElements(self):
        for element in self.elements:
            if element.name == 'wall':
                self.walls.append(element)
            elif element.name == 'bat':
                self.bats.append(element)
            elif element.name == 'thorn':
                self.thorns.append(element)
            elif element.name == 'thornTrap':
                self.thornsTrap.append(element)
            elif element.name == 'endPortal' or element.name == 'portal':
                self.portals.append(element)
            elif element.name == 'cannon':
                element.multiplier = self.settings.difficulty
                self.cannons.append(element)
                self.walls.append(element)
            elif element.name == 'pufferfish':
                element.multiplier = self.settings.difficulty
                self.pufferfish.append(element)
            elif element.name == 'star':
                element.multiplier = self.settings.difficulty
                self.stars.append(element)
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

    def drawThornsTrap(self):
        for thornTrap in self.thornsTrap:
            thornTrap.run()

    def drawCannons(self):
        for cannon in self.cannons:
            cannon.run()

    def drawPufferfish(self):
        for pufferfish in self.pufferfish:
            pufferfish.run()

    def drawStars(self):
        for star in self.stars:
            star.run()

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

    def checkCollisionsThornsTrap(self):
        for thornTrap in self.thornsTrap:
            if self.player.rect.colliderect(thornTrap.rect):
                if thornTrap.activated:
                    self.gameOver()
                elif thornTrap.cooldown == 0:
                    thornTrap.cooldown = 45

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

    def checkCollisionsPufferfish(self):
        for pufferfish in self.pufferfish:
            if not pufferfish.deflated and self.player.rect.colliderect(pufferfish.rect):
                self.gameOver()

    def checkCollisionsStars(self):
        delStars = []
        for i in range(len(self.stars)):
            star = self.stars[i]
            if self.player.rect.colliderect(star.rect):
                self.leftTime += star.addTime
                delStars.append(i)
                star.delete()
        for i in delStars:
            del self.stars[i]

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
        self.drawThornsTrap()
        self.drawBats()
        self.drawCannons()
        self.drawPufferfish()
        self.drawStars()
        self.drawTimer()

    def checkCollisions(self):
        endPortalCollision = self.checkCollisionsPortals()
        if endPortalCollision is not None:
            return endPortalCollision
        self.checkCollisionsBats()
        self.checkCollisionsWalls()
        self.checkCollisionsThorns()
        self.checkCollisionsThornsTrap()
        self.checkCollisionsProjectiles()
        self.checkCollisionsPufferfish()
        self.checkCollisionsStars()

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
