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


class Visitor(ABC):
    @abstractmethod
    def movePlayer(self, player: 'Player'):
        pass

    @abstractmethod
    def moveBot(self):  # у функции планируется другая сигнатура (как у movePlayer)
        pass


class fightVisitor(Visitor):
    info = str()

    def __init__(self):
        pass

    def movePlayer(self, player: 'Player'):
        pygame.key.set_repeat(200, 1000 // gs.FPS)
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
                    player.rotate(
                        -1/180 - 4/180 * pressedCtrl)
                    print("RIGHT")
                if pressed_keys[control.posRotate]:
                    player.rotate(
                        +1/180 + 4/180 * pressedCtrl)
                    print("LEFT")
                if pressed_keys[control.boostForce]:
                    player.changeForce(1 + 4 * pressedCtrl)
                    print("UP")
                if pressed_keys[control.reduceForce]:
                    player.changeForce(-1 - 4 * pressedCtrl)
                    print("DOWN")
                if pressed_keys[control.chooseUsualBomb]:
                    player.chooseWeapon(weapon.usualBomb)
                    print("1")
                if pressed_keys[control.chooseBullet]:
                    player.chooseWeapon(weapon.bullet)
                    print("2")
                if pressed_keys[control.chooseKiloton]:
                    player.chooseWeapon(weapon.kiloton)
                    print("3")
                if pressed_keys[control.chooseAtomBomb]:
                    player.chooseWeapon(weapon.atomBomb)
                    print("4")
                if pressed_keys[control.chooseLaser]:
                    player.chooseWeapon(weapon.laser)
                    print("5", "no please")
                if pressed_keys[control.shoot]:
                    pygame.key.set_repeat(0, 0)
                    player.shoot()
                    print("ENTER")
                    return "Shoot"

    def moveBot(self):
        pass


class Player(Fighter):
    def accept(self, visitor: 'Visitor'):
        return visitor.movePlayer(self)
