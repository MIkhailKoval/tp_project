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

# TANKS
TANK_RADIUS = 10
MUZZLE_LENGTH = 14


def init_window():
    global window
    window = pygame.display.set_mode((gs.WIDTH, gs.HEIGHT))
    pygame.display.update()


def prt_scr():
    return [[window.get_at((x, y)) for y in range(gs.HEIGHT)]
            for x in range(gs.WIDTH)]


def win():
    window.fill(gs.background_colour)


def show_current_state(matrix):
    for x in range(gs.WIDTH):
        for y in range(gs.HEIGHT):
            window.set_at((x, y), matrix[x][y])


class Tank(tank.Tank):
    def __init__(self, game, number):
        self.x, self.y = game.map.get_coord(0.1 * gs.WIDTH + 0.8 * gs.WIDTH /
                                            (gs.number_of_fighters - 1) * number)
        self.muzzle_coord = (self.x + TANK_RADIUS, self.y + MUZZLE_LENGTH)
        self.draw_muzzle(gs.background_colour)
        self.angle = math.pi / 2
        self.draw_tank()

    def rotate_muzzle(self, angle):
        self.draw_muzzle(gs.background_colour)
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
            pygame.draw.line(window, tank_colour, t,
                             (self.x - x / 10, self.y), 2)

        self.draw_muzzle()

    def get_angle(self):
        return self.angle

    def set_angle(self, angle):
        self.draw_muzzle(gs.background_colour)
        self.rotate_muzzle(angle)
        show_angle(self)
        self.draw_muzzle()

    def draw_muzzle(self, colour=BLACK):
        x = MUZZLE_LENGTH * math.cos(self.angle)
        y = -MUZZLE_LENGTH * math.sin(self.angle)
        self.muzzle_coord = (
            self.x + x, self.y - TANK_RADIUS + y)
        pygame.draw.line(window, colour, self.muzzle_coord,
                         (self.x, self.y - TANK_RADIUS), 3)
        pygame.display.update()

    def shoot(self, game, weapon, force, colour=BLUE):
        game.map.update()
        v = force / 5.5 * 2
        (x, y, t) = (0, 0, 0)
        clock = pygame.time.Clock()
        while abs(x) <= gs.WIDTH and abs(y) <= gs.HEIGHT:
            x = v * math.cos(self.angle) * t
            y = v * math.sin(self.angle) * t - 5 * t * t

            y = int(self.muzzle_coord[1] - y)
            x = int(self.muzzle_coord[0] + x)
            if y > 0 and x > 0 and x < gs.WIDTH and y < gs.HEIGHT:
                print(x, y)
                if window.get_at(
                        (x, y)) not in [gs.background_colour, BLUE, BLACK]:
                    break
                for i in range(3):
                    window.set_at((x + i, y), colour)
                clock.tick(3500)
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
        return explosion(fighters, self.x, self.y, 30, YELLOW)


def explosion(fighters, x, y, r, color=RED):
    pygame.display.update()
    pygame.draw.circle(window, color, (int(x), int(y)), int(r))
    pygame.display.update()
    pygame.time.wait(400)
    pygame.draw.circle(window, LIGHT_BLUE, (int(x), int(y)), int(r))
    distances = []
    for fighter in fighters:
        tank = fighter.impl
        distances.append(pow((tank.x - x)**2 + (tank.y - y)**2, 0.5))
    update_tanks(fighters)
    show_force(color)
    show_angle(tank)
    show_type_of_weapon(color)
    pygame.display.update()
    return distances


def update_tanks(fighters):
    for fighter in fighters:
        if fighter.health > 0:
            fighter.impl.draw_tank()


def show_force(player):
    pygame.draw.rect(window, gs.relief_colour, (gs.WIDTH - 100, 340, 100, 20))
    if not hasattr(player, 'force'):
        return
    _font = pygame.font.Font(None, 18)
    text = _font.render('Force:{}'.format(str(player.force)), 1, RED)
    place = text.get_rect(center=(550, 350))
    window.blit(text, place)
    pygame.display.update()


def show_type_of_weapon(player):
    pygame.draw.rect(window, gs.relief_colour,
                     (gs.WIDTH - 220, gs.HEIGHT - 40, 120, 40))
    if not hasattr(player, 'current_weapon'):
        return
    _font = pygame.font.Font(None, 18)
    print(type(player.current_weapon))
    lst = str(type(player.current_weapon)).replace('_', '')
    text = _font.render('Weapon:{}'.format(lst[15:-2]), 1, RED)
    place = text.get_rect(center=(440, 375))
    window.blit(text, place)
    pygame.display.update()


def show_angle(tank):
    pygame.draw.rect(window, gs.relief_colour,
                     (500, 360, gs.WIDTH - 500, gs.HEIGHT - 360))
    if not hasattr(tank, 'angle'):
        return
    _font = pygame.font.Font(None, 18)
    print(tank.angle)
    angle = int(tank.angle / math.pi * 180)
    text = _font.render('Angle:{}'.format(str(angle)), 1, RED)
    place = text.get_rect(center=(550, 375))
    window.blit(text, place)
    pygame.display.update()


class Map:
    def __init__(self):
        self.reflection = random.randint(0, gs.exists_reflection)
        self.wind = random.randint(0, gs.max_wind)
        pygame.draw.rect(window, gs.background_colour,
                         (0, 0, gs.WIDTH, gs.HEIGHT))
        self.draw_relief()

    def get_coord(self, x):
        return [
            x,
            x * (x - 100) * (x - gs.WIDTH) * (x - gs.HEIGHT) / 20000000 + 210
        ]

    def draw_relief(self):
        points = [self.get_coord(x) for x in range(gs.WIDTH)]
        for (x, y_min) in points:
            for y in range(int(y_min), gs.HEIGHT):
                window.set_at((x, y), gs.relief_colour)

    def update(self):
        for x in range(gs.WIDTH):
            for y in range(gs.HEIGHT):
                if window.get_at((x, y)) == BLUE:
                    window.set_at((x, y), gs.background_colour)
