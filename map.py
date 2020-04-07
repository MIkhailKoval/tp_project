import gamesettings


import random


# честно, не очень понимаю, что именно этот класс будет делать
class map:
    def __init__(self):
        self.reflection = random.randint(0, gamesettings.existsReflection)
        self.wind = random.randint(0, gamesettings.maxWind)
        # как-то выбирается или генерится рельеф
