import matplotlib.pyplot as plt
from random import random
from convexhull import convexhull
from point import Point


def showpoints(points, **kwargs):
    return plt.scatter([p.x for p in points], [p.y for p in points], **kwargs)


def showline(points, **kwargs):
    return plt.plot([p.x for p in points], [p.y for p in points], **kwargs)


def printpoints(points):
    for i, p in enumerate(points):
        print(p, end="\n" if i % 4 == 3 else ", ")


points = [Point(3, 0), Point(8, 0), Point(5, 1), Point(1, 2),
          Point(0, 3), Point(4, 3), Point(8, 4), Point(10, 4),
          Point(2, 5), Point(6, 5), Point(4, 6), Point(9, 7),
          Point(1, 8), Point(5, 8), Point(7, 9), Point(3, 10),
          ]

ch = convexhull(points)
showpoints(points)
showline(ch, lw=.4, c='r')
plt.savefig("CH.png")
plt.clf()

points.clear()
for i in range(20):
    points.append(Point(random()*10 - 5, random()*10 - 5))

ch = convexhull(points)
showpoints(points)
showline(ch, lw=.4, c='r')
plt.savefig("random_CH.png")
