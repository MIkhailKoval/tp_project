#from __future__ import annotations
from fighter import Fighter
from collections.abc import Iterable, Iterator
from typing import List


class FighterIterator(Iterator):
    def __init__(self, fighters: 'Fighters'):
        self._all = fighters
        self._pos = 0

    def __next__(self) -> Fighter:
        current = self._pos
        self._pos += 1
        while not self._all[self._pos % len(self._all)].isAlive():
            self._pos += 1
            if self._pos - current >= len(self._all):
                raise StopIteration()
        current = self._pos
        return self._all[self._pos % len(self._all)]


class Fighters(Iterable):
    def __init__(self, fighters: List[Fighter] = []):
        self._all = fighters

    def __iter__(self) -> FighterIterator:
        return FighterIterator(self._all)

    def add(self, fighter: Fighter):
        self._all.append(fighter)
