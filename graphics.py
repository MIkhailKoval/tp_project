import player
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
    def __init__(self, x ,y):
        self.angle = -1  
        self.x = x
        self.y = y + 6
        self.colour = RED

    def rotateMuzzle(self, angle):
        draw_tank(self, gamesettings.backgroundColour)
        self.angle += angle * 0.03
        print(self.angle)
        draw_tank(self)
    def shoot(self):
        pass



class Info:
    '''класс для отображения на экране разной инфы по типу того, чей ход, какой ветер'''
    pass






def draw_tank(tank, colour =BLACK):
    # нарисовали тело танка
    r = 30
    x = -r * 10 - 1
    while x  < r * 10:
        x += 1
        t = (tank.x - x /10,  - math.sqrt( r * r - (x) ** 2 / 100) + tank.y)  
        pygame.draw.line(window, tank.colour, t, (tank.x - x /10, tank.y), 3)
    # рисуем дуло
    rd = r + 4
    x = rd * math.cos(tank.angle)
    t = (tank.x + x , - math.sqrt( rd * rd - (x) ** 2) + tank.y - r)  
    pygame.draw.line(window, colour, t, (tank.x, tank.y - r), 3)
    pygame.display.update()

class Relief:
    def __init__(self):
        self.draw()
    def draw(self):
        points = [[x, (x*(x-100)*(x-400)*(x-600) /20000000 + 210)] for x in range(0, 600)]
        for (x, y_min) in points:
            for y in range(int(y_min + 0.5), 401):
                window.set_at((x, y), GREEN) 
        pygame.draw.lines(window, GREEN, False, points)