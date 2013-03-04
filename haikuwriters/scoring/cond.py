from haikuwriters.scoring.oper import UnaryOperator, BaseOperation, Operator
from haikuwriters.scoring.tree import BaseTree, ScoreTree, MetricData


class CondTree(BaseTree):
    def cond(self, data:MetricData):
        return NotImplemented


class CondOperation(BaseOperation, CondTree):
    """
    An Operation that is also a CondTree
    """
    def cond(self, data:MetricData):
        assert isinstance(self.operator, Operator), "self.operator must be an Operator"
        return self.operator.apply(data, self.children)


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


class NotOperator(UnaryOperator):
    symbol = "not"
    conjunction = "or"

    def apply(self, data:MetricData, operands:list):
        return False
        # return not operand or other operands
NotOperator = NotOperator()


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

    def cond(self, data:MetricData):
        return self.condition.cond(data)


class Not(CondOperation):
    operator = NotOperator

    # TODO: Move this to _wrap_str?
    def __str__(self):
        return "not " + " or ".join(map(str, self))
