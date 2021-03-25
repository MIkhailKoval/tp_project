from abc import ABC, abstractmethod
import weapon
import math


class Tank(ABC):
    angle = math.pi / 2
    force = float()
    health = 100

    @abstractmethod
    def get_angle(self) -> float:
        pass

    @abstractmethod
    def set_angle(self, angle):
        pass

    @abstractmethod
    def shoot(self, game, weapon, force):
        pass
