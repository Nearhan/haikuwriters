from unittest import TestCase
from haikuwriters.scoring.cond import IfCond, TrueCond, FalseCond, NotCond
from haikuwriters.scoring.tree import Score, BlankText


class TestIfCond(TestCase):

    def setUp(self):
        self.alwaysOne = IfCond(TrueCond, Score(1), Score(0))
        self.notTrue = NotCond(TrueCond)

    def test_true_str(self):
        self.assertEqual("True", str(TrueCond))

    def test_false_str(self):
        self.assertEqual("False", str(FalseCond))

    def test_if_str(self):
        self.assertEqual("if True then 1 else 0", str(self.alwaysOne))

    def test_if_repr(self):
        self.assertEqual("IfCond(TrueCond, Score(1), Score(0))", repr(self.alwaysOne))

    def test_if_score(self):
        self.assertEqual(1, self.alwaysOne.score(BlankText))

    def test_not_str(self):
        self.assertEqual("not True", str(self.notTrue))

    def test_not_repr(self):
        self.assertEqual("NotCond(TrueCond)", repr(self.notTrue))

    def test_not_score(self):
        self.assertEqual(False, self.notTrue.cond(BlankText))
