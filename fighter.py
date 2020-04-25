from abc import ABC, abstractmethod
import math

class Fighter(ABC):
    currentWeapon = str()
    score = int()
    health = 1
    force = 100

    def __init__(self, impl):
        self.impl = impl

    def rotate(self, angle: int):
        self.impl.set_angle(angle * math.pi)

    def changeForce(self, delta):
        self.force = (self.force + 200 + delta) % 200
        print('force ', self.force)
        
    def shoot(self):
        self.impl.shoot(self.currentWeapon, self.force)

    def isAlive(self):
        return self.health > 0
    
    def get_force(self):
        return self.force
    
    def change_force(self, delta ):
        self.force = (self.force + 200 + delta ) % 200
        print('force ', self.force )

    @abstractmethod
    def accept(self, visitor):
        pass
