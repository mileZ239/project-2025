# imports
import pygame

from player import Player
from button import Button
from sounds import sounds
from settings import Settings
from globalStuff import globalStuff


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
        match self.settings.difficulty:
            case 0:
                self.difficulty = 0.001
                self.difficultyName = 'explorer'
            case 1:
                self.difficulty = 1
                self.difficultyName = 'easy'
            case 2:
                self.difficulty = 2
                self.difficultyName = 'hard'
        self.leftTime = 60 * 90 // self.difficulty

        self.lastedTime = 0
        self.collectedStars = 0

        self.paused = False
        self.timerLabel = Button(display, 1140, 760, 'assets/backgroundEmpty.png', str(self.leftTime), 52, pygame.Color(0, 154, 255))
        self.invincibilityLabel = Button(display, 1100, 20, 'assets/backgroundEmpty.png', 'Неуязвимость', 35, pygame.Color(220, 220, 220))
        self.slowLabel = Button(display, 1100, 50, 'assets/backgroundEmpty.png', 'Замедление', 35, pygame.Color(52, 204, 255))
        self.name = 'level'

        # slowing time ability
        self.slow = False
        self.slowCount = 2
        self.slowTime = 60 / 2 * 2
        self.slowLeft = 0

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
            if element.name == 'wall' or element.name == 'semiWall':
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
                element.multiplier = self.difficulty
                element.cooldown /= element.multiplier
                self.cannons.append(element)
                self.walls.append(element)
            elif element.name == 'pufferfish':
                element.multiplier = self.difficulty
                element.cooldown /= element.multiplier
                self.pufferfish.append(element)
            elif element.name == 'star':
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
        self.timerLabel.text = str(round(self.leftTime / 60, 1))
        self.timerLabel.draw()

    def drawEffects(self):
        if self.player.invincible:
            self.invincibilityLabel.draw()
        if self.slow:
            self.slowLabel.draw()

    def checkCollisionsPortals(self):
        for portal in self.portals:
            if self.player.rect.colliderect(portal.rect):
                if portal.name == 'endPortal':
                    nextLevel = 'level' + str(int(self.name[-1]) + 1)
                    return nextLevel

    def checkCollisionsBats(self):
        if self.player.invincible:
            return
        for bat in self.bats:
            if self.player.rect.colliderect(bat.rect):
                self.gameOver()

    def checkCollisionsThorns(self):
        for thorn in self.thorns:
            if self.player.rect.colliderect(thorn.rect):
                self.gameOver()

    def checkCollisionsThornsTrap(self):
        if self.player.invincible:
            return
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
        for cannon in self.cannons:
            removed = []
            for projectile in cannon.projectiles:
                if not self.player.invincible and self.player.rect.colliderect(projectile.rect):
                    self.gameOver()
                for wall in self.walls:
                    if wall.name == 'wall' and wall.rect.colliderect(projectile.rect):
                        removed.append(projectile)
                        break
            for projectile in removed:
                cannon.projectiles.remove(projectile)

    def checkCollisionsPufferfish(self):
        if self.player.invincible:
            return
        for pufferfish in self.pufferfish:
            if not pufferfish.deflated and self.player.rect.colliderect(pufferfish.rect):
                self.gameOver()

    def checkCollisionsStars(self):
        delStars = []
        for i in range(len(self.stars)):
            star = self.stars[i]
            if self.player.rect.colliderect(star.rect):
                self.leftTime += star.addTime
                self.collectedStars += 1
                delStars.append(i)
                star.delete()
        for i in delStars:
            del self.stars[i]

    def pause(self):
        self.paused = True
        self.gameStateManager.appendState('pause')

    def gameOver(self):
        globalStuff.FPS = 60
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
        self.drawEffects()

    def checkCollisions(self):
        endPortalCollision = self.checkCollisionsPortals()
        if endPortalCollision is not None:
            return endPortalCollision
        self.checkCollisionsWalls()
        self.checkCollisionsThorns()
        self.checkCollisionsStars()
        self.checkCollisionsProjectiles()
        self.checkCollisionsBats()
        self.checkCollisionsThornsTrap()
        self.checkCollisionsPufferfish()
        if self.player.invincible:
            self.player.invincibilityLeft -= 1
            if self.player.invincibilityLeft == 0:
                self.player.invincible = False
                # print("Not invincible")

    def runEverything(self):
        self.stats.updateTime(1)

        self.leftTime -= 1
        if self.leftTime <= 0:
            self.gameOver()

        self.lastedTime += 1

        if self.slow:
            self.slowLeft -= 1
        if self.slow and self.slowLeft == 0:
            globalStuff.FPS *= 2
            self.player.speed /= 2
            self.slow = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return 'pause'
        if keys[pygame.K_c] and not self.slow and self.slowCount:
            globalStuff.FPS /= 2
            self.player.speed *= 2
            self.slow = True
            self.slowLeft = self.slowTime
            self.slowCount -= 1

        self.display.blit(self.background, (0, 0))

        self.drawStuff()
        collisionResult = self.checkCollisions()

        self.player.run()

        if collisionResult is not None:
            globalStuff.FPS = 60
            with open('assets/stats/levels/' + self.difficultyName + '/' + self.name[-1] + '.txt', 'r') as levelStats:
                data = levelStats.readlines()
                currentMinTime = int(data[0])
                currentMaxStars = int(data[1])
                levelStats.close()
            with open('assets/stats/levels/' + self.difficultyName + '/' + self.name[-1] + '.txt', 'w') as levelStats:
                levelStats.writelines(str(min(currentMinTime, self.lastedTime)) + '\n')
                levelStats.writelines(str(max(currentMaxStars, self.collectedStars)) + '\n')
                levelStats.close()
            return collisionResult
