from abc import ABC, abstractmethod
from menu import Menu_base
from state import Game


class Main_menu(Menu_base):
    options = ["New game", "Settings", "Quit"]


class Main_menu_selected_new_game(Main_menu):
    _selected = "New game"

    def enter(self):
        self.menu_context._game_context.info = "New"
        self.menu_context._game_context.transition_to(Game())

    def go_up(self):
        pass

    def go_down(self):
        self.menu_context.reselect("Settings")


class Main_menu_selected_settings(Main_menu):
    _selected = "Settings"

    def enter(self):
        pass

    def go_up(self):
        self.menu_context.reselect("New game")

    def go_down(self):
        self.menu_context.reselect("Quit")


class Main_menu_selected_quit(Main_menu):
    _selected = "Quit"

    def enter(self):
        self.quit()

    def go_up(self):
        self.menu_context.reselect("Settings")

    def go_down(self):
        pass
