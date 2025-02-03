import pygame


class Projectile:
    def __init__(self, display, x, y, direction):
        self.display = display

        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0

        self.facing = direction
        self.sprite = pygame.image.load('assets/projectile' + direction + '.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'projectile'

        match self.facing:
            case 'North':
                self.speedY = -5
            case 'South':
                self.speedY = 5
            case 'West':
                self.speedX = -5
            case 'East':
                self.speedX = 5
            case _:
                pass

    def run(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        self.display.blit(self.sprite, self.rect)
