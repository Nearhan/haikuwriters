from unittest import TestCase
from haikuwriters.scoring.cond import IfCond, TrueCond, FalseCond, Not, Or, And, LessThan, GreaterThan
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
        self.assertEqual(1, self.alwaysOne.score(BlankText))


class TestNotOperation(TestCase):

    def setUp(self):
        self.notTrue = Not(TrueCond)

    def test_not_str(self):
        self.assertEqual("(not True)", str(self.notTrue))

    def test_not_repr(self):
        self.assertEqual("Not(TrueCond)", repr(self.notTrue))

    def test_not_cond(self):
        self.assertEqual(False, self.notTrue.cond(BlankText))


class TestOrOperation(TestCase):

    def setUp(self):
        self.trueOrFalse = Or(TrueCond, FalseCond)
        self.falseOrFalse = Or(FalseCond, FalseCond)

    def test_true_or_false_str(self):
        self.assertEqual("(True or False)", str(self.trueOrFalse))

    def test_true_or_false_repr(self):
        self.assertEqual("Or(TrueCond, FalseCond)", repr(self.trueOrFalse))

    def test_true_or_false_cond(self):
        self.assertIs(True, self.trueOrFalse.cond(BlankText))

    def test_false_or_false_cond(self):
        self.assertIs(False, self.falseOrFalse.cond(BlankText))


class TestAndOperation(TestCase):

    def setUp(self):
        self.trueAndTrue = And(TrueCond, TrueCond)
        self.trueAndFalse = And(TrueCond, FalseCond)

    def test_true_and_false_str(self):
        self.assertEqual("(True and False)", str(self.trueAndFalse))

    def test_true_and_false_repr(self):
        self.assertEqual("And(TrueCond, FalseCond)", repr(self.trueAndFalse))

    def test_true_and_false_cond(self):
        self.assertIs(False, self.trueAndFalse.cond(BlankText))

    def test_true_and_true_cond(self):
        self.assertIs(True, self.trueAndTrue.cond(BlankText))


class TestLessThanCond(TestCase):

    def setUp(self):
        self.zeroLessThanOne = LessThan(Score(0), Score(1))
        self.oneLessThanZero = LessThan(Score(1), Score(0))

    def test_zero_less_than_one_str(self):
        self.assertEqual("(0 < 1)", str(self.zeroLessThanOne))

    def test_zero_less_than_one_repr(self):
        self.assertEqual("LessThan(Score(0), Score(1))", repr(self.zeroLessThanOne))

    def test_zero_less_than_one_cond(self):
        self.assertIs(True, self.zeroLessThanOne.cond(BlankText))

    def test_one_less_than_zero_cond(self):
        self.assertIs(False, self.oneLessThanZero.cond(BlankText))


class TestGreaterThanCond(TestCase):
    def setUp(self):
        self.zeroGreaterThanOne = GreaterThan(Score(0), Score(1))
        self.oneGreaterThanZero = GreaterThan(Score(1), Score(0))

    def test_zero_less_than_one_str(self):
        self.assertEqual("(0 > 1)", str(self.zeroGreaterThanOne))

    def test_zero_less_than_one_repr(self):
        self.assertEqual("GreaterThan(Score(0), Score(1))", repr(self.zeroGreaterThanOne))

    def test_zero_less_than_one_cond(self):
        self.assertIs(False, self.zeroGreaterThanOne.cond(BlankText))

    def test_one_less_than_zero_cond(self):
        self.assertIs(True, self.oneGreaterThanZero.cond(BlankText))