from haikuwriters.scoring.tree import BaseTree, ScoreTree


class Cond(BaseTree):
    def apply(self, *conditions):
        return NotImplemented


class TrueCond(Cond):
    def __init__(self):
        super().__init__(True)

    def apply(self, *conditions:Cond):
        return True

    def __str__(self):
        return str(True)

    def __repr__(self):
        return type(self).__name__
TrueCond = TrueCond()


class FalseCond(Cond):
    def __init__(self):
        super().__init__(False)

    def apply(self, *conditions:Cond):
        return False

    def __str__(self):
        return str(False)

    def __repr__(self):
        return type(self).__name__
FalseCond = FalseCond()


class Comparator(BaseTree):
    def compare(self, *other:Cond):
        return NotImplemented


class IfCond(ScoreTree):
    def __init__(self, condition:Cond, then:ScoreTree, otherwise:ScoreTree):
        self.condition = condition
        self.then = then
        self.otherwise = otherwise
        super().__init__(condition, then, otherwise)

    def __str__(self):
        return "if {cond} then {true} else {false}".format(
            cond=str(self.condition),
            true=str(self.then),
            false=str(self.otherwise),
        )
