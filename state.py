from abc import ABC, abstractmethod
from menu import Menu


class Context(ABC):
    _state = None

    def __init__(self, state: 'State') -> None:
        self.transition_to(state)

    def transition_to(self, state: 'State'):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context: 'Context'):
        self._context = context

    @abstractmethod
    def handle(self):
        pass


class Game(State):
    def handle(self):
        print("Game handles request.")
        print("Game wants to change the state of the context.")
        self.context.transition_to(Menu())


if __name__ == "__main__":

    context = Context(Game())
    context.request1()
    context.request2()
