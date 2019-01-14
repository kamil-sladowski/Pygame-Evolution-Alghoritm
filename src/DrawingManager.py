from Figures import Figures
from consts import *
from random import choice, getrandbits, random


class DrawingManager:

    def __init__(self):
        self.f = Figures()
        self.f_wheel = 0
        self.f_max = 0




    # def kill_series(self):
    #     kill_pr   opability = random()
    #
    #     if kill_propability > KILL_PROPABILITY:
    #         kill_factor = int(len(self.f)/4)
    #         for _ in range(kill_factor):
    #             r = random() / self.f_max
    #             for e, range_begin, range_end in self.f_wheel:
    #                 if range_begin < r < range_end:
    #                     self.f.remove_shape(e)

    @property
    def elements_num(self):
        return len(self.f.shapes)

    @property
    def pivots(self) -> list:
        return self.f.pivots

    @property
    def figure_types(self) -> list:
        return self.f.figure_types

    @property
    def number_of_all_verticles(self):
        return self.f.number_of_all_verticles

