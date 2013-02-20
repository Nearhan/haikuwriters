from unittest import TestCase
from haikuwriters.scoring.cond import IfCond, TrueCond, FalseCond
from haikuwriters.scoring.tree import Score


class TestIfCond(TestCase):

    def test_str_true(self):
        self.assertEqual("True", str(TrueCond))

    def test_str_false(self):
        self.assertEqual("False", str(FalseCond))

    def test_str_if(self):
        self.assertEqual("if True then 1 else 0", str(IfCond(TrueCond, Score(1), Score(0))))