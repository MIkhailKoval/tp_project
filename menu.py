from state import State, Context
from abc import ABC, abstractmethod
from main_menu import Main_menu_selected_new_game
from pause_menu import Pause_menu_selected_return
import pygame
from pygame import (
    QUIT, KEYDOWN
)
from pygame.key import(
    K_UP, K_DOWN, K_RETURN
)
import sys
from menu_graphics import menu_graphics
from state_game import Game


class Menu(State):
    def handle(self):
        pygame.key.set_repeat(0, 0)
        pygame.event.set_allowed(QUIT, KEYDOWN)
        if self.context.info == "Main_menu":
            menucontext = Menu_context(
                self.context, Main_menu_selected_new_game())
        elif self.context.info == "Pause_menu":
            menucontext = Menu_context(
                self.context, Pause_menu_selected_return())
        menucontext.work()


class Menu_context(ABC):
    _menu: 'Menu_base'
    _graphics: 'menu_graphics'

    def __init__(self, game_context: 'Context', menu: 'Menu_base', option: str = _menu.options[0]):
        _graphics = menu_graphics(self._menu.options)
        self._game_context = game_context
        self.go_to_menu(menu)
        self.reselect(option)

    def reselect(self, option: 'str'):
        self._graphics.deselect(self._menu._selected)
        self._menu._selected = option
        self._menu.menu_context = self
        self._graphics.select(self._menu._selected)

    def go_to_menu(self, menu: 'Menu_base'):
        self._menu = menu
        self._menu.menu_context = self
        self._graphics.redraw(self._menu.options)

    def work(self):
        self._menu.handle()


class Menu_base(ABC):
    options: 'List[str]'
    _selected: 'str'
    _menu_context: 'Menu_context'

    @property
    def menu_context(self):
        return self._menu_context

    @menu_context.setter
    def menu_context(self, menu_context: 'Menu_context'):
        self._menu_context = menu_context

    def handle(self):
        pygame.event.wait()
        if pygame.event.type == QUIT:
            self.quit()
        elif pygame.event.type == KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP]:
                self.go_up()
            elif pressed_keys[K_DOWN]:
                self.go_down()
            elif pressed_keys[K_RETURN]:
                self.enter()
        self.menu_context.work()

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
