import pygame


class ThornTrap:
    def __init__(self, display, x, y, direction):
        self.display = display

        self.x = x
        self.y = y

        self.cooldown = 0
        self.activated = False

        self.facing = direction
        self.sprite = pygame.image.load('assets/thornsTrapOff.png')
        self.spriteInactivated = pygame.image.load('assets/thornsTrapOff.png')
        self.spriteActivated = pygame.image.load('assets/thornsTrap' + direction + '.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'thornTrap'

    def activate(self):
        self.activated = True
        self.cooldown = 60
        self.sprite = self.spriteActivated
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))

    def inactivate(self):
        self.activated = False
        self.sprite = self.spriteInactivated
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))

    def run(self):
        if self.cooldown > 0:
            self.cooldown -= 1
            if self.cooldown == 0 and self.activated:
                self.inactivate()
            elif self.cooldown == 0 and not self.activated:
                self.activate()
        self.display.blit(self.sprite, self.rect)
