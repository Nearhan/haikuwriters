from nltk.tree import Tree


class ScoreTree(Tree):
    _score = None
    def __init__(self, node, *children:Tree):
        super().__init__(node, tuple(children))
        self._children = tuple([child for child in self if child is not Nil])

    @property
    def children(self):
        return self._children

    def __str__(self):
        return "Nil" if self.node == None else super().__str__()

    def __repr__(self):
        return "Nil" if self.node == None else super().__repr__()

    @property
    def score(self):
        return 0 if self._score is None else self._score

    def __eq__(self, other):
        if type(other) is type(self):
            return vars(self) == vars(other)
        return NotImplemented

    def __hash__(self):
        return hash((vars(self), hash(self.tree)))


Nil = ScoreTree(None)


class Score(ScoreTree):
    def __init__(self, score:int):
        self._score = score
        super().__init__(score, Nil)

    def __str__(self):
        return str(self.score)

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.score) + ")"


class ScoreTerm(ScoreTree):
    def __init__(self, meta, tree:ScoreTree):
        self.meta = meta
        self.tree = tree
        self._score = tree.score
        super().__init__(tree.node, *tree.children)

    def __getitem__(self, index):
        return super().__getitem__(index - 1)

    def __str__(self):
        return str(self.meta) + "@" + str(self.tree)

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.meta) + ", " + repr(self.tree) + ")"
