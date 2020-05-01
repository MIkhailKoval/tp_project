from abc import ABC, abstractmethod
from collections import OrderedDict
import fighterIterator
import math
import weapon

MAX_FORCE = 200
MIN_FORCE = 1

class Fighter(ABC):
    weapons = {weapon.usualBomb: 100, weapon.bullet: 9999,
               weapon.kiloton: 3, weapon.atomBomb: 1, weapon.laser: 0}
    currentWeapon = weapon.usualBomb
    score = int()
    health = 1000
    force = 100

    def __init__(self, impl):
        self.impl = impl

    def rotate(self, angle: int):
        self.impl.set_angle(angle * math.pi)

    def changeForce(self, delta):
        if self.force + delta >= MAX_FORCE:
            self.force = MAX_FORCE
        elif self.force + delta <= MIN_FORCE:
            self.force = MIN_FORCE
        else:
            self.force += delta
        print('force ', self.force)

    def chooseWeapon(self, newWeapon):
        self.currentWeapon = newWeapon

    def shoot(self):
        if self.weapons[self.currentWeapon] > 0:
            self.weapons[self.currentWeapon] -= 1
            distances = self.impl.shoot(self.currentWeapon, self.force)
            #iter = fighterIterator.Fighters().__iter__()
            #for x in iter:
                #if i == len(healthes):
                #    break
                #x.health = healthes[i]
                #i += 1
                #print(x.health)

    def isAlive(self):
        return self.health > 0

    def get_force(self):
        return self.force

    def change_force(self, delta):
        self.force = (self.force + 200 + delta) % 200
        print('force ', self.force)

    @abstractmethod
    def accept(self, visitor):
        pass
