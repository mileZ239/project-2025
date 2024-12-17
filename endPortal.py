import pygame


class EndPortal:
    def __init__(self, display, x, y):
        self.display = display
        self.x = x
        self.y = y
        self.sprite = pygame.image.load('assets/portal.png')
        self.rect = self.sprite.get_rect(center=(self.x + 15, self.y + 15))
        self.name = 'endPortal'

    # doing stuff
    def run(self):
        self.display.blit(self.sprite, self.rect)
