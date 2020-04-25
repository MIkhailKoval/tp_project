#from __future__ import annotations
from abc import ABC, abstractmethod
import control
import gamesettings as gs
from fighter import Fighter
import sys
from pygame.constants import (
    QUIT, KEYDOWN
)
import pygame


class Visitor(ABC):
    @abstractmethod
    def movePlayer(self, player: 'Player'):
        pass

    @abstractmethod
    def moveBot(self):  # у функции планируется другая сигнатура (как у movePlayer)
        pass


class fightVisitor(Visitor):
    def __init__(self):
        pass

    def movePlayer(self, player: 'Player'):
        pygame.key.set_repeat(100, 1000 // gs.FPS)
        while True:
            event = pygame.event.poll()
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
                if pressed_keys[control.posRotate]:
                    player.rotate(
                        1 + 4 * pressedCtrl)
                    print("RIGHT")
                if pressed_keys[control.negRotate]:
                    player.rotate(
                        -1 - 4 * pressedCtrl)
                    print("LEFT")
                if pressed_keys[control.boostForce]:
                    player.changeForce(1 + 4 * pressedCtrl)
                    print("UP")
                if pressed_keys[control.reduceForce]:
                    player.changeForce(-1 - 4 * pressedCtrl)
                    print("DOWN")
                if pressed_keys[control.shoot]:
                    pygame.key.set_repeat(0, 0)
                    player.shoot()
                    print("ENTER")
                    return

    def moveBot(self):
        pass


class Player(Fighter):
    def accept(self, visitor: 'Visitor'):
        visitor.movePlayer(self)
