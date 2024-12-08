from button import Button


class Settings:
    def __init__(self, display):
        self.display = display

    def run(self):
        self.display.fill('black')
