# imports
import pygame


# wall class
class Wall:
    def __init__(self, display, sprite, x, y):
        self.display = display
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'wall'

    # doing stuff
    def run(self):
        self.display.blit(self.sprite, self.rect)
