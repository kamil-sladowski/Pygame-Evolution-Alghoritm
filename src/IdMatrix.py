from consts import X_MAX, Y_MAX, RADIUS
from random import choice


class IdMatrix:

    def __init__(self):
        w, h = int(X_MAX / RADIUS / 2) + 1, int(Y_MAX / RADIUS / 2) + 1
        self.height = h
        self.id_matrix = [[0 for _ in range(w)] for _ in range(h)]

    @staticmethod
    def __normalise_coordinates(pivot):
        x, y = pivot
        x = int(x / RADIUS / 2)
        y = int(y / RADIUS / 2)
        return x, y

    def add_id(self, id, pivot):
        x, y = pivot
        self.id_matrix[y][x] = id

    def get_id_by_pivot(self, pivot):
        x, y = pivot
        return self.id_matrix[y][x]

    def print_id_matrix(self):
        for i in range(self.height):
            print(self.id_matrix[i])

    def get_neighbours_coordinates(self, pivot):
        neighbours_coordinates = []
        steps = [-1, 0, 1]
        x, y = pivot
        for i in steps:
            for j in steps:
                if i != 0 and j != 0:
                    xx, yy = x + i, y + j
                    if self.id_matrix[yy][xx] != 0:
                        print(self.id_matrix[yy][xx])
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


