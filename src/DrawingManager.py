from Figures import Figures
from consts import *
from random import randint, getrandbits


class DrawingManager:

    def __init__(self):
        self.f = Figures()
        self.f.add()

    @staticmethod
    def __is_point_in_range(x, y):
        if x > X_MAX or x < 0 or y > Y_MAX or y < 0:
            return False
        return True

    def __count_next_pivot(self):
        while True:
            x, y = self.f.random_pivot
            new_x = x + 2 * RADIUS * getrandbits(1)  # (-1 * getrandbits(1)) *
            new_y = y + 2 * RADIUS * getrandbits(1)  # (-1 * getrandbits(1)) *
            if self.__is_point_in_range(new_x, new_y) and (not (new_x, new_y) in self.f.pivots):
                print("NEW PAIR: {}  :  {}".format(new_x, new_y))
                return new_x, new_y
            # else:
            #     return 0,0

    def prepare_new_random_figure(self):
        pivot_pos = self.__count_next_pivot()
        verticle_num = randint(4, 6)
        self.f.add(pivot_pos, verticle_num)

    @property
    def elements_num(self):
        return len(self.f.pivots)

    @property
    def pivots(self):
        return self.f.pivots

    @property
    def figure_types(self):
        return self.f.figureType

