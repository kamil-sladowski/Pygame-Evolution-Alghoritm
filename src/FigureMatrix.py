from copy import deepcopy

from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle
from Matrix import Matrix


class FigureMatrix(Matrix):

    def set_type(self, x, y, type):
        self.matrix[y][x] = type

    def __getitem__(self, pos):
        x, y = pos
        return self.matrix[y][x]

