from DrawingManager import DrawingManager
from itertools import repeat


class MultipleDrawingManager(DrawingManager):
    def prepare_new_random_figure(self):
        for f in repeat(super().prepare_new_random_figure, 15): f()
