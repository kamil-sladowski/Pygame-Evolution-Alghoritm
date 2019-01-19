from Figures import Figures
from consts import *


class DrawingManager:

    def __init__(self):
        self.f = Figures()

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

