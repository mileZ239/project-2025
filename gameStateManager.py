# class for managing game states
class GameStateManager:
    def __init__(self, currentState):
        self.statesStack = [currentState]

    # getting current state
    def get_state(self):
        return self.statesStack[-1]

    # setting state
    def set_state(self, state):
        self.statesStack.clear()
        self.statesStack.append(state)

    def appendState(self, state):
        self.statesStack.append(state)

    def prevState(self):
        self.statesStack.pop()
