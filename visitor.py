from abc import ABC, abstractmethod
import control
from fighter import Fighter
import gamesettings as gs
from pygame.constants import (
    QUIT, KEYDOWN
)
import pygame
import sys
import weapon
import graphics


class Visitor(ABC):
    @abstractmethod
    def move_player(self, player: 'Player'):
        pass

    @abstractmethod
    def move_bot(self):
        # у функции планируется другая сигнатура (как у movePlayer)
        pass


class Fight_visitor(Visitor):
    info = str()

    def __init__(self):
        pass

    def move_player(self, game, player: 'Player'):
        if not player.is_alive():
            return
        # здесь надо, чтобы отсеялись лишние
        pygame.key.set_repeat(200, 1000 // gs.FPS)
        player.impl.draw_tank(graphics.PINK)
        graphics.show_force(player)
        graphics.show_angle(player.impl)
        graphics.show_type_of_weapon(player)
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
                sys.exit()
            elif event.type == KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                pressed_mod_keys = pygame.key.get_mods()
                pressed_ctrl = bool(
                    pressed_mod_keys & control.boost_move)
                if pressed_ctrl:
                    pass
                    #print("Ctrl")
                if pressed_keys[pygame.K_ESCAPE]:
                    return "Menu"
                if pressed_keys[control.neg_rotate]:
                    #print("RIGHT")
                    player.rotate(
                        -1/180 - gs.CTRL_BOOSTING/180 * pressed_ctrl)
                if pressed_keys[control.pos_rotate]:
                    #print("LEFT")
                    player.rotate(
                        +1/180 + gs.CTRL_BOOSTING/180 * pressed_ctrl)
                if pressed_keys[control.boost_force]:
                    #print("UP")
                    player.change_force(1 + gs.CTRL_BOOSTING * pressed_ctrl)
                    graphics.show_force(player)
                if pressed_keys[control.reduce_force]:
                    #print("DOWN")
                    player.change_force(-1 - gs.CTRL_BOOSTING * pressed_ctrl)
                    graphics.show_force(player)
                if pressed_keys[control.choose_usual_bomb]:
                    #print("1")
                    player.choose_weapon(weapon.usual_bomb)
                    graphics.show_type_of_weapon(player)
                if pressed_keys[control.choose_bullet]:
                    #print("2")
                    player.choose_weapon(weapon.bullet)
                    graphics.show_type_of_weapon(player)
                if pressed_keys[control.choose_kiloton]:
                    #print("3")
                    player.choose_weapon(weapon.kiloton)
                    graphics.show_type_of_weapon(player)
                if pressed_keys[control.choose_atom_bomb]:
                    #print("4")
                    player.choose_weapon(weapon.atom_bomb)
                    graphics.show_type_of_weapon(player)
                '''if pressed_keys[control.choose_laser]:
                    player.chooseWeapon(weapon.laser)
                    print("5", "no please")'''
                if pressed_keys[control.shoot]:
                    pygame.key.set_repeat(0, 0)
                    #print("ENTER")
                    if player.shoot(game):
                        return "Shoot"
                    else:
                        pygame.key.set_repeat(200, 1000 // gs.FPS)

    def move_bot(self):
        pass


class Player(Fighter):
    def accept(self, game, visitor: 'Visitor'):
        return visitor.move_player(game, self)
