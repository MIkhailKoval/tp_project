# клавиши управления
import pygame


# также, возможно, стоит сделать абстрактный класс и от него наследовать разные варианты
# pylint: disable=no-member
negRotate = pygame.K_RIGHT  # по часовой
posRotate = pygame.K_LEFT  # против часовой
boostForce = pygame.K_UP
reduceForce = pygame.K_DOWN
shoot = pygame.K_RETURN
boostMove = pygame.KMOD_CTRL
chooseUsualBomb = pygame.K_1
chooseBullet = pygame.K_2
chooseKiloton = pygame.K_3
chooseAtomBomb = pygame.K_4
#chooseLaser = pygame.K_5

# pylint: enable=no-member
