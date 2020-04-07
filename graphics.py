import player
import weapon


class Weapon(weapon.Weapon):
    pass


class Tank(player.Player):
    def rotateMuzzle(self, angle):
        pass

    def shoot(self):
        pass


class Info:
    '''класс для отображения на экране разной инфы по типу того, чей ход, какой ветер'''
    pass
