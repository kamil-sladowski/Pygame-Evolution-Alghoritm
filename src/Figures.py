from random import randint
from consts import X_MAX, Y_MAX, RADIUS
from recordtype import recordtype

PolygonCharacteristic = recordtype('PolygonsData', 'instance_count, probability, wheel_range')


class Shape:

    __count = 0

    @classmethod
    def _count(cls):
        Shape.__count += 1
        return Shape.__count

    def __init__(self, type, pivot):
        self.id = Shape._count()
        self.type = type
        self.pivot = pivot

    def __str__(self):
        return "ID: {} Type: {} Pivot {}".format(self.id, self.type, self.pivot)


class IdMatrix:

    def __init__(self):
        w, h = int(X_MAX / RADIUS / 2), int(Y_MAX / RADIUS / 2)
        self.height = h
        self.id_matrix = [[0 for _ in range(w)] for _ in range(h)]

    def add_id(self, id, pivot):
        x, y = pivot
        x = int(x / RADIUS / 2) - 1
        y = int(y / RADIUS / 2) - 1
        self.id_matrix[x][y] = id

    def print_id_matrix(self):
        for i in range(self.height):
            print(self.id_matrix[i])


class Figures:
    range_begin, range_end = (4, 7)
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

    # def __iter__(self):
    #     for f in self.shapes:
    #         yield f.id, f.pivot, f.type

    def __getitem__(self, i) -> Shape:
        for e in self.shapes:
            if e.id == i:
                return e

    def add(self, pivot=(X_MAX / 2, Y_MAX / 2), figure_type=4):
        a = Shape(figure_type, pivot)
        self.shapes.append(a)
        self.polygons_data[str(figure_type)].instance_count += 1
        self.id_matrix.add_id(a.id, pivot)
        self.id_matrix.print_id_matrix()

    @property
    def random_pivot(self) -> tuple:
        id = randint(0, len(self.shapes) - 1)
        return self.shapes[id].pivot

    def get_neighbours(self, curr_id):
        pass

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
