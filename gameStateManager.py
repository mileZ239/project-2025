# class for managing game states
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    # getting current state
    def get_state(self):
        return self.currentState

    # setting state
    def set_state(self, state):
        self.currentState = state
