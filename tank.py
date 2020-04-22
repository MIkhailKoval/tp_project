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
    def setAngle(self, angle):
        pass

    @abstractmethod
    def getForce(self) -> float:
        pass

    @abstractmethod
    def setHealth(self, percent):
        pass

    @abstractmethod
    def getHealth(self) -> float:
        pass

    @abstractmethod
    def setForce(self, percent):
        pass

    @abstractmethod
    def shoot(self, weapon):
        pass
