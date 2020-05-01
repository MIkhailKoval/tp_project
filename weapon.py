from gamesettings import max_health


class Weapon:
    gravitation = True
    radius = 0


class Usual_bomb(Weapon):
    radius = 30
    damage = max_health


class Bullet(Weapon):
    radius = 1
    damage = int(0.25 * max_health)
    

class Kiloton(Weapon):
    radius = 70
    damage = max_health


class Atom_bomb(Weapon):
    radius = 120
    damage = max_health


class Laser(Weapon):
    damage = int()
    gravitation = False


usual_bomb = Usual_bomb()
bullet = Bullet()
kiloton = Kiloton()
atom_bomb = Atom_bomb()
laser = Laser()
