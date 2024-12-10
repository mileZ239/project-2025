# imports
from player import Player


# level class
class Level:
    def __init__(self, display, gameStateManager, background):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = background
        self.player = Player(display)
        self.paused = False

    def pause(self):
        self.paused = True
        self.gameStateManager.setState('pause')
