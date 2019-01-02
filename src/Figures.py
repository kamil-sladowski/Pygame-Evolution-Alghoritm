from random import randint, random, choice
from consts import X_MAX, Y_MAX, RADIUS
from Shape import Shape
from IdMatrix import IdMatrix
from recordtype import recordtype
from consts import SHAPE_TYPE_MIN, SHAPE_TYPE_MAX, MUTATION_PROPABILITY
from copy import deepcopy

PolygonCharacteristic = recordtype('PolygonsData', 'instance_count, probability, wheel_range')


class Figures:
    range_begin, range_end = (SHAPE_TYPE_MIN, SHAPE_TYPE_MAX)
    shapes = []
    polygons_data = {}

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

    def __init__(self):
        self.id_matrix = IdMatrix()
        self.__take_polygon_characteristics()
        self.add()

    def __len__(self):
        return len(self.shapes)

    def __getitem__(self, i) -> Shape:
        for e in self.shapes:
            if e.id == i:
                return e

    @staticmethod
    def mutate(shape):
        r = random()
        t = shape.type
        if r > MUTATION_PROPABILITY:
            t = choice(range(SHAPE_TYPE_MIN, SHAPE_TYPE_MAX))
            shape.type = t
            return t
        else:
            return t

    def add(self, pivot=(int(X_MAX / (4*RADIUS)), int(Y_MAX / (4*RADIUS))), figure_type=4):
        a = Shape(figure_type, pivot)
        figure_type = self.mutate(a)
        self.shapes.append(a)
        self.polygons_data[str(figure_type)].instance_count += 1
        self.id_matrix.add_id(a.id, pivot)
        # self.id_matrix.print_id_matrix()

    def remove_shape(self, shape):
        try:
            shape_copy = deepcopy(shape)
            self.polygons_data[str(shape_copy.type)].instance_count -= 1
            self.id_matrix.remove_id(shape)
            self.shapes.remove(shape)
        except ValueError:
            pass

    def focuse_wheel(self):
        f_max = 0
        wheel = []
        for e in self.shapes:
            f_max += e.neighbours_field_factor
        previous = 0
        for e in self.shapes:
            wheel.append((e, previous, previous + e.neighbours_field_factor/f_max))

        return wheel, f_max

    def count_neighbours_factor(self, parent:Shape, coordinates):
        factor = SHAPE_TYPE_MAX * 8
        try:
            for x, y in coordinates:
                id = self.id_matrix.id_matrix[y][x]
                neigh_shape = self.shapes[id]
                if parent.type == neigh_shape.type:
                    factor -= int(neigh_shape.type)
                else:
                    factor += int(neigh_shape.type)
        except TypeError:
            pass
        finally:
            parent.neighbours_field_factor = factor
            return factor

    @property
    def random_pivot(self) -> tuple:
        id = randint(0, len(self.shapes) - 1)
        return self.shapes[id].pivot

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
