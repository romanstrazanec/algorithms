import matplotlib.pyplot as plt
from findintersections import intersection
from objects import Point, LineSegment


def pltlinesegment(ls: LineSegment, **kwargs):
    x = [p.x for p in ls.endpoints]
    y = [p.y for p in ls.endpoints]
    plt.scatter(x, y, **kwargs)
    plt.plot(x, y, **kwargs)


def sweep_line(x1, x2, y):
    return LineSegment([Point(x1, y), Point(x2, y)])


l1 = LineSegment(start=Point(1, 1), end=Point(3, 3))
l2 = LineSegment(start=Point(3, 1), end=Point(1, 4))

sl = sweep_line(0, 4, 6)
p = intersection(l1, l2, sl.endpoints[0])

pltlinesegment(l1)
pltlinesegment(l2)
pltlinesegment(sl, c='k', lw=.3)
print(p)
if p:
  plt.scatter(p.x, p.y)
plt.show()