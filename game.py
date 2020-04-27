import gamesettings as gs
import graphics
import pygame
import sys
from numpy import math
import state
from menu import Menu


class main_window():
    def __init__(self):
        # pylint: disable=no-member
        pygame.init()
        graphics.window = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
        pygame.draw.rect(
            graphics.window, gs.backgroundColour, (0, 0, gs.WIDTH, gs.HEIGHT))
        self.objects = []
        pygame.display.update()
        # pylint: disable=no-member
        self.context = state.Context(Menu())  
        self.context.info = 'Main_menu'
        self.context.request()

'''
    def cycle(self):
        self.map = graphics.Map()
        graphics.plan = self.map

        fighters = fighterIterator.Fighters()
        for i in range(gs.numberOfFighters):
            fighters.add(Player(graphics.Tank(i)))
        pygame.display.update()

        fighter = fighters.__iter__()
        visitor = fightVisitor()

        for currentFighter in fighter:
            currentFighter.accept(visitor)
            clock.tick(gs.FPS/10)
        print('Win')
        sys.exit()
'''

clock = pygame.time.Clock()
if __name__ == "__main__":
    main_window()
    # pylint: disable=no-member