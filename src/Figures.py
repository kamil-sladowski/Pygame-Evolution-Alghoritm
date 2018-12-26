from random import randint
from consts import X_MAX, Y_MAX


class Figures:
    pivots = []
    figureType = []

    def __iter__(self):
        for pivot, f_type in zip(self.pivots, self.figureType):
            yield pivot, f_type

    def __len__(self):
        assert len(self.pivots) == len(self.figureType)
        return len(self.pivots)

    def __str__(self):
        return "Pivots: {} \n Types: {}".format(self.pivots, self.figureType)

    def add(self, position=(X_MAX/2, Y_MAX/2), figure_type=12):
        self.pivots.append(position)
        self.figureType.append(figure_type)

    @property
    def random_pivot(self):
        id = randint(0, len(self.pivots) - 1)
        return self.pivots[id]





