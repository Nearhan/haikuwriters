from haikuwriters.scoring.oper import InfixOperation
from haikuwriters.scoring.tree import ScoreTree, MetricData


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
