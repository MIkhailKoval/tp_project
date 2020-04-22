import fighter
from visitor import Visitor


class Player(fighter.fighter):
    def accept(self, visitor: Visitor):
        visitor.movePlayer(self)
