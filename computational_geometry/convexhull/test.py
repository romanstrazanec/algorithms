import matplotlib.pyplot as plt
from random import random
from convexhull import convexhull


def showpoints(points, **kwargs):
    """Plot given points"""
    return plt.scatter([p[0] for p in points], [p[1] for p in points], **kwargs)


def showline(points, **kwargs):
    """Plot the line through the given points"""
    return plt.plot([p[0] for p in points], [p[1] for p in points], **kwargs)


def printpoints(points):
    """Print points to the console"""
    for i, p in enumerate(points):
        print(p, end="\n" if i % 4 == 3 else ", ")


def randp(r): return random() * r - r / 2, random() * r - r / 2  # random point


# convex hull for hard coded points
points = [(3, 0), (8, 0), (5, 1), (1, 2),
          (0, 3), (4, 3), (8, 4), (10, 4),
          (2, 5), (6, 5), (4, 6), (9, 7),
          (1, 8), (5, 8), (7, 9), (3, 10)]

expected_result = [(0, 3), (1, 8), (3, 10), (7, 9), (9, 7), (10, 4), (8, 0), (3, 0), (0, 3)]

ch = convexhull(points)
assert expected_result == ch

# display the result
showpoints(points)
showline(ch, lw=.4, c='r')
plt.show()
# plt.savefig("CH.png")
# plt.clf()

# convex hull for random points
points = [randp(100) for _ in range(100)]

ch = convexhull(points)
showpoints(points)
showline(ch, lw=.4, c='r')
plt.show()
# plt.savefig("random_CH.png")
