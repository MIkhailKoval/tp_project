import control
import environment
import fighterIterator
import gamesettings
import gamesettings as gs
import graphics
from visitor import Player, fightVisitor
import tank
import pygame
import sys
from numpy import math


class main_window():
    def __init__(self):
        # pylint: disable=no-member
        pygame.init()
        # pylint: enable=no-member
        graphics.window = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
        self.update()
        self.objects = []
        pygame.display.update()
        pygame.key.set_repeat(100, 1000 // gs.FPS)
        self.cycle()

    def update(self):
        pygame.draw.rect(
            graphics.window, gamesettings.backgroundColour, (0, 0, gs.WIDTH, gs.HEIGHT))
        pygame.display.update()

    def cycle(self):
        clock = pygame.time.Clock()
        while True:
            self.map = graphics.Map()
            graphics.plan = self.map

            fighters = fighterIterator.Fighters()
            for i in range(gs.numberOfFighters):
                # здесь инициализация танков, определение их местоположения и первая отрисовка
                fighters.add(Player(graphics.Tank(i)))
            pygame.display.update()

            fighter = fighters.__iter__()
            visitor = fightVisitor()
            for currentFighter in fighter:
                currentFighter.accept(visitor)
                clock.tick(gs.FPS)
            print('Win')
            sys.exit()


if __name__ == "__main__":
    main_window()
