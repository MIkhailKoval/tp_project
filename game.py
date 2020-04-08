import control
import gamesettings
import gamesettings as gs
import graphics
import player
import pygame
import sys
import map
from numpy import math

class main_window():
    def __init__(self):
        pygame.init()
        graphics.window = pygame.display.set_mode((gs.HEIGHT, gs.WIDTH))
        self.update()
        self.objects = []
        map.Map()
        pygame.display.update()
        self.cycle()

    def update(self):
        pygame.draw.rect(graphics.window, gamesettings.backgroundColour, (0, 0, gs.HEIGHT, gs.WIDTH))
        pygame.display.update()
        # for obj in self.objects:
        #    obj.update()

    def cycle(self):
        clock = pygame.time.Clock()
        map.Map()
        while True:
            currentNumOfFighters = gs.numberOfFighters
            fighters = list()
            for i in range(gs.numberOfFighters):
                # здесь инициализация танков, определение их местоположения и первая отрисовка
                x = 300 
                y = 300
                fighters.append(graphics.Tank(x, y))

            while currentNumOfFighters > 1:
                for currentFighter in fighters:
                    pygame.key.set_repeat(500, 500 // gs.FPS)
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
                                    1 + 9 * pressedCtrl)
                                print("LEFT")
                            if pressed_keys[control.negRotate]:
                                currentFighter.rotateMuzzle(
                                    -1 - 9 * pressedCtrl)
                                print("RIGHT")
                            if pressed_keys[control.shoot]:
                                pygame.key.set_repeat(0, 0)
                                currentFighter.shoot()
                                print("ENTER")
                                break
                        clock.tick(gs.FPS)
            print('Win')
            sys.exit()


main_window()

