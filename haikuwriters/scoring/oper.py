import random
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

    def apply(self, *operands:ScoreTerm):
        # Roulette algorithm:
        # 1. Normalize all options to a wheel between [0, 1)
        #    using the sum of all operand probabilities as a normalizing factor
        normalizer = sum(op.meta for op in operands)
        # 2. Roll the wheel [0, 1)
        landing = random.random()
        # 3. Subtract the size of each slot on the wheel,
        #    determined by the probability of that option
        #    to the total of all operands' probabilities
        selection = None
        for op in operands:
            # The relative probability of choosing the given operand
            slot = op.meta / normalizer
            if landing - slot < 0:
                # The ball has landed in the slot of the given operand
                selection = op
                break
            else:
                # The ball keeps rolling
                landing -= slot
        # 4. Return the selected operation's score
        return selection.score()

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
    def _score(self):
        return self.operator.apply(*self.children)


class BinaryOperation(Combinator):
    def __init__(self, left:ScoreTree, right:ScoreTree):
        self.left = left
        self.right = right
        super().__init__(left, right)


class Add(BinaryOperation):
    operator = InfixOperator("+", lambda x, y: x.score() + y.score())


class Multiply(BinaryOperation):
    operator = InfixOperator("*", lambda x, y: x.score() * y.score())


class Choose(Combinator):
    operator = ChooseOperator

