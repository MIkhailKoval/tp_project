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
    def setHealth(self, percent):
        pass

    @abstractmethod
    def getHealth(self) -> float:
        pass

    @abstractmethod
    def shoot(self, weapon, force):
        pass
