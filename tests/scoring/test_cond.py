from unittest import TestCase
from haikuwriters.scoring.cond import IfCond, TrueCond, FalseCond
from haikuwriters.scoring.tree import Score


class TestIfCond(TestCase):

    def test_true_str(self):
        self.assertEqual("True", str(TrueCond))

    def test_false_str(self):
        self.assertEqual("False", str(FalseCond))

    def test_if_str(self):
        self.assertEqual("if True then 1 else 0", str(IfCond(TrueCond, Score(1), Score(0))))

    def test_if_repr(self):
        self.assertEqual("IfCond(TrueCond, Score(1), Score(0))", repr(IfCond(TrueCond, Score(1), Score(0))))
