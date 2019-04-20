import matplotlib.pyplot as plt

from findintersections import AVLTree
from objects.linesegment import LineSegment
from objects.point import Point


def sweep_line_x_intersection(y, ls):
    """x = (x1*(y2-y) + x2*(y-y1)) / (y2-y1)"""
    y1 = ls.endpoints[0].y
    y2 = ls.endpoints[1].y
    x1 = ls.endpoints[0].x
    if y1 == y2:
        return x1
    x2 = ls.endpoints[1].x
    return (x1 * (y2 - y) + x2 * (y - y1)) / (y2 - y1)


def line_segment__lt_(l1, l2) -> bool:
    if l1.endpoints[0].x == l2.endpoints[0].x:
        return l1.endpoints[1].x < l2.endpoints[1].x
    return l1.endpoints[0].x < l2.endpoints[0].x


def plt_line_segment(ls: LineSegment, **kwargs):
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
# plt_line_segment(l1)
# plt_line_segment(l2)
# plt_line_segment(sl, c='k', lw=.3)
# print(p)
# if p:
#     plt.scatter(p.x, p.y)
# plt.show()

line_segments = [LineSegment([Point(1, 5), Point(2, 3)]), LineSegment([Point(3, 4), Point(2, 2)]),
                 LineSegment([Point(2, 4), Point(3, 2)]), LineSegment([Point(3, 6), Point(3, 4)]),
                 LineSegment([Point(2, 4), Point(1, 1)])]

# for i in line_segments:
#     plt_line_segment(i)
# plt.show()

q = AVLTree()
Point.__lt__ = lambda p1, p2: p1.x < p2.x if p1.y == p2.y else p1.y > p2.y

for line_segment in line_segments:
    line_segment.endpoints.sort()
    q.append(line_segment.endpoints[0], line_segment)

    if line_segment.endpoints[1] not in q:
        q.put(line_segment.endpoints[1], [])

print("Event Q:")
print(q)
print()

status = AVLTree()
while len(q) > 0:
    event_point = q.min
    print("=" * 15)
    print("EVENT POINT ", event_point.key)

    u = event_point.value
    l = []
    c = []
    for elem in status:
        line_segment = elem.key
        if event_point.key == line_segment.endpoints[1]:
            l.append(line_segment)
        elif event_point.key in line_segment:
            c.append(line_segment)
    print("u ", u)
    print("l ", l)
    print("c ", c)

    if len(u) + len(l) + len(c) > 1:
        print(event_point.key, " is intersection")

    for line_segment in l + c:
        del status[line_segment]

    def ls_lt(l1, l2, y):
        x1 = sweep_line_x_intersection(y, l1)
        x2 = sweep_line_x_intersection(y, l2)
        if x1 == x2:
            return l1.slope < l2.slope
        return x1 < x2

    LineSegment.__lt__ = lambda l1, l2: ls_lt(l1, l2, event_point.key.y)

    for line_segment in u + c:
        status.put(line_segment, None)

    print("SWEEP LINE STATUS:")
    print(status)
    print()

    del q[event_point.key]
