import gamesettings as gs
import graphics
from numpy import math
import pygame
from state import Context, Menu, Game
import sys


class main_window():
    def __init__(self):
        # pylint: disable=no-member
        pygame.init()
        # pylint: disable=no-member
        graphics.init_window()
        self.objects = []

        self.context = Context(Menu())
        self.context.info = 'Main_menu'
        self.context.game = None

        '''
        self.context = Context(Game())
        self.context.info = "New"
        '''
        while True:
            print("----------REQUEST------------")
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
