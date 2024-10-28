# level class
class Level:
    def __init__(self, display, gameStateManager, background):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = background

    # doing stuff
    def run(self):
        self.display.blit(self.background, (0, 0))
