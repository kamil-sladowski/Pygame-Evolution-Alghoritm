from random import choice, shuffle, getrandbits
from consts import X_MAX, Y_MAX, RADIUS
from Shape import Shape
from IdMatrix import IdMatrix
from IslandMatrix import IslandMatrix
from FigureMatrix import FigureMatrix
from recordtype import recordtype
from consts import SHAPE_TYPE_MIN, SHAPE_TYPE_MAX, MUTATION_PROPABILITY
from copy import deepcopy

PolygonCharacteristic = recordtype('PolygonsData', 'instance_count, probability, wheel_range')
Individual = recordtype('Individual', 'pivot, genotype fitness')


class Figures:
    range_begin, range_end = (SHAPE_TYPE_MIN, SHAPE_TYPE_MAX)
    shapes = []
    polygons_data = {}
    used_pivots_by_individuals = [(3, 3)]

    def __init__(self):
        self.figure_matrix = FigureMatrix()
        self.id_matrix = IdMatrix(self.figure_matrix)
        self.island_matrix = IslandMatrix(self.id_matrix, self.figure_matrix)
        self.__take_polygon_characteristics()

    def __generate_polygon_characteristic(self):
        probability = 1 / len(range(self.range_begin, self.range_end + 1))
        previous_polygon = PolygonCharacteristic(0, probability, (0, probability))
        yield previous_polygon

        for i in range(self.range_begin + 1, self.range_end + 1):
            previous_range = previous_polygon.wheel_range[1]
            new_polygon = PolygonCharacteristic(0, probability, (previous_range, previous_range + probability))
            yield new_polygon
            previous_polygon = new_polygon

    def __take_polygon_characteristics(self):
        polygon_generator = self.__generate_polygon_characteristic()
        for i in range(self.range_begin, self.range_end + 1):
            self.polygons_data[str(i)] = next(polygon_generator)

    def __len__(self):
        return len(self.shapes)

    def __getitem__(self, i) -> Shape:
        for e in self.shapes:
            if e.id == i:
                return e

    @staticmethod
    def is_point_in_range(x, y):
        if x + 1 > X_MAX / (2 * RADIUS) or x < 0 or y + 1 > Y_MAX / (2 * RADIUS) or y < 0:
            return False
        return True

    def __count_new_pivot(self, used_pivots):
        shuffle(used_pivots)
        for _ in range(len(used_pivots) * 3):
            for pivot in used_pivots:
                x, y = pivot
                new_x = x + getrandbits(1) * choice([-3, 3])
                new_y = y + getrandbits(1) * choice([-3, 3])
                if self.is_point_in_range(new_x, new_y) and (self.id_matrix[new_x, new_y] == 0):
                    return (int(new_x), int(new_y)), (x, y)

    def create_new_individual(self, used_pivots, herited_type, colors):
        genotype = []
        x_space = [0, 0, 1, 1, 1, 2, 2, 2]
        y_space = [1, 2, 0, 1, 2, 0, 1, 2]

        def create_child_shapes_in_individual(new_pivot):
            x_P, y_P = new_pivot
            for k in range(8):
                shape = self.add(pivot=(x_P + x_space[k], y_P + y_space[k]),
                                 figure_type=herited_type, color=colors[k])
                genotype.append(shape)

        new_pivot, previous_pivot = self.__count_new_pivot(used_pivots)

        used_pivots.append(new_pivot)

        shape = self.add(pivot=new_pivot, figure_type=herited_type, color=colors[0])
        genotype.append(shape)
        try:
            create_child_shapes_in_individual(new_pivot)
        except IndexError as e:
            print("Index error")
            print(e.args)
        return Individual(pivot=new_pivot, genotype=genotype, fitness=0)

    def remove_individual(self, individuals_to_delete, all_individuals):
        for ind in individuals_to_delete:
            self.used_pivots_by_individuals.remove(ind.pivot)
            for shape in ind.genotype:
                self.polygons_data[str(shape.type)].instance_count -= 1
                self.id_matrix.remove_id(shape.id)
                self.shapes.remove(shape)

            all_individuals.remove(ind)

    def add(self, pivot=(int(X_MAX / (4 * RADIUS)), int(Y_MAX / (4 * RADIUS))),
            figure_type=int(SHAPE_TYPE_MAX / 2), color=(100, 200, 100)):
        s = Shape(figure_type, pivot, color=color)
        self.shapes.append(s)
        self.polygons_data[str(figure_type)].instance_count += 1
        self.id_matrix.add_id(s)
        return s

    @property
    def number_of_all_verticles(self) -> int:
        vert_num = 0
        for type in self.polygons_data.keys():
            vert_num += int(type) * self.polygons_data[type].instance_count
        return vert_num

    @property
    def pivots(self) -> list:
        pivots = []
        for e in self.shapes:
            pivots.append(e.pivot)
        return pivots

    @property
    def figure_types(self) -> list:
        f_types = []
        for e in self.shapes:
            f_types.append(e.type)
        return f_types
