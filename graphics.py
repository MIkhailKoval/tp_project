import player
import environment
import functools
import weapon
import pygame
import gamesettings as gs
import math
import random
TYPE_OF_GRAPHICS = 0
window = ''
plan = ''
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
#

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
    def __init__(self, number):
        self.angle = math.pi / 2
        self.x, self.y = plan.getCoord(
            gs.WIDTH // (gs.numberOfFighters + 1) * (number + 1))
        self.y += 6
        self.t = (0, 0)
        self.colour = WHITE
        # вставил костыль для отрисовки танков. Надо исправить!
        draw_tank(self)
        '''да нормас'''

    @degrees(2)
    def rotateMuzzle(self, angle):
        draw_muzzer(self, gs.backgroundColour)
        self.angle += angle
        if self.angle > math.pi:
            self.angle -= math.pi
        if self.angle < 0:
            self.angle += math.pi
        draw_muzzer(self)

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


def draw_tank(tank):
    # нарисовали тело танка
    r = 10
    x = -r * 10 - 1
    while x < r * 10:
        x += 1
        t = (tank.x - x / 10,  - math.sqrt(r * r - (x) ** 2 / 100) + tank.y)
        pygame.draw.line(window, tank.colour, t, (tank.x - x / 10, tank.y), 2)
    draw_muzzer(tank)

def draw_muzzer(tank, colour = BLACK):
    # рисуем дуло
    rd = 14
    x = rd * math.cos(tank.angle)
    t = (tank.x + x, - math.sqrt(rd * rd - (x) ** 2) + tank.y - 10)
    tank.t = t
    pygame.draw.line(window, colour, t, (tank.x, tank.y - 10 - 2), 3)
    pygame.display.update()
                

def shoot(tank, colour = BLUE):
    plan.update()
    v = tank.force / 12.5
    (x, y, t) = (0, 0, 0)
    snaryad = 0
    a = []
    while abs(x) <= gs.WIDTH and abs(y) <= gs.HEIGHT:
        x = v * math.cos(tank.angle) * t
        y = v * math.sin(tank.angle) * t - t * t / 10
        y = int(tank.t[1] - y)
        x = int(tank.t[0] + x)
        print(x, y)
        snaryad += 1
        if y > 0 and x > 0 and x < gs.WIDTH and y < gs.HEIGHT:    
            if window.get_at((x, y)) not in [gs.backgroundColour, BLUE, BLACK]:
                print(window.get_at((x, y)), '   ' , BLUE)
                break
            window.set_at((x, y), colour)
            window.set_at((x+1,y), colour)
            a.append((x,y))
        #if snaryad > 7:
        #window.set_at(a[-7], gs.backgroundColour)
        #window.set_at((a[-7][0] + 1,a[-7][1]), gs.backgroundColour)
        '''нижнюю строчку надо в иф'''
        pygame.display.update()
        t += 0.01
    # здесь вызывай взрыв в точке x, y


class Map:
    def __init__(self):
        self.reflection = random.randint(0, gs.existsReflection)
        self.wind = random.randint(0, gs.maxWind)
        self.draw_relief()
    def getCoord(self, t):
        return [t, t*(t - 100)*(t - gs.WIDTH)*(t - gs.HEIGHT) / 20000000 + 210]

    def draw_relief(self):
        points = [self.getCoord(x) for x in range(gs.WIDTH)]
        for (x, y_min) in points:
            for y in range(int(y_min + 0.5), gs.HEIGHT):
                window.set_at((x, y), gs.reliefColour)
    def update(self):
        for x in range(gs.WIDTH):
            for y in range(gs.HEIGHT):
                if window.get_at((x, y)) == BLUE:
                    window.set_at((x, y), gs.backgroundColour)