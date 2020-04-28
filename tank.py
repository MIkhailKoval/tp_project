from abc import ABC, abstractmethod
import weapon


class Tank(ABC):
    angle = float()
    force = float()
    health = 1000

    @abstractmethod
    def get_angle(self) -> float:
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
