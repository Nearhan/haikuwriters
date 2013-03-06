from haikuwriters.scoring.oper import InfixOperation, BaseOperation
from haikuwriters.scoring.tree import ScoreTree, MetricData


class ScoreOperation(BaseOperation, ScoreTree):
    """
    The base class for all operations that are ScoreTrees of ScoreTrees
    """
    def __init__(self, *children:ScoreTree):
        super().__init__(*children)


class Add(ScoreOperation, InfixOperation):
    symbol = "+"

    def score(self, data:MetricData):
        total = 0
        for child in self.children:
            total += child.score(data)
        return total


class Multiply(ScoreOperation, InfixOperation):
    symbol = "*"

    def score(self, data:MetricData):
        product = 1
        for child in self.children:
            product *= child.score(data)
        return product
