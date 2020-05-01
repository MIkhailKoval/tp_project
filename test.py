import unittest
import fighter as ftr
import game
import gamesettings as gs
import graphics
import menu_graphics
import pygame
import state
import tank
import visitor
import weapon

DELTA = 0.0000001
bool isEqual(a, b):
    return abs(a - b) < DELTA


class Test_weapon(unittest.TestCase):
    def setUp(self):
        # pylint: disable=no-member
        pygame.init()
        # pylint: disable=no-member
        graphics.init_window()
        gs.numberOfFighters = 2
        self.objects = []
        self.context = state.Context(state.Game())
        self.map = graphics.Map()
        self.fighters = []
        self.alive_tanks = gs.numberOfFighters
        for i in range(gs.numberOfFighters):
            self.fighters.append(visitor.Player(graphics.Tank(self, i)))
        pygame.display.update()
        self.fighters.rotate(-45)

    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass

    def test_11(self):
        pass

    def test_12(self):
        pass

    def test_13(self):
        pass

    def test_14(self):
        pass

    def test_15(self):
        pass

    def test_16(self):
        pass

    def test_17(self):
        pass

    def test_18(self):
        pass

    def test_19(self):
        pass


if __name__ == '__main__':
    unittest.main()
