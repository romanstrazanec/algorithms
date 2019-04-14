import matplotlib.pyplot as plt

from findintersections import AVLTree
from objects.linesegment import LineSegment
from objects.point import Point


def pltlinesegment(ls: LineSegment, **kwargs):
    x = [p.x for p in ls.endpoints]
    y = [p.y for p in ls.endpoints]
    plt.scatter(x, y, **kwargs)
    plt.plot(x, y, **kwargs)


def sweep_line(x1, x2, y):
    return LineSegment([Point(x1, y), Point(x2, y)])


# l1 = LineSegment(start=Point(1, 1), end=Point(3, 3))
# l2 = LineSegment(start=Point(3, 1), end=Point(1, 4))
#
# sl = sweep_line(0, 4, 6)
# p = intersection(l1, l2, sl.endpoints[0])
#
# pltlinesegment(l1)
# pltlinesegment(l2)
# pltlinesegment(sl, c='k', lw=.3)
# print(p)
# if p:
#     plt.scatter(p.x, p.y)
# plt.show()

lss = [LineSegment([Point(1, 5), Point(2, 3)]), LineSegment([Point(3, 4), Point(2, 2)]),
       LineSegment([Point(2, 4), Point(3, 2)]), LineSegment([Point(3, 6), Point(3, 4)]),
       LineSegment([Point(2, 4), Point(1, 1)])]

a = AVLTree()

for ls in lss:
    if ls.endpoints[0] in a:
        a[ls.endpoints[0]].append(ls)
    else:
        a.put(ls.endpoints[0], [ls])
    if ls.endpoints[1] not in a:
        a.put(ls.endpoints[1], [])
    for i in a:
        print(i, a[i])
    print()
