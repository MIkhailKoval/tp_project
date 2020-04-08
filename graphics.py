import player
import environment
import weapon
import pygame
import gamesettings
import math
TYPE_OF_GRAPHICS = 0
window = ''

# COLORS
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHT_BLUE = (0, 255, 255)
WHITE = (255, 255, 255)
PINK = (255, 100, 180)
ORANGE = (255, 100, 10)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


class Weapon(weapon.Weapon):
    pass


class Tank(player.Player):
    def __init__(self, map, number):
        self.angle = -1
        self.x, self.y = map.relief.getCoord(
            gamesettings.HEIGHT // (gamesettings.numberOfFighters + 1) * (number + 1))
        self.y += 6
        self.colour = RED
        # вставил костыль для отрисовки танков. Надо исправить!
        self.rotateMuzzle(0)

    def rotateMuzzle(self, angle):
        draw_tank(self, gamesettings.backgroundColour)
        self.angle += angle * 0.01
        print(self.angle)
        draw_tank(self)

    def changeForce(self, value):
        pass

    def shoot(self):
        pass


class Info:
    '''класс для отображения на экране разной инфы по типу того, чей ход, какой ветер'''
    pass


def draw_tank(tank, colour=BLACK):
    # нарисовали тело танка
    r = 10
    x = -r * 10 - 1
    while x < r * 10:
        x += 1
        t = (tank.x - x / 10,  - math.sqrt(r * r - (x) ** 2 / 100) + tank.y)
        pygame.draw.line(window, tank.colour, t, (tank.x - x / 10, tank.y), 3)
    # рисуем дуло
    rd = r + 4
    x = rd * math.cos(tank.angle)
    t = (tank.x + x, - math.sqrt(rd * rd - (x) ** 2) + tank.y - r)
    pygame.draw.line(window, colour, t, (tank.x, tank.y - r), 3)
    pygame.display.update()


class Relief:
    def __init__(self):
        self.draw()

    def getCoord(self, t):
        return [t, t*(t-100)*(t-400)*(t-600) / 20000000 + 210]

    def draw(self):
        points = [self.getCoord(x) for x in range(0, 600)]
        for (x, y_min) in points:
            for y in range(int(y_min + 0.5), 401):
                window.set_at((x, y), GREEN)
        pygame.draw.lines(window, GREEN, False, points)
