from abc import ABC, abstractmethod


class Fighter(ABC):
    currentWeapon = str()
    score = int()
    health = float()
    force = 100

    def __init__(self, impl):
        self.impl = impl

    def rotate(self, angle: int):
        currentAngle = self.impl.getAngle()
        self.impl.set_angle(currentAngle + angle)

    def changeForce(self, delta ):
        self.force = (self.force + 200 + delta ) % 200
        print('force ', self.force )
        
    def shoot(self):
        self.impl.shoot(self.currentWeapon, self.force)

    def isAlive(self):
        return self.health > 0

    @abstractmethod
    def accept(self, visitor):
        pass
