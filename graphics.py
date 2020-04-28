import functools
import gamesettings as gs
import math
import pygame
import random
import tank
import weapon
window = None
plan = None
tanks = set()

# COLORS
BLUE = (0, 0, 100, 255)
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


def init_window():
    global window
    window = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
    pygame.display.update()


class Tank(tank.Tank):
    def __init__(self, number):
        self.angle = math.pi / 2
        self.x, self.y = plan.getCoord(
            0.1 * gs.WIDTH + 0.8 * gs.WIDTH / (gs.numberOfFighters - 1) * number)
        self.t = (0, 0)
        self.colour = WHITE
        self.draw_tank()

    def rotateMuzzle(self, angle):
        self.draw_muzzle(gs.backgroundColour)
        self.angle += (angle)
        if self.angle > math.pi:
            self.angle = 0.0
        if self.angle < 0:
            self.angle = math.pi
        self.draw_muzzle()

    def draw_tank(self, tank_colour=WHITE):
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

    def get_angle(self):
        return self.angle

    def set_angle(self, angle):
        self.draw_muzzle(gs.backgroundColour)
        self.rotateMuzzle(angle)
        self.draw_muzzle()

    def set_health(self, percent):
        self.health *= (1 - percent)

    def get_health(self):
        return self.health

    def draw_muzzle(self, colour=BLACK):
        rd = 14
        x = rd * math.cos(self.angle)
        t = (self.x + x, - math.sqrt(rd * rd - (x) ** 2) + self.y - 10)
        self.t = t
        pygame.draw.line(window, colour, t, (self.x, self.y - 10 - 2), 3)
        pygame.display.update()

    def shoot(self, weapon, force, colour=BLUE):
        plan.update()
        v = force/12.5
        (x, y, t) = (0, 0, 0)
        snaryad = 0
        a = []
        while abs(x) <= gs.WIDTH and abs(y) <= gs.HEIGHT:
            x = v * math.cos(self.angle) * t
            y = v * math.sin(self.angle) * t - t * t / 2
            y = int(self.t[1] - y)
            x = int(self.t[0] + x)
            snaryad += 1
            if y > 0 and x > 0 and x < gs.WIDTH and y < gs.HEIGHT:
                if window.get_at((x, y)) not in [gs.backgroundColour, BLUE, BLACK]:
                    break
                a.append((x, y))
                for i in range(3):
                    window.set_at((x + i, y), colour)
                a.append((x, y))
                if snaryad % 7 == 0:
                    pygame.display.update()
            t += 0.01
        pygame.display.update()
        distances = []
        if x <= gs.WIDTH and x >= 0:
            distances = explosion(x, y, weapon.radius)
        plan.update()
        pygame.display.update()
        #for tank in tanks:
        #distances.append( (tank.x - x)**2 + (tank.y - y)**2)
        #distances.append(tank.health)
        return distances


def explosion(x, y, r, color=RED,  update=1):
    pygame.draw.circle(window, color, (int(x), int(y)), int(r))
    pygame.display.update()
    pygame.time.wait(400)
    pygame.draw.circle(window, LIGHT_BLUE, (int(x), int(y)), int(r))
    distances = []
    for tank in tanks:
        distances.append( (tank.x - x)**2 + (tank.y - y)**2)
        #if (10 + r)**2 >= (tank.x - x)**2 + (tank.y - y)**2:
            #tank.set_health(1)
    #if update:
    #    updateTanks()
    pygame.display.update()
    return distances


def updateTanks():
    for tank in tanks:
        print(tank.health)
        if tank.health > 0:
            tank.draw_tank()
        else:
            tank.draw_muzzle(BLUE)
            explosion(tank.x, tank.y - 12, 24, YELLOW, 0)


class Info:
    '''класс для отображения на экране разной инфы по типу того, чей ход, какой ветер'''
    pass


class Map:
    def __init__(self, ):
        self.reflection = random.randint(0, gs.existsReflection)
        self.wind = random.randint(0, gs.maxWind)
        pygame.draw.rect(window, gs.backgroundColour, (0, 0, gs.WIDTH, gs.HEIGHT))
        self.draw_relief()
        global plan
        plan = self

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
