from unittest import TestCase
from haikuwriters.scoring.cond import IfCond, TrueCond, FalseCond
from haikuwriters.scoring.tree import Score, BlankText


class TestIfCond(TestCase):

    def setUp(self):
        self.alwaysOne = IfCond(TrueCond, Score(1), Score(0))

    def test_true_str(self):
        self.assertEqual("True", str(TrueCond))

    def test_false_str(self):
        self.assertEqual("False", str(FalseCond))

    def test_if_str(self):
        self.assertEqual("if True then 1 else 0", str(self.alwaysOne))

    def test_if_repr(self):
        self.assertEqual("IfCond(TrueCond, Score(1), Score(0))", repr(self.alwaysOne))

    def test_if_score(self):
        self.assertEqual(self.alwaysOne.score(BlankText), 1)
