from random import choice, shuffle, randint, random

from recordtype import recordtype
from consts import X_MAX, Y_MAX, RADIUS, \
    INITIAL_INDIVIDUALS_NUM, INDIVIDUM_SIZE

Individual = recordtype('Individual', 'pivot, genotype fitness')


# def get_coordinates_from_grid_divided_to_3_x_3():
#     width, height = int(X_MAX / RADIUS / 2) + 2, int(Y_MAX / RADIUS / 2) + 2
#     pivots_3x = []
#     for x in range(0, width - 3 , 3):
#         for y in range(0, height - 3, 3):
#             pivots_3x.append((x, y))
#     print(pivots_3x)
#     return pivots_3x

def generate_colors():
    colors = []
    for _ in range(9):
        colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    return colors


def generate_initial_individuals(figure_obj):
    individuals = []

    for _ in range(INITIAL_INDIVIDUALS_NUM):
        colors = generate_colors()
        # try:
        individuals.append(figure_obj
                               .create_new_individual(figure_obj.used_pivots_by_individuals,
                                                      choice([4, 5, 6, 7, 8, 9]),
                                                      colors))
        # except TypeError:
        #     print("Limit exceeded") #???
        # except AttributeError:
        #     print("AttributeError")
    return individuals


def mutate(genotype_color):
    i = random()
    # if i > 0.9:
    #     for subcolor in genotype_color:
    #         genotype_color_tmp = subcolor
    #         mask = 1 << randint(0, 7)
    #         subcolor &= ~mask
    #         if subcolor == genotype_color_tmp:
    #             subcolor |= ~mask

    return genotype_color


def cross(ind_1, ind_2, figure_mgr):
    new_genotype_colors = []
    cross_propability = 1.0
    if cross_propability > 0.5:
        genotype_colors_1 = list(map(lambda g: g.color, ind_1.genotype))
        genotype_colors_2 = list(map(lambda g: g.color, ind_2.genotype))
        figures_to_change = randint(1, 9)
        residue_num = 9 - figures_to_change
        shuffle(genotype_colors_1)
        shuffle(genotype_colors_2)
        for i in range(figures_to_change):
            mask_r = randint(0, 255)
            mask_g = randint(0, 255)
            mask_b = randint(0, 255)
            r_1, g_1, b_1 = genotype_colors_1[i]
            r_2, g_2, b_2 = genotype_colors_2[i]

            new_r = (r_1 & mask_r) ^ r_2
            new_g = (g_1 & mask_g) ^ g_2
            new_b = (b_1 & mask_b) ^ b_2

            new_genotype_color = (new_r, new_g, new_b)
            new_genotype_color = mutate(new_genotype_color)
            new_genotype_colors.append(new_genotype_color)

        new_genotype_colors.extend(genotype_colors_1[0:residue_num])

        new_individual = figure_mgr.create_new_individual(
            figure_mgr.used_pivots_by_individuals, 4, new_genotype_colors)
    return new_individual


def calculate_fitness(individuals):
    f_max = 0
    for ind in individuals:
        for gen in ind.genotype:
            for subcolor in gen.color:
                ind.fitness += subcolor
                f_max += subcolor
    return f_max


def get_fitness_wheel(individuals, f_max):
    wheel = []
    previous = 0
    for ind in individuals:
        wheel.append((ind, previous, round(previous + ind.fitness / f_max, 4)))
        previous = round(previous + ind.fitness / f_max, 4)
    return wheel


def get_individuals_to_kill(individuals, fitness_wheel):
    how_much_kill = choice(range(0, int(len(individuals)/2)))
    individuals_to_delete = []
    for _ in range(how_much_kill):
        t = round(random(), 4)
        for wheel_range in fitness_wheel:
            if wheel_range[1] <= t < wheel_range[2]:
                # for ind in wheel_range[0]:
                individuals_to_delete.append(wheel_range[0])
                break

    return individuals_to_delete


def generate_population(individuals, figure_mgr):
    shuffle(individuals)
    for i in range(0, len(individuals) -2, 2):
        cross(individuals[i], individuals[i+1], figure_mgr)

    fitness_max = calculate_fitness(individuals)
    wheel = get_fitness_wheel(individuals, fitness_max)
    individuals_to_delete = get_individuals_to_kill(individuals, wheel)
    figure_mgr.remove_individual(individuals_to_delete)
