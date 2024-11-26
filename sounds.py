import pygame


class Sounds:
    def __init__(self):
        pygame.mixer.init()
        self.gameOver = pygame.mixer.Sound('assets/nerd.mp3')

    def play(self, sound):
        match sound:
            case 'gameOver':
                self.gameOver.play()
            case 'stop':
                self.gameOver.stop()
            case _:
                pass


sounds = Sounds()
