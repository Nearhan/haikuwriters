from unittest import TestCase
from haikuwriters.scoring.cond import IfCond, TrueCond, FalseCond, Not, Or, And
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

    def test_trueorfalse_str(self):
        self.assertEqual("(True or False)", str(self.trueOrFalse))

    def test_trueorfalse_repr(self):
        self.assertEqual("Or(TrueCond, FalseCond)", repr(self.trueOrFalse))

    def test_trueorfalse_cond(self):
        self.assertIs(True, self.trueOrFalse.cond(BlankText))

    def test_falseorfalse_cond(self):
        self.assertIs(False, self.falseOrFalse.cond(BlankText))


class TestAndOperation(TestCase):

    def setUp(self):
        self.trueAndTrue = And(TrueCond, TrueCond)
        self.trueAndFalse = And(TrueCond, FalseCond)

    def test_trueandfalse_str(self):
        self.assertEqual("(True and False)", str(self.trueAndFalse))

    def test_trueandfalse_repr(self):
        self.assertEqual("And(TrueCond, FalseCond)", repr(self.trueAndFalse))

    def test_trueandfalse_cond(self):
        self.assertIs(False, self.trueAndFalse.cond(BlankText))

    def test_trueandtrue_cond(self):
        self.assertIs(True, self.trueAndTrue.cond(BlankText))
