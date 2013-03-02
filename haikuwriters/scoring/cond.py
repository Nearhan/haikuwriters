from haikuwriters.scoring.tree import BaseTree, ScoreTree, MetricData


class CondTree(BaseTree):
    def cond(self, data:MetricData):
        return NotImplemented


class TrueCond(CondTree):
    def __init__(self):
        super().__init__(True)

    def cond(self, data:MetricData):
        return True

    def __str__(self):
        return str(True)

    def __repr__(self):
        return type(self).__name__
TrueCond = TrueCond()


class FalseCond(CondTree):
    def __init__(self):
        super().__init__(False)

    def cond(self, data:MetricData):
        return False

    def __str__(self):
        return str(False)

    def __repr__(self):
        return type(self).__name__
FalseCond = FalseCond()


class NotCond(CondTree):
    def __init__(self, condition:CondTree):
        self.condition = condition
        super().__init__(condition)

    def __str__(self):
        return "not " + str(self.condition)

    def cond(self, data:MetricData):
        return not super().cond(data)


class IfCond(ScoreTree):
    def __init__(self, condition:CondTree, then:ScoreTree, otherwise:ScoreTree):
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

    def score(self, data:MetricData):
        if self.condition.cond(data) is True:
            return self.then.score(data)
        else:
            return self.otherwise.score(data)