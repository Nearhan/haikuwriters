from nltk.tree import ImmutableTree


class ScoreTree(ImmutableTree):
    def __init__(self, node, *children:ImmutableTree):
        super().__init__(node, tuple(children))
        self._children = tuple([child for child in self if child is not Nil])

    @property
    def children(self):
        return self._children

    def __str__(self):
        return "Nil" if self.node == None else super().__str__()

    def __repr__(self):
        return "Nil" if self.node == None else super().__repr__()


Nil = ScoreTree(None)


class Score(ScoreTree):
    def __init__(self, score:int):
        self.score = score
        super().__init__(score, Nil)

    def __str__(self):
        return str(self.score)

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.score) + ")"

    def __eq__(self, other):
        return self.score == other.score

    def __hash__(self):
        # the hash of an int is the int itself
        return self.score


class ScoreTerm(ScoreTree):
    def __init__(self, meta, tree:ScoreTree):
        super().__init__(tree.node, *tree.children)
        self.meta = meta
        self.tree = tree

    def __str__(self):
        return str(self.meta) + "@" + str(self.tree)

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.meta) + ", " + repr(self.tree) + ")"

    def __eq__(self, other):
        return self.meta == other.meta and self.tree == other.tree

    def __hash__(self):
        return hash((self.meta, hash(self.tree)))