import player
import weapon
import pygame
import gamesettings
import math
TYPE_OF_GRAPHICS = 0
window = ''

class Weapon(weapon.Weapon):
    pass


class Tank(player.Player):
    def __init__(self, x ,y):
        self.angle = -1  
        self.x = x
        self.y = y
        self.colour = (0, 255, 0)

    def rotateMuzzle(self, angle):
        draw_tank(self, (255, 255, 0) )
        self.angle += angle * 0.03
        print(self.angle)
        (self.colour, gamesettings.backgroundColour) = ( gamesettings.backgroundColour, self.colour) 
        draw_tank(self)
    def shoot(self):
        pass



class Info:
    '''класс для отображения на экране разной инфы по типу того, чей ход, какой ветер'''
    pass

def draw_tank(tank, colour =(0,0,0)):
    # нарисовали тело танка
    print(tank.colour)
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
    print( math.sqrt((t[0] - tank.x) ** 2 + (tank.y - r - t[1])**2 ))
    pygame.display.update()


