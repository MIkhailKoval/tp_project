import player
import environment
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


class Weapon(weapon.Weapon):
    pass


class Tank(player.Player):
    def __init__(self, map, number):
        self.angle = math.pi / 2
        self.x, self.y = map.relief.getCoord(
            gs.HEIGHT // (gs.numberOfFighters + 1) * (number + 1))
        self.y += 6
        self.t = (0, 0)
        self.colour = RED
        # вставил костыль для отрисовки танков. Надо исправить!
        self.rotateMuzzle(0)

    def rotateMuzzle(self, angle):
        draw_tank(self, gs.backgroundColour)
        # пока просто сделаю поворот на 10 градусов
        self.angle += math.pi / 80
        print(self.angle)
        draw_tank(self)


    def changeForce(self, value):
        pass

    def shoot(self):
        v = 10
        x = 0
        y = 0
        t = 0
        #print(self.t)
        while abs(x) <= gs.WIDTH and abs(y) <= gs.HEIGHT:
            x = v * math.cos(self.angle) * t
            y = v * math.sin(self.angle) * t -  t * t / 10
            new_x = int(self.t[1] - y)
            new_y = int(self.t[0] + x)
            window.set_at((new_y, new_x), ORANGE)
            t += 0.01
        '''
        for i in range(600):
            window.set_at((i, int(self.t[1])), ORANGE)
        for j in range(400):
            window.set_at((int(self.t[0]), j), ORANGE)'''
        pygame.display.update()
        

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
