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
    def movePlayer(self, player: 'Player'):
        pass

    @abstractmethod
    def moveBot(self):
        # у функции планируется другая сигнатура (как у movePlayer)
        pass


class fightVisitor(Visitor):
    info = str()

    def __init__(self):
        pass

    def movePlayer(self, game, player: 'Player'):
        if not player.isAlive():
            return
        pygame.key.set_repeat(200, 1000 // gs.FPS)
        # здесь надо, чтобы отсеялись лишние
        player.impl.draw_tank(graphics.PINK)
        graphics.show_force(player)
        print('HERE')
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
                pressedCtrl = bool(
                    pressed_mod_keys & control.boostMove)
                if pressedCtrl:
                    print("Ctrl")
                if pressed_keys[pygame.K_ESCAPE]:
                    return "Menu"
                if pressed_keys[control.negRotate]:
                    print("RIGHT")
                    player.rotate(
                        -1/180 - 4/180 * pressedCtrl)
                    # graphics.show_force(player)
                if pressed_keys[control.posRotate]:
                    print("LEFT")
                    player.rotate(
                        +1/180 + 4/180 * pressedCtrl)
                    # graphics.show_force(player)
                if pressed_keys[control.boostForce]:
                    print("UP")
                    player.changeForce(1 + 4 * pressedCtrl)
                    graphics.show_force(player)
                if pressed_keys[control.reduceForce]:
                    print("DOWN")
                    player.changeForce(-1 - 4 * pressedCtrl)
                    graphics.show_force(player)
                if pressed_keys[control.chooseUsualBomb]:
                    print("1")
                    player.chooseWeapon(weapon.usualBomb)
                if pressed_keys[control.chooseBullet]:
                    print("2")
                    player.chooseWeapon(weapon.bullet)
                if pressed_keys[control.chooseKiloton]:
                    print("3")
                    player.chooseWeapon(weapon.kiloton)
                if pressed_keys[control.chooseAtomBomb]:
                    print("4")
                    player.chooseWeapon(weapon.atomBomb)
                if pressed_keys[control.chooseLaser]:
                    player.chooseWeapon(weapon.laser)
                    print("5", "no please")
                if pressed_keys[control.shoot]:
                    pygame.key.set_repeat(0, 0)
                    print("ENTER")
                    graphics.updateTanks(game.fighters)
                    player.shoot(game)
                    return "Shoot"

    def moveBot(self):
        pass


class Player(Fighter):
    def accept(self, game, visitor: 'Visitor'):
        return visitor.movePlayer(game, self)
