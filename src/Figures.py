from random import randint
from consts import X_MAX, Y_MAX
from recordtype import recordtype

PolygonsData = recordtype('PolygonsData', 'instance_num, probability, wheel_range')

class Figures:
    range_begin, range_end = (4, 7)
    pivots = []
    figureType = []
    polygons_data = {}

    def generate_polygon_data(self):
        probability = 1/len(range(self.range_begin, self.range_end + 1))
        print("probability {}".format(probability))
        previous_polygon = PolygonsData(0, probability, (0, probability))
        yield previous_polygon

        for i in range(self.range_begin + 1, self.range_end+1):
            previous_range = previous_polygon.wheel_range[1]
            new_polygon = PolygonsData(0, probability, (previous_range, previous_range + probability))
            yield new_polygon
            previous_polygon = new_polygon

    def __init__(self):
        polygon_generator = self.generate_polygon_data()
        for i in range(self.range_begin, self.range_end + 1):
            self.polygons_data[str(i)] = next(polygon_generator)



    def __iter__(self):
        for pivot, f_type in zip(self.pivots, self.figureType):
            yield pivot, f_type

    def __len__(self):
        assert len(self.pivots) == len(self.figureType)
        return len(self.pivots)

    def __str__(self):
        return "Pivots: {} \n Types: {}".format(self.pivots, self.figureType)

    def add(self, position=(X_MAX/2, Y_MAX/2), figure_type=4):
        self.pivots.append(position)
        self.figureType.append(figure_type)
        self.polygons_data[str(figure_type)].instance_num += 1

    @property
    def random_pivot(self):
        id = randint(0, len(self.pivots) - 1)
        return self.pivots[id]

    @property
    def number_of_all_verticles(self):
        vert_num = 0
        for type in self.polygons_data.keys():
            vert_num += int(type) * self.polygons_data[type].instance_num
        return vert_num
    #
    # @property
    # def polygon_data(self):
    #     print(self.polygons_data)
    #     return self.polygons_data


