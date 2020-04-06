import gamesettings


import random


# честно, не очень понимаю, что именно этот класс будет делать
class map:
    def __init__(self):
        reflection = random.randint(0, gamesettings.existsReflection)
        wind = random.randint(0, gamesettings.maxWind)
        # как-то выбирается или генерится рельеф
