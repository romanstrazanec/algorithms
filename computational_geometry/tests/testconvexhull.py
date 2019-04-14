from random import random

import matplotlib.pyplot as plt

from computational_geometry.convexhull import convex_hull


def show_points(_points, **kwargs):
    """Plot given points"""
    return plt.scatter([p[0] for p in _points], [p[1] for p in _points], **kwargs)


def show_line(_points, **kwargs):
    """Plot the line through the given points"""
    return plt.plot([p[0] for p in _points], [p[1] for p in _points], **kwargs)


def print_points(_points):
    """Print points to the console"""
    for i, p in enumerate(_points):
        print(p, end="\n" if i % 4 == 3 else ", ")


def random_point(r):
    return random() * r - r / 2, random() * r - r / 2


if __name__ == '__main__':
    # convex hull for hard coded points
    points = [(3, 0), (8, 0), (5, 1), (1, 2),
              (0, 3), (4, 3), (8, 4), (10, 4),
              (2, 5), (6, 5), (4, 6), (9, 7),
              (1, 8), (5, 8), (7, 9), (3, 10)]

    expected_result = [(0, 3), (1, 8), (3, 10), (7, 9), (9, 7), (10, 4), (8, 0), (3, 0), (0, 3)]

    ch = convex_hull(points)
    assert expected_result == ch

    # display the result
    show_points(points)
    show_line(ch, lw=.4, c='r')
    plt.show()

    # convex hull for random points
    points = [random_point(100) for _ in range(10)]

    ch = convex_hull(points)
    show_points(points)
    show_line(ch, lw=.4, c='r')
    plt.show()

    # intersection of two convex hulls is convex
    points2 = [random_point(100) for _ in range(10)]
    show_points(points, s=.5)
    show_line(ch, lw=.5)
    show_points(points2, s=.5)
    show_line(convex_hull(points2), lw=.5)
    plt.show()
