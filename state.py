from abc import ABC, abstractmethod
import menu
import pygame
from pygame.constants import (
    QUIT, KEYDOWN
)


class Context(ABC):
    _state = None
    info = str()

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
        pygame.event.set_allowed(QUIT, KEYDOWN)
        print("Game wants to change the state of the context.")
        self.context.transition_to(menu.Menu())
