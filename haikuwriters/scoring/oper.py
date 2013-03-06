from haikuwriters.scoring.tree import ScoreTree, MetricData, BaseTree, Unary


class BaseOperation(BaseTree):
    symbol = NotImplemented

    def __init__(self, *children:BaseTree):
        super().__init__(self.symbol, *children)

    def __str__(self):
        return type(self).__name__ + "(" + ", ".join(map(str, self)) + ")"

    def __repr__(self):
        return type(self).__name__ + "(" + ", ".join(map(repr, self)) + ")"


class InfixOperation(BaseOperation):
    def __str__(self):
        return "(" + (" " + self.symbol + " ").join(map(str, self)) + ")"


class UnaryOperation(Unary, BaseOperation):
    def __str__(self):
        return "(" + self.symbol + " " + str(self.child) + ")"
