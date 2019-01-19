from random import choice

from recordtype import recordtype
from consts import X_MAX, Y_MAX, RADIUS, INITIAL_INDIVIDUALS_NUM


Individual = recordtype('Individual', 'pivot, genotype')


def get_coordinates_from_grid_divided_to_3_x_3():
    width, height = int(X_MAX / RADIUS / 2) + 2, int(Y_MAX / RADIUS / 2) + 2
    pivots_3x = []
    for x in range(0, width - 3 , 3):
        for y in range(0, height - 3, 3):
            pivots_3x.append((x, y))
    print(pivots_3x)
    return pivots_3x


def generate_initial_individuals(figure_obj):
    used_pivots = [(3,3)]
    individuals = []
    for _ in range(INITIAL_INDIVIDUALS_NUM):
        individuals.append(figure_obj.create_new_individual(used_pivots, choice([4, 5, 6, 7, 8, 9])))

get_coordinates_from_grid_divided_to_3_x_3()