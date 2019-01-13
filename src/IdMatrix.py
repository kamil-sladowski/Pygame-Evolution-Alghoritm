from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle


class IdMatrix:

    def __init__(self):
        w, h = int(X_MAX / RADIUS / 2) + 2, int(Y_MAX / RADIUS / 2) + 2
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

    def remove_id(self, shape):
        x, y = shape.pivot
        self.id_matrix[y][x] = 0

    def get_free_space(self, first_parent_pivot,  size=3):
        new_free_space = []
        f_x, f_y = first_parent_pivot
        x_possibility = [f_x, f_x +1, f_x -1, f_x +2, f_x-2]
        y_possibility = [f_y, f_y +1, f_y -1, f_y +2, f_y-2]
        shuffle(x_possibility)
        shuffle(y_possibility)
        for new_x in x_possibility:
            for new_y in y_possibility:
                if self.id_matrix[new_y][new_x] == 0:
                    space_size = 1
                    x_opt = [-1, 0, 1]
                    y_opt = [-1, 0, 1]
                    for n_x in x_opt:
                        for n_y in y_opt:
                            if space_size < size and n_x != n_y and n_x !=0:
                                if self.id_matrix[n_y][n_x] == 0:
                                    new_free_space.append((n_x, n_y))
                                    space_size +=1
                    new_free_space.append((new_x, new_y))
        return new_free_space
