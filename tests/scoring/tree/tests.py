from unittest import TestCase
from haikuwriters.scoring.oper import Add, Multiply, Choose
from haikuwriters.scoring.tree import ScoreTree, Score, Nil, ScoreTerm


class TestScoreTree(TestCase):
    def test_str_nil(self):
        self.assertEqual("Nil", str(Nil))

    def test_repr_nil(self):
        self.assertEqual("Nil", repr(Nil))

    def test_str_nil_equals_str_empty(self):
        self.assertEqual(str(Nil), str(ScoreTree(None)))

    def test_repr_nil_equals_repr_empty(self):
        self.assertEqual(repr(Nil), repr(ScoreTree(None)))

    def test_equal_empty_and_nil(self):
        self.assertEqual(Nil, ScoreTree(None))


class TestScore(TestCase):

    def setUp(self):
        self.one = Score(1)
        self.zero = Score(0)

    def test_str_score(self):
        self.assertEqual("1", str(self.one))

    def test_repr_score(self):
        self.assertEqual("Score(1)", repr(self.one))

    def test_equal_scores(self):
        self.assertEqual(self.one, self.one)

    def test_not_equal_scores(self):
        self.assertNotEqual(self.one, self.zero)


class TestScoreTerm(TestCase):

    def setUp(self):
        self.a = ScoreTerm("a", Score(1))
        self.x = ScoreTerm("x", Nil)
        self.y = ScoreTerm("y", Nil)
        self.nest_x = ScoreTerm("nest_x", self.x)
        self.nest_y = ScoreTerm("nest_y", self.y)

    def test_str_nil(self):
        self.assertEqual("x@Nil", str(self.x))

    def test_str_score(self):
       self.assertEqual("a@1", str(self.a))

    def test_repr_nil(self):
        self.assertEqual("ScoreTerm('x', Nil)", repr(self.x))

    def test_repr_score(self):
        self.assertEqual("ScoreTerm('a', Score(1))", repr(self.a))

    def test_equal_scoreterm(self):
        self.assertEqual(self.x, self.x)

    def test_not_equal_scoreterm(self):
        self.assertNotEqual(self.x, self.y)

    def test_equal_nested_scoreterm(self):
        self.assertEqual(self.nest_x, self.nest_x)

    def test_not_equal_nested_scoreterm(self):
        self.assertNotEqual(self.nest_x, self.nest_y)


class TestOperations(TestCase):

    def setUp(self):
        self.one_plus_one = Add(Score(1), Score(1))

    def test_str_add(self):
        self.assertEqual("(1 + 1)", str(self.one_plus_one))

    def test_repr_add(self):
        self.assertEqual("Add(Score(1), Score(1))", repr(self.one_plus_one))

    def test_equal_add(self):
        self.assertEqual(self.one_plus_one, self.one_plus_one)

    def test_str_multiply(self):
        self.assertEqual("(1 * 1)", str(Multiply(Score(1), Score(1))))

    def test_str_choose(self):
        actual = Choose(
            ScoreTerm(.2, Score(2)),
            ScoreTerm(.4, Score(3))
        )
        self.assertEqual("(2 {20%} | 3 {40%})", str(actual))

    def test_str_nested(self):
        self.assertEqual("(1 * (2 + 3))", str(Multiply(Score(1), Add(Score(2), Score(3)))))


