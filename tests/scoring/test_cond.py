from unittest import TestCase
from haikuwriters.scoring.cond import IfCond, TrueCond, Cond
from haikuwriters.scoring.tree import Score


class TestIfCond(TestCase):

    def test_str_if(self):
        self.assertEqual("if (True) then Score(1) else Score(0)", str(IfCond(TrueCond, Score(1), Score(0))))