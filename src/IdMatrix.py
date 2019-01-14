from copy import deepcopy

from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle
from Matrix import Matrix


class IdMatrix(Matrix):

    def __init__(self, figure_matrix):
        super().__init__()
        self.figure_matrix = figure_matrix
        self.shapes = {}

    def add_id(self, shape):
        x, y = shape.pivot
        self.matrix[y][x] = shape.id
        self.shapes[shape.id] = shape
        self.figure_matrix.set_type(x, y, shape.type)

    def get_id_by_pivot(self, pivot):
        x, y = pivot
        return self.matrix[y][x]

    def remove_id(self, id):
        x, y = self.shapes[id].pivot
        self.matrix[y][x] = 0
        self.figure_matrix.set_type(x, y, 0)
        self.shapes.pop(id)

    def __getitem__(self, pos):
        x, y = pos
        return self.matrix[y][x]

