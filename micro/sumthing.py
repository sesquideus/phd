import itertools
import functools
import operator
import numpy as np

def combo(maximum, count, thesum):
    return list(filter(lambda x: sum(x) == thesum, itertools.combinations(range(1, maximum + 1), count)))

def intersect(x, y, inter):
    if inter is None:
        return True
    else:
        return len(set(x).intersection(set(y))) == inter


class Area():
    def __init__(self, limit, vertices, thesum):
        self.limit = limit
        self.sum = thesum
        self.vertices = vertices
        self.combinations = combo(limit, vertices, thesum)

    def __str__(self):
        return f"Area {self.limit} {self.vertices} {self.sum}"


class SumThing():
    def __init__(self, limit, areas, matrix):
        self.limit = limit
        self.areas = [Area(limit, *area) for area in areas]
        self.matrix = matrix

        self.possible = [(p,) for p in self.areas[0].combinations]

        for depth in range(1, len(self.areas)):
            self.new_possible = []
            for p in self.possible:
                for c in self.areas[depth].combinations:
                    if functools.reduce(operator.and_, map(lambda x: intersect(p[x], c, self.matrix[x][depth]), range(0, depth)), True):
                        self.new_possible.append((*p, c))

            self.possible = self.new_possible

        print(self.possible)

puzzle = SumThing(9,
    ((3, 6), (3, 8), (3, 11), (3, 14), (3, 16), (3, 20), (3, 22), (7, 28), (7, 29), (7, 40)
    (
        (   3, None, None, None, None, None, None, 1, 1, 1),
        (None,    3, None, None, None, None, None, 1, 1, 1),
        (None, None,    3, None, None, None, None, 1, 1, 1),
        (None, None, None,    3, None, None, None, 1, 1, 1),
        (None, None, None, None,    3, None, None, 1, 1, 1),
        (None, None, None, None, None,    3, None, 1, 1, 1),
        (None, None, None, None, None, None,    3, 1, 1, 1),
        (   1,    1,    1,    1,    1,    1,    1, 7, None, None),
        (   1,    1,    1,    1,    1,    1,    1, None, 7, None),
        (   1,    1,    1,    1,    1,    1,    1, None, None, 7),
    )
)
