import pygame


class Player:
    def __init__(self, display, sprite, x=0, y=0):
        self.display = display
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite).convert()
        self.spriteMoving = pygame.image.load('assets/playerMoving.png').convert()
        self.currentSprite = self.sprite
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.ignoreX = 239
        self.ignoreY = 239
        self.ignoredWalls = []
        self.speedX = 0
        self.speedY = 0
        self.moving = False
        self.name = 'player'

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

        if self.moving:
            self.currentSprite = self.spriteMoving
            return
        self.currentSprite = self.sprite

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

    def run(self):
        self.move()
        self.rect = self.currentSprite.get_rect(center=(self.x + 15, self.y + 15))
        self.display.blit(self.currentSprite, self.rect)
