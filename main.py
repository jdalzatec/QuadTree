from matplotlib import pyplot
from matplotlib.patches import Rectangle
from QTree import QTree
from Point import Point
from Particle import Particle
import numpy


def get_tree(tree, lista):
    lista.append(tree)
    for ch in tree.children:
        if isinstance(ch, QTree):
            get_tree(ch, lista)

def main():
    N = 2000
    L = 10

    root = QTree(Point(0, 0), L, None)
    points = [Point(x, y) for x, y in numpy.random.uniform(0, L, size=(N, 2))]

    for p in points:
        root.insert_point(p)

    tree = []
    get_tree(root, tree)

    colors = pyplot.cm.jet(numpy.linspace(0, 1, len(tree)))

    pyplot.figure()
    for i, quad in enumerate(tree):
        print(len(quad.points), len(quad.children))
        rect = Rectangle(quad.position, quad.length, quad.length, facecolor=colors[i], zorder=-1, alpha=0.1, edgecolor="black")
        pyplot.gca().add_patch(rect)
        for x, y in quad.points:
            pyplot.plot(x, y, ".k", ms=1, zorder=100)


    pyplot.plot(*points[-1], "o", ms=10)
    pyplot.xlim(-0.5, L+0.5)
    pyplot.ylim(-0.5, L+0.5)
    pyplot.gca().set_aspect("equal")
    pyplot.tight_layout()
    pyplot.savefig("mientras.pdf")
    pyplot.close()


if __name__ == '__main__':
    main() 