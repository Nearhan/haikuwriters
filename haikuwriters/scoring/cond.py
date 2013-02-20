from haikuwriters.scoring.tree import BaseTree, ScoreTree


class Cond:
    def apply(self, *conditions):
        return NotImplemented


class TrueCond(Cond):
    def apply(self, *conditions:Cond):
        return True
TrueCond = TrueCond()


class FalseCond(Cond):
    def apply(self, *conditions:Cond):
        return False
FalseCond = FalseCond()


class Comparator(BaseTree):
    def compare(self, *other:Cond):
        pass


class IfCond(Cond):
    def __init__(self, condition:Cond, then:ScoreTree, otherwise:ScoreTree):
        self.condition = condition
        self.then = then
        self.otherwise = otherwise
