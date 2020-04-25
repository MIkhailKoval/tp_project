import tank
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


tanks = set()


class Weapon(weapon.Weapon):
    pass

class Tank(tank.Tank):
    def __init__(self, number):
        self.angle = math.pi / 2
        self.x, self.y = plan.getCoord(
            0.1 * gs.WIDTH + 0.8 * gs.WIDTH / (gs.numberOfFighters - 1) * number)
        self.y += 6
        self.t = (0, 0)
        self.colour = WHITE
        self.health = 1000
        self.draw_tank()
        #print(self.force)

    def rotateMuzzle(self, angle):
        self.draw_muzzle(gs.backgroundColour)
        self.angle += (angle)
        print(angle)
        if self.angle > math.pi:
            self.angle = 0.0
        if self.angle < 0:
            self.angle = math.pi
        self.draw_muzzle()

    def draw_tank(self):
        if not self in tanks:
            print('add')
            tanks.add(self)
        r = 10
        x = -r * 10 - 1
        while x < r * 10:
            x += 1
            t = (self.x - x / 10,  - math.sqrt(r * r - (x) ** 2 / 100) + self.y)
            pygame.draw.line(window, self.colour, t,
                             (self.x - x / 10, self.y), 2)
        self.draw_muzzle()

    def getAngle(self):
        return self.angle

    def set_angle(self, angle):
        self.draw_muzzle(gs.backgroundColour)
        self.rotateMuzzle(angle)
        self.draw_muzzle()

    def set_health(self, percent):
        pass

    def get_health(self):
        pass

    def draw_muzzle(self, colour=BLACK):
        rd = 14
        x = rd * math.cos(self.angle)
        t = (self.x + x, - math.sqrt(rd * rd - (x) ** 2) + self.y - 10)
        self.t = t
        pygame.draw.line(window, colour, t, (self.x, self.y - 10 - 2), 3)
        pygame.display.update()

    def shoot(self, type_of_weapon, colour=BLUE):
        plan.update()
        #v = self.get_force() / 12.5
        v = 100
        (x, y, t) = (0, 0, 0)
        snaryad = 0
        a = []
        while abs(x) <= gs.WIDTH and abs(y) <= gs.HEIGHT:
            x = v * math.cos(self.angle) * t
            y = v * math.sin(self.angle) * t - t * t / 10
            print(v)
            y = int(self.t[1] - y)
            x = int(self.t[0] + x)
            snaryad += 1
            if y > 0 and x > 0 and x < gs.WIDTH and y < gs.HEIGHT:
                if window.get_at((x, y)) not in [gs.backgroundColour, BLUE, BLACK]:
                    pass
                    #break
                window.set_at((x, y), colour)
                window.set_at((x+1, y), colour)
                a.append((x, y))
                if snaryad % 7 == 0:
                    pygame.display.update()
            t += 0.01
        pygame.display.update()
        if x <= gs.WIDTH and x >= 0:
            explosion(x, y, 30)
        plan.update()
        pygame.display.update()


def explosion(x, y, r):
    pygame.draw.circle(window, RED, (int(x), int(y)), int(r))
    pygame.display.update()
    pygame.time.wait(800)
    pygame.draw.circle(window, LIGHT_BLUE, (int(x), int(y)), int(r))
    updateTanks()
    pygame.display.update()


def updateTanks():
    for tank in tanks:
        if tank.health > 0:
            tank.draw_tank()


class Info:
    '''класс для отображения на экране разной инфы по типу того, чей ход, какой ветер'''
    pass



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
