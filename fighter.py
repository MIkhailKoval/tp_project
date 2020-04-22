from abc import ABC, abstractmethod


class Fighter(ABC):
    currentWeapon = str()
    score = int()
    health = float()

    def __init__(self, impl):
        self.impl = impl

    def rotate(self, angle: int):
        currentAngle = self.impl.getAngle()
        self.impl.setAngle(currentAngle + angle)

    def changeForce(self, percent: float):
        currentForce = self.impl.getForce()
        self.impl.setForce(min(max(0, currentForce + percent), 1))

    def shoot(self):
        self.impl.shoot(self.currentWeapon)

    def isAlive(self):
        return self.health > 0

    @abstractmethod
    def accept(self, visitor):
        pass
