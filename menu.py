from state import State, Game
from abc import ABC, abstractmethod
from menu import menu_graphics
import pygame
import sys


class Menu(State, ABC):
    options: 'List[str]'

    def __init__(self):
        pass

    def handle(self):
        menu_graphics(self.options)

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def go_up(self):
        pass

    @abstractmethod
    def go_down(self):
        pass

    def quit(self):
        # pylint: disable=no-member
        pygame.quit()
        # pylint: enable=no-member
        sys.exit()


class MainMenu(Menu, ABC):
    def handle(self):
        print("MainMenu handles request")
        print("MainMenu wants to change the state of the context.")
        self.context.transition_to(Game())


class PauseMenu(Menu, ABC):
    def handle(self):
        print("PauseMenu handles request")
        print("PauseMenu wants to change the state of the context.")
        self.context.transition_to(Game())
