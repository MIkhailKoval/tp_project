from state import State, Game
from abc import ABC


class Menu(State, ABC):
    def handle(self):
        pass


class MainMenu(Menu):
    def handle(self):
        print("MainMenu handles request")
        print("MainMenu wants to change the state of the context.")
        self.context.transition_to(Game())


class PauseMenu(Menu):
    def handle(self):
        print("PauseMenu handles request")
        print("PauseMenu wants to change the state of the context.")
        self.context.transition_to(Game())
