from haikuwriters.scoring.tree import ScoreTree, MetricData, BaseTree


### Operators ###

class Operator:
    def apply(self, data:MetricData, *operands:BaseTree):
        return NotImplemented

    def _wrap_str(self, *operands:ScoreTree):
        return NotImplemented


class BaseOperator(Operator):
    symbol = NotImplemented

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol


class UnaryOperator(BaseOperator):
    # noinspection PyMethodOverriding
    def apply(self, data:MetricData, operand:BaseTree):
        return NotImplemented

    def _wrap_str(self, operand:BaseTree):
        return str(self) + " " + str(operand)


class InfixOperator(BaseOperator):
    def _wrap_str(self, *children:BaseTree):
        return (" " + str(self) + " ").join(map(str, children))


class AddOperator(InfixOperator):
    symbol = "+"
    def apply(self, data:MetricData, *operands:BaseTree):
        total = 0
        for op in operands:
            total += op.score(data)
        return total
AddOperator = AddOperator()


class MultiplyOperator(InfixOperator):
    symbol = "*"
    def apply(self, data:MetricData, *operands:BaseTree):
        product = 1
        for op in operands:
            product *= op.score(data)
        return product
MultiplyOperator = MultiplyOperator()


### Operations ###

class BaseOperation(BaseTree):
    operator = None

    def __init__(self, *children:BaseTree):
        super().__init__(self.operator, *children)

    def __str__(self):
        return "(" + self.operator._wrap_str(*self) + ")"

    def __repr__(self):
        return type(self).__name__ + "(" + ", ".join(map(repr, self)) + ")"


class ScoreOperation(BaseOperation, ScoreTree):
    """
    An Operation that is also a ScoreTree.
    """

    def score(self, data:MetricData):
        assert isinstance(self.operator, Operator), "self.operator must be an Operator"
        return self.operator.apply(data, *self.children)


class Add(ScoreOperation):
    operator = AddOperator


class Multiply(ScoreOperation):
    operator = MultiplyOperator
