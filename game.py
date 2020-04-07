import control
import gamesettings
import graphics
import player
import pygame
import sys
from numpy import math
# COLORS
LIGHT_BLUE = (0, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 100, 180)
ORANGE = (255, 100, 10)
YELLOW = (255, 255, 0)
# PARAMETERS
WIDTH = 800
HEIGHT = 600
FPS = 60


class main_window():
    def __init__(self):
        pygame.init()
        self.height = 400
        self.width = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.update()
        self.objects = []
        self.cycle()

    def update(self):
        # пока просто для наполненности написал:
        pygame.draw.rect(self.window, YELLOW, (0, 0, 600, 200))
        pygame.draw.rect(self.window, LIGHT_BLUE, (0, 200, 600, 400))
        pygame.draw.lines(self.window, BLACK, False, [
                          [30 * math.sin(x), 30 * x] for x in range(0, 600)])
        pygame.display.update()
        # for obj in self.objects:
        #    obj.update()

    def cycle(self):
        clock = pygame.time.Clock()
        while True:
            currentNumOfFighters = gamesettings.numberOfFighters
            fighters = list()
            for i in range(gamesettings.numberOfFighters):
                # здесь инициализация танков, определение их местоположения и первая отрисовка
                fighters.append(graphics.Tank())

            while currentNumOfFighters > 1:
                for currentFighter in fighters:
                    wasShoot = False
                    while not wasShoot:
                        event = pygame.event.wait()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            pressedCtrl = (event.mod == pygame.KMOD_CTRL)
                            if(event.key == control.clockwiseRotationMuzzle):
                                currentFighter.rotateMuzzle(
                                    -1 - 9 * pressedCtrl)
                                print("RIGHT")
                            elif event.key == control.anticlockwiseRotationMuzzle:
                                currentFighter.rotateMuzzle(1 +
                                                            9 * pressedCtrl)
                                print("LEFT")
                            elif event.key == control.shoot:
                                currentFighter.shoot()
                                wasShoot = True
                                print("ENTER")


main_window()
