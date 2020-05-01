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


def isEqual(a, b):
    return abs(a - b) < DELTA


class Test_weapon(unittest.TestCase):
    def setUp(self):
        # pylint: disable=no-member
        pygame.init()
        # pylint: disable=no-member
        graphics.init_window()
        gs.number_of_fighters = 2
        self.objects = []
        game = state.Game()
        self.context = state.Context(game)
        self.game = game
        pygame.display.update()

    def tearDown(self):
        # pylint: disable=no-member
        pygame.quit()
        # pylint: disable=no-member

    def test_usual_bomb(self):
        self.game.fighters[0].rotate(-45/180)
        self.game.fighters[0].change_force(100)
        self.game.fighters[0].shoot(self.game)
        self.assertTrue(self.game.fighters[1].health == 66)

    def test_bullet(self):
        self.game.fighters[0].rotate(-45/180)
        self.game.fighters[0].change_force(100)
        self.game.fighters[0].choose_weapon(weapon.bullet)
        self.game.fighters[0].shoot(self.game)
        self.assertTrue(self.game.fighters[1].health == 100)

    def test_kilotone(self):
        self.game.fighters[0].rotate(-25/180)
        self.game.fighters[0].change_force(100)
        self.game.fighters[0].choose_weapon(weapon.kiloton)
        self.game.fighters[0].shoot(self.game)
        self.assertTrue(self.game.fighters[1].health == 100)

    def test_atom_bomb(self):
        self.game.fighters[0].rotate(-25/180)
        self.game.fighters[0].change_force(100)
        self.game.fighters[0].choose_weapon(weapon.atom_bomb)
        self.game.fighters[0].shoot(self.game)
        self.assertTrue(self.game.fighters[1].health <= 0)


if __name__ == '__main__':
    unittest.main()
