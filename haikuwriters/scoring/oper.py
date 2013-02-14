from haikuwriters.scoring.tree import ScoreTree, ScoreTerm


### Operators ###

class Operator:
    def apply(self, *operands:ScoreTree):
        return NotImplemented

    def _wrap_str(self, *operands:ScoreTree):
        return NotImplemented

    def __str__(self):
        return ""


NoOp = Operator()


class InfixOperator(Operator):
    def __init__(self, symbol:str, apply:callable):
        self.symbol = symbol
        self.apply = apply

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

    def _wrap_str(self, left:ScoreTree, right:ScoreTree):
        return str(left) + " " + str(self) + " " + str(right)


class ChooseOperator(Operator):
    def _wrap_str(self, *operands:ScoreTerm):
        terms = [str(op.node) + " {" + str(int(op.meta * 100)) + "%}" for op in operands]
        return " | ".join(terms)

    def __str__(self):
        return "|%"

    def __repr__(self):
        return "|%"

ChooseOperator = ChooseOperator()


### Operations ###

class Operation:
    operator = NoOp


class Combinator(ScoreTree):

    def __init__(self, *children:ScoreTree):
        super().__init__(self.operator, *children)

    def __str__(self):
        return "(" + self.operator._wrap_str(*self.children) + ")"

    def __repr__(self):
        return type(self).__name__ + "(" + ", ".join(map(repr, self.children)) + ")"

    @property
    def score(self):
        return self.operator.apply(*[child.score for child in self.children])


class BinaryOperation(Combinator):
    def __init__(self, left:ScoreTree, right:ScoreTree):
        self.left = left
        self.right = right
        super().__init__(left, right)


class Add(BinaryOperation):
    operator = InfixOperator("+", lambda x, y: x + y)


class Multiply(BinaryOperation):
    operator = InfixOperator("*", lambda x, y: x * y)


class Choose(Combinator):
    operator = ChooseOperator

