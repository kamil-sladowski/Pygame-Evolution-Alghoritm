
class Shape:

    __count = 0
    neighbours_field_factor = 0

    @classmethod
    def _count(cls):
        Shape.__count += 1
        return Shape.__count

    def __init__(self, type, pivot, color=(100,200,100)):
        self.id = Shape._count()
        self.type = type
        self.pivot = pivot
        self.color = color

    def __str__(self):
        return "ID: {} Type: {} Pivot {} Factor {}".format(
            self.id, self.type, self.pivot, self.neighbours_field_factor)
