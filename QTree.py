from Point import Point


class QTree:
    def __init__(self, position, length, parent):
        self.position = position
        self.length = length
        self.parent = parent
        self.children = []
        self.points = []

    def add_quadrature(self):
        length = self.length
        a = QTree(self.position + Point(0, length / 2), length / 2, self)
        b = QTree(self.position + Point(length / 2, length / 2), length / 2, self)
        c = QTree(self.position + Point(0, 0), length / 2, self)
        d = QTree(self.position + Point(length / 2, 0), length / 2, self)
        self.children = [a, b, c, d]

    def contains(self, point):
        x, y = point
        xg, yg = self.position
        return (xg < x <= xg + self.length) and (yg < y <= yg + self.length)

    def __contains__(self, points):
        return points in self.points

    def insert_point(self, point):
        if len(self.points) == 0:
            if len(self.children) == 0:
                self.points.append(point)
            else:
                for tree in self.children:
                    if tree.contains(point):
                        tree.insert_point(point)
        else:
            self.add_quadrature()
            oldPoint = self.points.pop()
            for tree in self.children:
                if tree.contains(oldPoint):
                    tree.insert_point(oldPoint)

            for tree in self.children:
                if tree.contains(point):
                    tree.insert_point(point)
