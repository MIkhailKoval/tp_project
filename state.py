from abc import ABC, abstractmethod

class Context(ABC):
    _state = None
    info = str()

    def __init__(self, state: 'State') -> None:
        self.transition_to(state)

    def transition_to(self, state: 'State'):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request(self):
        self._state.handle()


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


