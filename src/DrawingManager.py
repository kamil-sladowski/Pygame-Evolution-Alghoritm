from Figures import Figures
from consts import *
from random import choice, getrandbits, random


class DrawingManager:

    def __init__(self):
        self.f = Figures()

    @staticmethod
    def is_point_in_range(x, y):
        if x > X_MAX/(2*RADIUS) or x < 0 or y > Y_MAX/(2*RADIUS) or y < 0:
            return False
        return True

    def __count_new_pivot(self, random_pivot):
        while True:
            x, y = random_pivot
            new_x = x + 2 * getrandbits(1) * choice([-1, 1])
            new_y = y + 2 * getrandbits(1) * choice([-1, 1])
            if self.is_point_in_range(new_x, new_y) and (not (new_x, new_y) in self.f.pivots):
                print("NEW PAIR: {}  :  {}".format(new_x, new_y))
                return int(new_x), int(new_y)

    def prepare_new_random_figure(self):
        pass
        # r = random()
        # pol = self.f.polygons_data
        # for figure_type, type_characteristics in pol.items():
        #     if type_characteristics.wheel_range[0] < r < type_characteristics.wheel_range[1]:
        #         verticles_count = int(figure_type)
        #         self.f.add(pivot=pivot_pos, figure_type=verticles_count)

    @staticmethod
    def get_herited_type(type_1, type_2):
        return choice([type_1, type_2])

    def count_shape_factor_based_on_neighbours(self):
        parent_pivot = self.f.random_pivot
        parent_id = self.f.id_matrix.get_id_by_pivot(parent_pivot)
        parent_shape = self.f[parent_id]

        neighbour_pivot = self.f.id_matrix.get_random_neighbour_pivot(parent_pivot)
        neighbour_id = self.f.id_matrix.get_id_by_pivot(neighbour_pivot)
        neighbour_shape = self.f[neighbour_id]


        child_pivot = self.__count_new_pivot(parent_pivot)
        herited_type = self.get_herited_type(parent_shape.type, neighbour_shape.type)
        self.f.add(pivot=child_pivot, figure_type=herited_type)
        neighbours_coordinates = self.f.id_matrix.get_neighbours_coordinates(child_pivot)
        self.f.count_neighbours_factor(parent_shape, neighbours_coordinates)

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

