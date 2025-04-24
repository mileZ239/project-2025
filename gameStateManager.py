# класс для управления игровыми состояниями
class GameStateManager:
    def __init__(self, currentState):
        self.statesStack = [currentState]

    def get_state(self):
        return self.statesStack[-1]

    def set_state(self, state):
        self.statesStack.clear()
        self.statesStack.append(state)

    def appendState(self, state):
        self.statesStack.append(state)

    def prevState(self):
        self.statesStack.pop()
