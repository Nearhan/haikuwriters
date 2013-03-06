from unittest import TestCase
from haikuwriters.scoring.algebra import Add, Multiply
from haikuwriters.scoring.tree import BlankText, Score


class TestAlgebraOperations(TestCase):

    def setUp(self):
        self.one_plus_one = Add(Score(1), Score(1))
        self.two_times_two = Multiply(Score(2), Score(2))
        self.three_times_four_plus_five = Multiply(Score(3), Add(Score(4), Score(5)))

    def test_str_add(self):
        self.assertEqual("(1 + 1)", str(self.one_plus_one))

    def test_repr_add(self):
        self.assertEqual("Add(Score(1), Score(1))", repr(self.one_plus_one))

    def test_str_nested_infix(self):
        self.assertEqual("(3 * (4 + 5))", str(self.three_times_four_plus_five))

    def test_repr_nested_infix(self):
        self.assertEqual("Multiply(Score(3), Add(Score(4), Score(5)))", repr(self.three_times_four_plus_five))

    def test_equal_add(self):
        self.assertEqual(self.one_plus_one, self.one_plus_one)

    def test_score_add(self):
        self.assertEqual(2, self.one_plus_one.score(BlankText))

    def test_str_multiply(self):
        self.assertEqual("(2 * 2)", str(self.two_times_two))

    def test_repr_multiply(self):
        self.assertEqual("Multiply(Score(2), Score(2))", repr(self.two_times_two))

    def test_score_multiply(self):
        self.assertEqual(4, self.two_times_two.score(BlankText))
