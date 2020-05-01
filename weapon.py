from gamesettings import maxHealth


class Weapon:
    gravitation = True
    radius = 0


class UsualBomb(Weapon):
    radius = 30
    damage = maxHealth


class Bullet(Weapon):
    radius = 1
    damage = int(0.25 * maxHealth)
    

class Kiloton(Weapon):
    radius = 70
    damage = maxHealth


class AtomBomb(Weapon):
    radius = 120
    damage = maxHealth


class Laser(Weapon):
    damage = int()
    gravitation = False


usualBomb = UsualBomb()
bullet = Bullet()
kiloton = Kiloton()
atomBomb = AtomBomb()
laser = Laser()
