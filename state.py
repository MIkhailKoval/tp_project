from menu_graphics import menu_graphics
from abc import ABC, abstractmethod
import gamesettings as gs
import graphics
from pygame import (
    QUIT, KEYDOWN
)
import pygame
import sys
from visitor import fightVisitor, Player


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


class Game(State):
    def __init__(self):
        self.map = graphics.Map()
        self.fighters = []
        self.alive_tanks = gs.numberOfFighters
        for i in range(gs.numberOfFighters):
            self.fighters.append(Player(graphics.Tank(self, i)))
        pygame.display.update()

        self.visitor = fightVisitor()

    def loop(self) -> str:
        while self.alive_tanks > 1:
            for current_fighter in self.fighters:
                while True:
                    info = current_fighter.accept(self, self.visitor)
                    if info == "Menu":
                        print('Pause')
                        yield "Pause_menu"
                    else:
                        break
            print('Win')
        return "Main_menu"

    def handle(self):
        print("Game handles request.")
        pygame.event.set_allowed([QUIT, KEYDOWN])
        if self.context.info == "New":
            self._loop = self.loop()
        else:
            graphics.show_current_state(self.context.game._screen)
        self.stop_case = next(self._loop)
        print(self.stop_case)
        if self.stop_case == "Pause_menu":
            # print(self.context._screen)
            self.context.info = "Pause_menu"
            self.context.game = self
            self.context.game._screen = graphics.PrtScr()
            self.context.transition_to(Menu())
        else:
            self.context.info = "Main_menu"
            self.context.game = None
            self.context.transition_to(Menu())
        print("Game wants to change the state of the context to", self.stop_case)


class Menu(State):
    def handle(self):
        pygame.key.set_repeat(0, 0)
        pygame.event.set_allowed([QUIT, KEYDOWN])
        print(self.context.info == "Pause_menu", self.context.info)
        if self.context.info == "Main_menu":
            menucontext = Menu_context(
                self.context, Main_menu_selected_new_game())
        elif self.context.info == "Pause_menu":
            menucontext = Menu_context(
                self.context, Pause_menu_selected_return())
        menucontext.work()


class Menu_context(ABC):
    _menu = None
    _graphics: 'menu_graphics'

    def __init__(self, game_context: 'Context', menu: 'Menu_base'):
        self._game_context = game_context
        self._menu = menu
        self._menu.menu_context = self
        self._graphics = menu_graphics(self._menu.options)
        self._graphics.redraw(self._menu.options)
        self._graphics.select(self._menu._selected)

    def reselect(self, menu: 'Menu_base'):
        self._graphics.deselect(self._menu._selected)
        self._menu = menu
        self._menu.menu_context = self
        self._graphics.select(self._menu._selected)

    def go_to_menu(self, menu: 'Menu_base'):
        self._menu = menu
        self._menu.menu_context = self
        self._graphics.redraw(self._menu.options)
        self._graphics.select(self._menu._selected)

    def work(self):
        self._menu.accept()


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

    def accept(self):
        self._go_to_game = False
        event = pygame.event.wait()
        print("event")
        if event.type == QUIT:
            self.quit()
        elif event.type == KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                self.go_up()
            elif pressed_keys[pygame.K_DOWN]:
                self.go_down()
            elif pressed_keys[pygame.K_RETURN]:
                if self.enter():
                    print("Return")
                    return
        self.menu_context.work()

    @abstractmethod
    def enter(self) -> bool:
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


class Main_menu(Menu_base):
    options = ["New game", "Settings", "Quit"]


class Main_menu_selected_new_game(Main_menu):
    _selected = "New game"

    def enter(self):
        self.menu_context._game_context.info = "New"
        self.menu_context._game_context.transition_to(Game())
        return True

    def go_up(self):
        pass

    def go_down(self):
        self.menu_context.reselect(Main_menu_selected_settings())


class Main_menu_selected_settings(Main_menu):
    _selected = "Settings"

    def enter(self):
        return False

    def go_up(self):
        self.menu_context.reselect(Main_menu_selected_new_game())

    def go_down(self):
        self.menu_context.reselect(Main_menu_selected_quit())


class Main_menu_selected_quit(Main_menu):
    _selected = "Quit"

    def enter(self):
        self.quit()
        return True

    def go_up(self):
        self.menu_context.reselect(Main_menu_selected_settings())

    def go_down(self):
        pass


class Pause_menu(Menu_base):
    options = ["Return", "Main menu", "Quit"]


class Pause_menu_selected_return(Pause_menu):
    _selected = "Return"

    def enter(self):
        self.menu_context._game_context.info = "Continue"
        self.menu_context._game_context.transition_to(
            self.menu_context._game_context.game)
        return True

    def go_up(self):
        pass

    def go_down(self):
        self.menu_context.reselect(Pause_menu_selected_main_menu())


class Pause_menu_selected_main_menu(Pause_menu):
    _selected = "Main menu"

    def enter(self):
        self.menu_context.go_to_menu(Main_menu_selected_new_game())
        self.menu_context._game_context.game = None
        return False

    def go_up(self):
        self.menu_context.reselect(Pause_menu_selected_return())

    def go_down(self):
        self.menu_context.reselect(Pause_menu_selected_quit())


class Pause_menu_selected_quit(Pause_menu):
    _selected = "Quit"

    def enter(self):
        self.quit()
        return True

    def go_up(self):
        self.menu_context.reselect(Pause_menu_selected_main_menu())

    def go_down(self):
        pass
