import random
import pygame
from projectile import Projectile


class Cannon:
    def __init__(self, display, x, y, direction):
        self.display = display

        self.x = x
        self.y = y

        self.facing = direction
        self.sprite = pygame.image.load('assets/cannon' + direction + '.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'cannon'

        self.projectiles = []
        self.cooldown = 120

    def updateProjectiles(self):
        for projectile in self.projectiles:
            projectile.run()

    def run(self):
        self.cooldown -= 1
        if self.cooldown == 0:
            self.projectiles.append(Projectile(self.display, self.x, self.y, self.facing))
            self.cooldown = random.randint(150, 240)
        self.updateProjectiles()
        self.display.blit(self.sprite, self.rect)
