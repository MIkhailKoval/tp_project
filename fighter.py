from abc import ABC, abstractmethod
from collections import OrderedDict
import math
import weapon
MAX_FORCE = 200
MIN_FORCE = 10


class Fighter(ABC):
    weapons = {weapon.usual_bomb: 100, weapon.bullet: 9999,
               weapon.kiloton: 3, weapon.atom_bomb: 1, weapon.laser: 0}
    current_weapon = weapon.usual_bomb
    score = int()
    health = 100
    force = 100

    def __init__(self, impl):
        self.impl = impl

    def rotate(self, angle: int):
        self.impl.set_angle(angle * math.pi)

    def change_force(self, delta):
        self.force = max(MIN_FORCE, min(MAX_FORCE, self.force + delta))
        print('force ', self.force)

    def choose_weapon(self, new_weapon):
        self.current_weapon = new_weapon

    def shoot(self, game):
        if self.weapons[self.current_weapon] > 0:
            self.weapons[self.current_weapon] -= 1
            distances = self.impl.shoot(game, self.current_weapon, self.force)
            handle_explosion(game, distances,
                             self.current_weapon.radius, self.current_weapon.damage)
            return True
        else:
            return False

    def reduce_health(self, delta, game):
        if self.health > 0:
            self.health -= delta
            if self.health <= 0:
                distances = self.impl.detonate(game.fighters)
                game.alive_tanks -= 1
                handle_explosion(
                    game, distances, weapon.usual_bomb.radius, weapon.usual_bomb.damage)

    def is_alive(self):
        return self.health > 0

    def get_force(self):
        return self.force

    @abstractmethod
    def accept(self, visitor):
        pass


def handle_explosion(game, distances, radius, damage):
    for i in range(len(distances)):
        if radius >= distances[i]:
            game.fighters[i].reduce_health(damage, game)
