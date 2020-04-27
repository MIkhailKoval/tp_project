import pygame
import fighter
import fighterIterator
import graphics
import gamesettings as gs
from pygame import (
    QUIT, KEYDOWN
)
from state import State
from visitor import fightVisitor, Player
from game import clock
import sys
from menu import Menu

class Game(State):
    def handle(self):
        print("Game handles request.")
        pygame.event.set_allowed(QUIT, KEYDOWN)
        self.cycle()
        print("Game wants to change the state of the context.")
        self.context.transition_to(Menu())
    
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
