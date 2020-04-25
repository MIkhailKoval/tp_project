import weapon
from abc import ABC, abstractmethod


class Tank(ABC):
    angle = float()
    force = float()
    health = float()

    @abstractmethod
    def getAngle(self) -> float:
        pass

    @abstractmethod
    def set_angle(self, angle):
        pass

    @abstractmethod
    def set_health(self, percent):
        pass

    @abstractmethod
    def get_health(self) -> float:
        pass

    @abstractmethod
    def shoot(self, weapon, force):
        pass

