import pygame


class Sounds:
    def __init__(self):
        pygame.mixer.init()
        self.gameOver = pygame.mixer.Sound('assets/nerd.mp3')
        self.giveUp = pygame.mixer.Sound('assets/giveUp.mp3')

    def play(self, sound):
        match sound:
            # case 'gameOver':
            #     self.gameOver.play()
            # case 'giveUp':
            #     self.giveUp.play()
            # case 'stop':
            #     self.gameOver.stop()
            #     self.giveUp.stop()
            case _:
                pass


sounds = Sounds()
