import weapon
from abc import ABC, abstractmethod


class Player(ABC):
    angle = 0
    force = 1000
    health = 100
    currentWeapon = "usualBomb"

    @abstractmethod
    def rotateMuzzle(self, angle):
        pass

    @abstractmethod
    def changeForce(self, value):
        pass

    @abstractmethod
    def shoot(self):
        pass
