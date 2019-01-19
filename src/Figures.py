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


class Figures:
    range_begin, range_end = (SHAPE_TYPE_MIN, SHAPE_TYPE_MAX)
    shapes = []
    polygons_data = {}

    def __init__(self):
        self.figure_matrix = FigureMatrix()
        self.id_matrix = IdMatrix(self.figure_matrix)
        self.island_matrix = IslandMatrix(self.id_matrix, self.figure_matrix)
        self.__take_polygon_characteristics()
        self.add(pivot=(int(X_MAX / (8*RADIUS)), int(Y_MAX / (8*RADIUS))), figure_type=4)
        self.add(pivot=(int(X_MAX / (8*RADIUS)), int(Y_MAX / (3*RADIUS))), figure_type=5)
        self.add(pivot=(int(X_MAX / (3*RADIUS)), int(Y_MAX / (8*RADIUS))), figure_type=6)
        self.add(pivot=(int(X_MAX / (3*RADIUS)), int(Y_MAX / (3*RADIUS))), figure_type=7)

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
        if x > X_MAX/(2*RADIUS) or x < 0 or y > Y_MAX/(2*RADIUS) or y < 0:
            return False
        return True

    def __count_new_pivot(self, ):
        pivots_tmp = list(map(lambda shape: shape.pivot, self.shapes))
        shuffle(pivots_tmp)
        for pivot in pivots_tmp:
            x, y = pivot
            new_x = x + getrandbits(1) * choice([-1, 1])
            new_y = y + getrandbits(1) * choice([-1, 1])
            if self.is_point_in_range(new_x, new_y) and (self.id_matrix[new_x, new_y] == 0): # todo matrix[x, y]
                return (int(new_x), int(new_y)), (x, y)

    def create_new_object(self, herited_type):
        try:
            child_pivot, parent_pivot = self.__count_new_pivot()
            self.add(pivot=child_pivot, figure_type=herited_type)
        except TypeError:
            print("Limit exceeded")


    def evolution(self):
        print("")
        print("")
        self.island_matrix.detect_islands()
        self.island_matrix.calc_island_statistics()
        self.island_matrix.print_matrix()
        number_of_islands = self.island_matrix.get_number_of_islands()
        if number_of_islands > 1:
            island_ids = [i+1 for i in range(number_of_islands)]
            shuffle(island_ids)
            for i in range(0, number_of_islands, 2):
                try:
                    for _ in range(choice([1,2,3])):
                        child_type = self.island_matrix.deduce_child_type(island_ids[i], island_ids[i+1])
                        self.create_new_object(child_type)
                except IndexError:
                    self.island_matrix.print_matrix()
                    print("IndexError in evolution")

            # self.island_matrix.detect_islands()
            # self.island_matrix.calc_island_statistics()

            islands_to_delete = self.island_matrix.get_islands_to_kill()
            for id in islands_to_delete:
                shape_to_delete = self.id_matrix.remove_id(id)
                self.remove_shape(shape_to_delete)

        else:
            self.create_new_object(choice([4,5,6,7,8,9]))

    def remove_shape(self, shape):
        shape_copy = deepcopy(shape)
        self.polygons_data[str(shape_copy.type)].instance_count -= 1
        self.shapes.remove(shape)

    # @staticmethod
    # def mutate(shape):
    #     r = random()
    #     t = shape.type
    #     mutation_types = [t-1, t, t+1,]
    #     if r > MUTATION_PROPABILITY:
    #         while True:
    #             try:
    #                 shuffle(mutation_types)
    #                 t = choice([mutation_types[0], mutation_types[1]])
    #                 assert t in range(SHAPE_TYPE_MIN, SHAPE_TYPE_MAX)
    #                 shape.type = t
    #                 return t
    #             except KeyError:
    #                 pass
    #             except AssertionError:
    #                 pass
    #     return t

    def add(self, pivot=(int(X_MAX / (4*RADIUS)), int(Y_MAX / (4*RADIUS))), figure_type=int(SHAPE_TYPE_MAX/2)):
        a = Shape(figure_type, pivot)
        # figure_type = self.mutate(a)
        self.shapes.append(a)
        self.polygons_data[str(figure_type)].instance_count += 1
        self.id_matrix.add_id(a)



    # def count_neighbours_factor(self, parent:Shape, coordinates):
    #     factor = SHAPE_TYPE_MAX * 8
    #     try:
    #         for x, y in coordinates:
    #             id = self.id_matrix.id_matrix[y][x]
    #             neigh_shape = self.shapes[id]
    #             if parent.type == neigh_shape.type:
    #                 factor -= int(neigh_shape.type)
    #             else:
    #                 factor += int(neigh_shape.type)
    #     except TypeError:
    #         pass
    #     finally:
    #         parent.neighbours_field_factor = factor
    #         return factor

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
