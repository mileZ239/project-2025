import pygame


class Player:
    def __init__(self, display, sprite, x=0, y=0):
        self.display = display
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite).convert()
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.ignoreX = 239
        self.ignoreY = 239
        self.speedX = 0
        self.speedY = 0
        self.moving = False

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

        if self.moving:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.moving = True
            self.speedX = 20
        elif keys[pygame.K_a]:
            self.moving = True
            self.speedX = -20
        elif keys[pygame.K_w]:
            self.moving = True
            self.speedY = -20
        elif keys[pygame.K_s]:
            self.moving = True
            self.speedY = 20

    def run(self):
        self.move()
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.display.blit(self.sprite, self.rect)
