from Figures import Figures
from consts import *
from random import choice, getrandbits, random


class DrawingManager:

    def __init__(self):
        self.f = Figures()
        self.f_wheel = 0
        self.f_max = 0

    @staticmethod
    def is_point_in_range(x, y):
        if x > X_MAX/(2*RADIUS) or x < 0 or y > Y_MAX/(2*RADIUS) or y < 0:
            return False
        return True

    def __count_new_pivot(self, ):
        while True:
            x, y = self.f.random_pivot
            new_x = x + getrandbits(1) * choice([-1, 1])
            new_y = y + getrandbits(1) * choice([-1, 1])
            if self.is_point_in_range(new_x, new_y) and (self.f.id_matrix.matrix[new_y][new_x] == 0): # todo matrix[x, y]
                return (int(new_x), int(new_y)), (x, y)

    @staticmethod
    def get_herited_type(type_1, type_2):
        return choice([type_1, type_2])

    def create_new_object(self):
        child_pivot, parent_pivot = self.__count_new_pivot()
        parent_id = self.f.id_matrix.get_id_by_pivot(parent_pivot)
        parent_shape = self.f[parent_id]

        neighbour_pivot = self.f.id_matrix.get_random_neighbour_pivot(parent_pivot)
        neighbour_id = self.f.id_matrix.get_id_by_pivot(neighbour_pivot)
        neighbour_shape = self.f[neighbour_id]
        herited_type = self.get_herited_type(parent_shape.type, neighbour_shape.type)

        self.f.add(pivot=child_pivot, figure_type=herited_type)
        neighbours_coordinates = self.f.id_matrix.get_neighbours_coordinates(child_pivot)
        self.f.count_neighbours_factor(parent_shape, neighbours_coordinates)
        self.f_wheel, self.f_max = self.f.focuse_wheel()

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

