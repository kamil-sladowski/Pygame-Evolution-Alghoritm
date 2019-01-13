from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle


class Matrix:

    def __init__(self):
        w, h = int(X_MAX / RADIUS / 2) + 2, int(Y_MAX / RADIUS / 2) + 2
        self.height = h
        self.width = w
        self.matrix = [[0 for _ in range(w)] for _ in range(h)]

    @staticmethod
    def __normalise_coordinates(pivot):
        x, y = pivot
        x = int(x / RADIUS / 2)
        y = int(y / RADIUS / 2)
        return x, y

    def get_neighbours_coordinates(self, pivot):
        neighbours_coordinates = []
        steps = [-1, 0, 1]
        x, y = pivot
        for i in steps:
            for j in steps:
                if i != 0 and j != 0:
                    xx, yy = x + i, y + j
                    if self.matrix[yy][xx] != 0:
                        neighbours_coordinates.append((xx, yy))
        if len(neighbours_coordinates) == 0:
            return x, y
        return neighbours_coordinates

    def get_random_neighbour_pivot(self, pivot):
        arr = self.get_neighbours_coordinates(pivot)
        if type(arr) == list:
            return choice(arr)
        else:
            return arr

    def print_matrix(self):
        for i in range(self.height):
            print(self.matrix[i])
