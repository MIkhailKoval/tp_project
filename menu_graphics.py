import gamesettings as gs
import graphics
import pygame
import sys
from pygame.constants import (
    QUIT, KEYDOWN
)

ACTIVE_FONT_COLOUR = (100, 0, 0)
PASSIVE_FONT_COLOUR = (0, 100, 0)
MENU_BACKGROUND_COLOUR = (200, 200, 200)
SMALL_FONT = 36
BIG_FONT = 48

# Настройки меню:
WORD_LENGTH = 300
COUNT_FOR_SMALL_FONT = 6
class menu_graphics:
    _font = property()

    def __init__(self, options: 'List[str]'):
        graphics.window.fill(MENU_BACKGROUND_COLOUR)
        pygame.display.update()
        self.buttons = dict()
        self.count = len(self.buttons)

    @_font.setter
    def _font(self, value):
        _font = value

    @_font.getter
    def _font(self):
        return pygame.font.Font(None, SMALL_FONT * (self.count >= COUNT_FOR_SMALL_FONT) + BIG_FONT * (self.count < COUNT_FOR_SMALL_FONT))

    def redraw(self, options: 'List[str]'):
        graphics.window.fill(MENU_BACKGROUND_COLOUR)
        x = 30
        self.count = len(options)
        delta = (gs.HEIGHT - (self.count < COUNT_FOR_SMALL_FONT) * x * 2 - x) / self.count * 0.5
        self.buttons = dict(
            zip(options, [(WORD_LENGTH, x + delta * (2 * y + 1)) for y in range(0, self.count)]))

        for key, value in self.buttons.items():
            text = self._font.render(key, 1, PASSIVE_FONT_COLOUR)
            place = text.get_rect(center=value)
            graphics.window.blit(text, place)
        pygame.display.update()

    def select(self, name: str):
        text = self._font.render(name, 1, ACTIVE_FONT_COLOUR)
        place = text.get_rect(center=self.buttons[name])
        graphics.window.blit(text, place)
        pygame.display.update()

    def deselect(self, name: str):
        text = self._font.render(name, 1, PASSIVE_FONT_COLOUR)
        place = text.get_rect(center=self.buttons[name])
        graphics.window.blit(text, place)
        pygame.time.wait(200)
        pygame.display.update()

