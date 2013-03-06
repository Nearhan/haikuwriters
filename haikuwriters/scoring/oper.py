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


class Add(InfixOperation, ScoreTree):
    symbol = "+"

    def score(self, data:MetricData):
        total = 0
        for child in self.children:
            total += child.score(data)
        return total

class Multiply(InfixOperation, ScoreTree):
    symbol = "*"

    def score(self, data:MetricData):
        product = 1
        for child in self.children:
            product *= child.score(data)
        return product

