# imports
import pygame


# class for player
class Player:
    def __init__(self, display, sprite, x=0, y=0):
        self.display = display

        # position
        self.x = x
        self.y = y

        # sprites
        self.sprite = pygame.image.load(sprite).convert()
        self.spriteMoving = pygame.image.load('assets/playerMoving.png').convert()
        self.currentSprite = self.sprite
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))

        # something for colliding with walls
        self.ignoreX = 239
        self.ignoreY = 239
        self.ignoredWalls = []

        # speed and moving state
        self.speedX = 0
        self.speedY = 0
        self.moving = False

        self.name = 'player'

    # movement
    def move(self):
        # moving
        self.x += self.speedX
        self.y += self.speedY

        # changing sprite
        if self.moving:
            self.currentSprite = self.spriteMoving
            return
        self.currentSprite = self.sprite

        # changing direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.moving = True
            self.speedX = 15
        elif keys[pygame.K_a]:
            self.moving = True
            self.speedX = -15
        elif keys[pygame.K_w]:
            self.moving = True
            self.speedY = -15
        elif keys[pygame.K_s]:
            self.moving = True
            self.speedY = 15
        else:
            self.moving = False

    # doing stuff
    def run(self):
        # moving the player
        self.move()
        self.rect = self.currentSprite.get_rect(center=(self.x + 15, self.y + 15))
        self.display.blit(self.currentSprite, self.rect)
