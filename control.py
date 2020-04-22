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
# pylint: enable=no-member
