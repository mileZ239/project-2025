import pygame


class Bat:
    def __init__(self, display, x, y, direction, flyingRange=200):
        self.display = display
        self.baseX = x
        self.baseY = y
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        if direction == 'hor':
            self.speedX = 5
        else:
            self.speedY = 5
        self.flyingRange = flyingRange
        self.delay = 1000
        self.sprite = pygame.image.load('assets/bat.png')
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.name = 'bat'

    def run(self):
        self.x += self.speedX
        self.y += self.speedY
        if abs(self.x - self.baseX) + abs(self.y - self.baseY) >= self.flyingRange:
            self.speedX = -self.speedX
            self.speedY = -self.speedY
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.display.blit(self.sprite, self.rect)
