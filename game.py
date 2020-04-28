import gamesettings as gs
import graphics
from numpy import math
import pygame
from state import Context, Menu
import sys


class main_window():
    def __init__(self):
        # pylint: disable=no-member
        pygame.init()
        window = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
        pygame.draw.rect(
            window, gs.backgroundColour, (0, 0, gs.WIDTH, gs.HEIGHT))
        self.objects = []
        pygame.display.update()
        # pylint: disable=no-member
        self.context = Context(Menu())
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
