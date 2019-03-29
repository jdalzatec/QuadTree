from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

def add(self, other):
    return Point(self.x + other.x, self.y + other.y)

Point.__add__ = add