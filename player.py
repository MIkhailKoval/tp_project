import weapon


class Player:
    angle = 0
    force = 1000
    health = 100

    # какие есть ещё варианты, как это хранить, кроме как строкой?
    currentTypeOfWeapon = "usualBomb"
    '''Кажется, это оптимальный вариант. Можно конечно хранить числом и хранить словарь,
    который переводит число в строку, если так удобнее будет'''
    '''Так вариант со словарём ничем не лучше такого, т.к. строками писать и читать проще и понятнее
    и смысл это делать в числах, если всё равно будет делаться перевод в строку'''
