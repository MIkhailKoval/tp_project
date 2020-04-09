import control
import environment
import gamesettings
import gamesettings as gs
import graphics
import player
import pygame
import sys
from numpy import math


class main_window():
    def __init__(self):
        pygame.init()
        graphics.window = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
        self.update()
        self.objects = []
        pygame.display.update()
        self.cycle()

    def update(self):
        pygame.draw.rect(
            graphics.window, gamesettings.backgroundColour, (0, 0, gs.WIDTH, gs.HEIGHT))
        pygame.display.update()
        # for obj in self.objects:
        #    obj.update()

    def cycle(self):
        clock = pygame.time.Clock()
        while True:
            self.map = environment.Map()
            currentNumOfFighters = gs.numberOfFighters
            fighters = list()
            for i in range(gs.numberOfFighters):
                # здесь инициализация танков, определение их местоположения и первая отрисовка
                fighters.append(graphics.Tank(self.map, i))
            pygame.display.update()

            while currentNumOfFighters > 1:
                for currentFighter in fighters:
                    pygame.key.set_repeat(100, 1000 // gs.FPS)
                    if currentFighter.health <= 0:
                        continue
                    while True:
                        event = pygame.event.poll()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            pressed_keys = pygame.key.get_pressed()
                            pressed_mod_keys = pygame.key.get_mods()
                            pressedCtrl = bool(
                                pressed_mod_keys & pygame.KMOD_CTRL)
                            if pressedCtrl:
                                print("Ctrl")
                            if pressed_keys[control.posRotate]:
                                currentFighter.rotateMuzzle(
                                    1 + 4 * pressedCtrl)
                                print("RIGHT")
                            if pressed_keys[control.negRotate]:
                                currentFighter.rotateMuzzle(
                                    -1 - 4 * pressedCtrl)
                                print("LEFT")
                            if pressed_keys[control.boostForce]:
                                currentFighter.changeForce(1 + 4 * pressedCtrl)
                                print("UP")
                            if pressed_keys[control.reduceForce]:
                                currentFighter.changeForce(-1 -
                                                           4 * pressedCtrl)
                                print("DOWN")
                            if pressed_keys[control.shoot]:
                                pygame.key.set_repeat(0, 0)
                                currentFighter.shoot()
                                print("ENTER")
                                break
                        clock.tick(gs.FPS)
            print('Win')
            sys.exit()


main_window()
