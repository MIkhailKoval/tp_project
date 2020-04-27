from abc import ABC, abstractmethod
from menu import Menu_base
from main_menu import Main_menu_selected_new_game
from state import Game


class Pause_menu(Menu_base):
    options = ["Return", "Main menu", "Quit"]


class Pause_menu_selected_return(Pause_menu):
    _selected = "Return"

    def enter(self):
        self.menu_context._game_context.info = "Continue"
        self.menu_context._game_context.transition_to(Game())

    def go_up(self):
        pass

    def go_down(self):
        self.menu_context.reselect("Main_menu")


class Pause_menu_selected_main_menu(Pause_menu):
    _selected = "Main menu"

    def enter(self):
        self.menu_context.go_to_menu(Main_menu_selected_new_game())

    def go_up(self):
        self.menu_context.reselect("Return")

    def go_down(self):
        self.menu_context.reselect("Quit")


class Pause_menu_selected_quit(Pause_menu):
    _selected = "Quit"

    def enter(self):
        self.quit()

    def go_up(self):
        self.menu_context.reselect("Main menu")

    def go_down(self):
        pass
