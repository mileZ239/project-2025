import pygame

pygame.init()

WIDTH = HEIGHT = 1200
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson")
clock = pygame.time.Clock()


def init():
    # screen.fill('White')
    imp = pygame.image.load("../i.png")
    screen.blit(imp, (0, 0))


def main():
    running = True
    while running:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        pygame.display.flip()


init()
main()
