
class Shape:

    __count = 0
    neighbours_field_factor = 0

    @classmethod
    def _count(cls):
        Shape.__count += 1
        return Shape.__count

    def __init__(self, type, pivot):
        self.id = Shape._count()
        self.type = type
        self.pivot = pivot

    def __str__(self):
        return "ID: {} Type: {} Pivot {} Factor".format(
            self.id, self.type, self.pivot, self.neighbours_field_factor)
