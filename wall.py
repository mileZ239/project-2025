import pygame


class Wall:
    def __init__(self, display, sprite, x, y):
        self.display = display
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.name = 'wall'

    def run(self):
        self.display.blit(self.sprite, self.rect)
