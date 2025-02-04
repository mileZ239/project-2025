import pygame
import random


class Pufferfish:
    def __init__(self, display, x, y):
        self.display = display

        self.x = x
        self.y = y

        self.sprite = pygame.image.load('assets/pufferfishDeflated.png')
        self.spriteActive = pygame.image.load('assets/pufferfish.png')
        self.spriteDeflated = pygame.image.load('assets/pufferfishDeflated.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'pufferfish'

        self.cooldown = 120
        self.deflated = True

        # difficulty correction
        self.multiplier = 1

    def run(self):
        self.cooldown -= 1
        if self.cooldown <= 0:
            if self.deflated:
                self.deflated = False
                self.sprite = self.spriteActive
                self.cooldown = 30
            else:
                self.deflated = True
                self.sprite = self.spriteDeflated
                self.cooldown = random.randint(120, 180) // self.multiplier
            self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))

        self.display.blit(self.sprite, self.rect)
