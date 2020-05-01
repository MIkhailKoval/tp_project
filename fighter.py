from abc import ABC, abstractmethod
from collections import OrderedDict
import math
import weapon

MAX_FORCE = 200
MIN_FORCE = 1


class Fighter(ABC):
    weapons = {weapon.usualBomb: 100, weapon.bullet: 9999,
               weapon.kiloton: 3, weapon.atomBomb: 1, weapon.laser: 0}
    currentWeapon = weapon.usualBomb
    score = int()
    health = 100
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

    def shoot(self, game):
        if self.weapons[self.currentWeapon] > 0:
            self.weapons[self.currentWeapon] -= 1
            distances = self.impl.shoot(game, self.currentWeapon, self.force)
            handle_explosion(game.fighters, distances,
                             self.currentWeapon.radius, self.currentWeapon.damage, game.alive_tanks)

    def reduceHealth(self, delta, fighters, alive_tanks):
        if self.health > 0:
            self.health -= delta
            if self.health <= 0:
                distances = self.impl.detonate(fighters)
                alive_tanks -= 1
                handle_explosion(
                    fighters, distances, weapon.usualBomb.radius, weapon.usualBomb.damage, alive_tanks)

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


def handle_explosion(fighters, distances, radius, damage, alive_tanks):
    for i in range(len(distances)):
        print(i, radius, distances[i])
        if radius >= distances[i]:
            fighters[i].reduceHealth(damage, fighters, alive_tanks)
