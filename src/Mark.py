from functools import reduce
from math import sqrt


class Mark:

    def __init__(self, drawing_manager):
        self.figure_pivots = drawing_manager.pivots

    @staticmethod
    def count_distance_between_points(p1, p2):
        xx = p1[0] - p2[0]
        yy = p1[1] - p2[1]
        return sqrt(xx * xx + yy * yy)

    @staticmethod
    def count_circuit(points):
        points.append(points[0])
        circuit = 0
        for first, second in zip(points, points[1:]):
            circuit += Mark.count_distance_between_points(first, second)
        return circuit

    @staticmethod
    def convex_hull_graham(points):

        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]), 0)

        def _keep_left(hull, r):
            while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
                hull.pop()
            if not len(hull) or hull[-1] != r:
                hull.append(r)
            return hull

        points = sorted(points)
        l = reduce(_keep_left, points, [])
        u = reduce(_keep_left, reversed(points), [])
        return l.extend(u[i] for i in range(1, len(u) - 1)) or l

    def count_mark_of_structure(self):
        points = self.convex_hull_graham(self.figure_pivots)
        circuit = self.count_circuit(points)
        mark = circuit / len(self.figure_pivots)
        print(mark)
        return str(round(mark))
