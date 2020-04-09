import player
import environment
import functools
import weapon
import pygame
import gamesettings as gs
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
MAX_FORCE = 200
MIN_FORCE = 1


class Weapon(weapon.Weapon):
    pass


def degrees(angleIndex):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            args = list(args)
            args[angleIndex - 1] *= math.pi / 180
            args = tuple(args)
            return func(*args, **kwargs)
        return inner
    return wrapper


class Tank(player.Player):
    def __init__(self, map, number):
        self.angle = math.pi / 2
        self.x, self.y = map.relief.getCoord(
            gs.WIDTH // (gs.numberOfFighters + 1) * (number + 1))
        self.y += 6
        self.t = (0, 0)
        self.colour = RED
        # вставил костыль для отрисовки танков. Надо исправить!
        self.rotateMuzzle(0)

    @degrees(2)
    def rotateMuzzle(self, angle):
        draw_tank(self, gs.backgroundColour)
        self.angle += angle
        if self.angle > math.pi:
            self.angle -= math.pi
        if self.angle < 0:
            self.angle += math.pi
        #print("angle", int(self.angle * 180 / math.pi))
        draw_tank(self)

    def changeForce(self, value):
        self.force += value
        if self.force > MAX_FORCE:
            self.force = MAX_FORCE
        elif self.force < MIN_FORCE:
            self.force = MIN_FORCE
        print("force", self.force)

    def shoot(self):
        shoot(self)



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
    tank.t = t
    pygame.draw.line(window, colour, t, (tank.x, tank.y - r), 3)
    pygame.display.update()

def shoot(tank, colour = BLUE):
    v = tank.force / 12.5
    x = 0
    y = 0
    t = 0
    while abs(x) <= gs.WIDTH and abs(y) <= gs.HEIGHT:
        x = v * math.cos(tank.angle) * t
        y = v * math.sin(tank.angle) * t - t * t / 10
        new_x = int(tank.t[1] - y)
        new_y = int(tank.t[0] + x)
        window.set_at((new_y, new_x), colour)
        t += 0.01
    pygame.display.update()

class Relief:
    def __init__(self):
        self.draw()

    def getCoord(self, t):
        return [t, t*(t - 100)*(t - gs.WIDTH)*(t - gs.HEIGHT) / 20000000 + 210]

    def draw(self):
        points = [self.getCoord(x) for x in range(gs.WIDTH)]
        for (x, y_min) in points:
            for y in range(int(y_min + 0.5), gs.HEIGHT):
                window.set_at((x, y), GREEN)
        pygame.draw.lines(window, GREEN, False, points)
