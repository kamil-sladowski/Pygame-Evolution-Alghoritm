from random import randint
from consts import X_MAX, Y_MAX


class Figures:
    pivots = []
    figureType = []
    types_polygon_number = {
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
    }

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
        self.types_polygon_number[str(figure_type)] +=1
        print(self.types_polygon_number)

    @property
    def random_pivot(self):
        id = randint(0, len(self.pivots) - 1)
        return self.pivots[id]





