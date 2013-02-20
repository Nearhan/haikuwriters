from nltk.tree import Tree


class ScoreTree(Tree):
    _score = 0
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

    def score(self):
        return self._score

    def __eq__(self, other):
        if type(other) is type(self):
            return vars(self) == vars(other)
        return NotImplemented

    def __hash__(self):
        # Hash all variable name: value pairs along with the hash of all the children
        return hash((tuple(vars(self).items()), hash(self.children)))


Nil = ScoreTree(None)


class Score(ScoreTree):
    def __init__(self, score:int):
        self._score = score
        super().__init__(score, Nil)

    def __str__(self):
        return str(self._score)

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self._score) + ")"


class ScoreTerm(ScoreTree):
    def __init__(self, meta, tree:ScoreTree):
        self.meta = meta
        self.tree = tree
        super().__init__(tree.node, *tree.children)

    def __getitem__(self, index):
        return super().__getitem__(index - 1)

    def __str__(self):
        return str(self.meta) + "@" + str(self.tree)

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.meta) + ", " + repr(self.tree) + ")"

    @property
    def _score(self):
        return self.tree.score()

