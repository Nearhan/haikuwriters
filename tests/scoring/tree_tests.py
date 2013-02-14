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

    def test_score_nil(self):
        self.assertEqual(0, Nil.score)


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

    def test_score_one(self):
        self.assertEqual(1, self.one.score)


class TestScoreTerm(TestCase):

    def setUp(self):
        self.a_one = ScoreTerm("a", Score(1))
        self.x_nil = ScoreTerm("x", Nil)
        self.y_nil = ScoreTerm("y", Nil)
        self.nest_x = ScoreTerm("nest_x", self.x_nil)
        self.nest_y = ScoreTerm("nest_y", self.y_nil)

    def test_str_nil(self):
        self.assertEqual("x@Nil", str(self.x_nil))

    def test_str_score(self):
       self.assertEqual("a@1", str(self.a_one))

    def test_repr_nil(self):
        self.assertEqual("ScoreTerm('x', Nil)", repr(self.x_nil))

    def test_repr_score(self):
        self.assertEqual("ScoreTerm('a', Score(1))", repr(self.a_one))

    def test_equal_scoreterm(self):
        self.assertEqual(self.x_nil, self.x_nil)

    def test_not_equal_scoreterm(self):
        self.assertNotEqual(self.x_nil, self.y_nil)

    def test_equal_nested_scoreterm(self):
        self.assertEqual(self.nest_x, self.nest_x)

    def test_not_equal_nested_scoreterm(self):
        self.assertNotEqual(self.nest_x, self.nest_y)

    def test_score_one_not_equal_scoreterm_one(self):
        self.assertNotEqual(Score(1), self.a_one)

    def test_score_nil_not_equal_scoreterm_nil(self):
        self.assertNotEqual(Nil, self.x_nil)

    def test_score_one_not_equal_scoreterm_nil(self):
        self.assertNotEqual(Score(1), self.x_nil)

    def test_scoreterm_one_score(self):
        self.assertEqual(1, self.a_one.score)

    def test_scoreterm_nil_score(self):
        self.assertEqual(Nil.score, self.x_nil.score)


class TestOperations(TestCase):

    def setUp(self):
        self.one_plus_one = Add(Score(1), Score(1))
        self.two_times_two = Multiply(Score(2), Score(2))
        self.three_times_four_plus_five = Multiply(Score(3), Add(Score(4), Score(5)))
        self.choose = Choose(
            ScoreTerm(0.5, Score(-1)),
            ScoreTerm(0.5, Score(1))
        )
        self.nested_choose = Multiply(
            self.choose,
            Score(5)
        )

    def test_str_add(self):
        self.assertEqual("(1 + 1)", str(self.one_plus_one))

    def test_repr_add(self):
        self.assertEqual("Add(Score(1), Score(1))", repr(self.one_plus_one))

    def test_equal_add(self):
        self.assertEqual(self.one_plus_one, self.one_plus_one)

    def test_score_add(self):
        self.assertEqual(2, self.one_plus_one.score)

    def test_str_multiply(self):
        self.assertEqual("(2 * 2)", str(self.two_times_two))

    def test_repr_multiply(self):
        self.assertEqual("Multiply(Score(2), Score(2))", repr(self.two_times_two))

    def test_score_multiply(self):
        self.assertEqual(4, self.two_times_two.score)

    def test_str_choose(self):
        self.assertEqual("(-1 {50%} | 1 {50%})", str(self.choose))

    def test_repr_choose(self):
        self.assertEqual("Choose(ScoreTerm(0.5, Score(-1)), ScoreTerm(0.5, Score(1)))", repr(self.choose))

    def test_str_nested_infix(self):
        self.assertEqual("(3 * (4 + 5))", str(self.three_times_four_plus_five))

    def test_repr_nested_infix(self):
        self.assertEqual("Multiply(Score(3), Add(Score(4), Score(5)))", repr(self.three_times_four_plus_five))

    def test_str_nested_choose(self):
        self.assertEqual("((-1 {50%} | 1 {50%}) * 5)", str(self.nested_choose))

    def test_repr_nested_choose(self):
        self.assertEqual(
            "Multiply(Choose(ScoreTerm(0.5, Score(-1)), ScoreTerm(0.5, Score(1))), Score(5))",
            repr(self.nested_choose)
        )
