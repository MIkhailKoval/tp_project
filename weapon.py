class weapon:
    gravitation = True
    pass


# численные значения условны, просто обозначены поля
# в питоне можно объявить переменную, но ничем пока не инициализировать?
'''можно'''
class usualBomb(weapon):
    radius = 10
    '''radius = int()'''
    damage = 50


class laser(weapon):
    damage = 1000
    gravitation = False
