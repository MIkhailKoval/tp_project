import functools
import gamesettings as gs
import math
import pygame
import random
import tank
import weapon
window = None

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
# tank
TANK_RADIUS = 10
MUZZLE_LENGTH = 14


def init_window():
    global window
    window = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
    pygame.display.update()


def PrtScr():
    return [[window.get_at((x, y)) for y in range(gs.HEIGHT)]
            for x in range(gs.WIDTH)]


def show_current_state(matrix):
    for x in range(gs.WIDTH):
        for y in range(gs.HEIGHT):
            window.set_at((x, y), matrix[x][y])


class Tank(tank.Tank):
    def __init__(self, game, number):
        self.x, self.y = game.map.getCoord(0.1 * gs.WIDTH + 0.8 * gs.WIDTH /
                                           (gs.numberOfFighters - 1) * number)
        self.muzzle_coord = (self.x + TANK_RADIUS, self.y + MUZZLE_LENGTH)
        self.colour = WHITE
        self.draw_muzzle(gs.backgroundColour)
        self.angle = math.pi / 2
        self.draw_tank()

    def rotateMuzzle(self, angle):
        #print(self.angle, angle)
        self.draw_muzzle(gs.backgroundColour)
        self.angle += (angle)
        if self.angle > math.pi:
            self.angle = 0.0
        if self.angle < 0:
            self.angle = math.pi
        self.draw_muzzle()

    def draw_tank(self, tank_colour=WHITE):
        x = -TANK_RADIUS * 10 - 1
        while x < TANK_RADIUS * 10:
            x += 1
            t = (self.x - x / 10,
                 -math.sqrt(TANK_RADIUS * TANK_RADIUS - (x)**2 / 100) + self.y)
            pygame.draw.line(window, self.colour, t,
                             (self.x - x / 10, self.y), 2)
        self.draw_muzzle()

    def get_angle(self):
        return self.angle

    def set_angle(self, angle):
        self.draw_muzzle(gs.backgroundColour)
        self.rotateMuzzle(angle)
        self.draw_muzzle()

    def draw_muzzle(self, colour=BLACK):
        x = MUZZLE_LENGTH * math.cos(self.angle)
        self.muzzle_coord = (
            self.x + x,
            -math.sqrt(MUZZLE_LENGTH * MUZZLE_LENGTH - (x)**2) + self.y - 10)
        pygame.draw.line(window, colour, self.muzzle_coord,
                         (self.x, self.y - 10 - 2), 3)
        pygame.display.update()

    def shoot(self, game, weapon, force, colour=BLUE):
        game.map.update()
        v = force
        (x, y, t) = (0, 0, 0)
        snaryad = 0
        a = []
        while abs(x) <= gs.WIDTH and abs(y) <= gs.HEIGHT:
            x = v * math.cos(self.angle) * t / 5.5
            y = v * math.sin(self.angle) * t / 5.5 - t * t / 2
            y = int(self.muzzle_coord[1] - y)
            x = int(self.muzzle_coord[0] + x)
            snaryad += 1
            if y > 0 and x > 0 and x < gs.WIDTH and y < gs.HEIGHT:
                if window.get_at(
                        (x, y)) not in [gs.backgroundColour, BLUE, BLACK]:
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
        game.map.update()
        if x <= gs.WIDTH and x >= 0:
            distances = explosion(game.fighters, x, y, weapon.radius)
        pygame.display.update()
        return distances

    def detonate(self, fighters):
        explosion(fighters, self.x, self.y, 30, YELLOW)


def explosion(fighters, x, y, r, color=RED):
    pygame.display.update()
    pygame.draw.circle(window, color, (int(x), int(y)), int(r))
    pygame.display.update()
    pygame.time.wait(400)
    pygame.draw.circle(window, LIGHT_BLUE, (int(x), int(y)), int(r))
    distances = []
    for fighter in fighters:
        tank = fighter.impl
        distances.append((tank.x - x)**2 + (tank.y - y)**2)
        '''
        if (10 + r)**2 >= (tank.x - x)**2 + (tank.y - y)**2:
            old_health = tank.health
            tank.set_health(gs.maxHealth / 2)
            if tank.health <= 0 and old_health > 0:
                tank.draw_muzzle(BLUE)
                explosion(tank.x, tank.y - MUZZLE_LENGTH,
                          TANK_RADIUS + MUZZLE_LENGTH, YELLOW)
        '''
    updateTanks(fighters)
    pygame.display.update()
    return distances


def updateTanks(fighters):
    for fighter in fighters:
        print(fighter.health)
        if fighter.health > 0:
            fighter.impl.draw_tank()


class Info:
    '''класс для отображения на экране разной инфы по типу того, чей ход, какой ветер'''
    pass


class Map:
    def __init__(self):
        self.reflection = random.randint(0, gs.existsReflection)
        self.wind = random.randint(0, gs.maxWind)
        pygame.draw.rect(window, gs.backgroundColour,
                         (0, 0, gs.WIDTH, gs.HEIGHT))
        self.draw_relief()

    def getCoord(self, x):
        return [
            x,
            x * (x - 100) * (x - gs.WIDTH) * (x - gs.HEIGHT) / 20000000 + 210
        ]

    def draw_relief(self):
        points = [self.getCoord(x) for x in range(gs.WIDTH)]
        for (x, y_min) in points:
            for y in range(int(y_min), gs.HEIGHT):
                window.set_at((x, y), gs.reliefColour)

    def update(self):
        for x in range(gs.WIDTH):
            for y in range(gs.HEIGHT):
                if window.get_at((x, y)) == BLUE:
                    window.set_at((x, y), gs.backgroundColour)
