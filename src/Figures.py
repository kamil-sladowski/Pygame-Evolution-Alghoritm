from random import randint


class Figures:
    pivots = []
    figureType = []

    def __init__(self):
        self.pivots.append((50, 50))
        self.figureType.append(6)

    def __iter__(self):
        for pivot, type in zip(self.pivots, self.figureType):
            yield pivot, type

    def __len__(self):
        assert len(self.pivots) == len(self.figureType)
        return len(self.pivots)

    def __str__(self):
        return "Pivots: {} \n Types: {}".format(self.pivots, self.figureType)

    def add(self, position=(0,0), figure_type=3):
        self.pivots.append(position)
        self.figureType.append(figure_type)

    @property
    def random_pivot(self):
        id = randint(0, len(self.pivots) - 1)
        return self.pivots[id]





