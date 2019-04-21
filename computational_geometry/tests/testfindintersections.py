from random import random

import matplotlib.pyplot as plt

from findintersections import _ls_lt, _find_new_event, find_intersections
from objects.linesegment import LineSegment
from objects.point import Point
from structures.avltree import AVLTree


def plt_line_segments(_lss, **kwargs):
    for _ls in _lss:
        x = [p.x for p in _ls.endpoints]
        y = [p.y for p in _ls.endpoints]
        plt.scatter(x, y, **kwargs)
        plt.plot(x, y, **kwargs)


def sweep_line(x1, x2, y):
    return LineSegment([Point(x1, y), Point(x2, y)])


def random_point(_r):
    return Point(random() * _r - _r / 2, random() * _r - _r / 2)


# test line segments
# line_segments = [LineSegment([Point(1, 5), Point(2, 3)]), LineSegment([Point(3, 4), Point(2, 2)]),
#                  LineSegment([Point(2, 4), Point(3, 2)]), LineSegment([Point(3, 6), Point(3, 4)]),
#                  LineSegment([Point(2, 4), Point(1, 1)])]

plot_process = True
r = 4  # range from -r to r
n = 10  # number of random points
line_segments = [LineSegment([random_point(r), random_point(r)]) for _ in range(n)]

# slow algorithm
intersections = set()
for i in range(len(line_segments)):
    for ls in line_segments[i + 1:]:
        intersection = LineSegment.intersection(ls, line_segments[i])
        if intersection:
            intersections.add((intersection.x, intersection.y))

# show lines with intersection points
plt_line_segments(line_segments)
plt.scatter([i[0] for i in intersections], [i[1] for i in intersections], c='k')
plt.title("Slow algorithm")
plt.show()

# start fast algorithm
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

result = []
status = AVLTree()
while len(q) > 0:
    event_point = q.min
    if plot_process:
        plt_line_segments([sweep_line(-r, r, event_point.key.y)], label="sweep line", c='lightgray')
    print("=" * 15)
    print("EVENT POINT ", event_point.key)

    u = event_point.value
    l = []
    c = []
    for elem in status:  # yield the TreeNode element with line segment as the key
        if event_point.key == elem.key.endpoints[1]:
            l.append(elem)
        elif event_point.key in elem.key:
            c.append(elem)
    print("u ", u)
    print("l ", [i.key for i in l])
    print("c ", [i.key for i in c])
    if plot_process:
        plt_line_segments(u, label="U", c='r')
        plt_line_segments([i.key for i in l], label="L", c='b')
        plt_line_segments([i.key for i in c], label="C", c='steelblue')

    if len(u) + len(l) + len(c) > 1:
        result.append(event_point.key)
        print(event_point.key, " IS INTERSECTION <--------------")

    for line_segment_node in l + c:
        status.delete(line_segment_node)

    LineSegment.__lt__ = lambda l1, l2: _ls_lt(l1, l2, event_point.key.y)

    uc = sorted(u + [i.key for i in c])
    if len(uc) == 0:
        temp = status.put(LineSegment(start=event_point.key, end=event_point.key), None)
        if temp.has_both_children():
            ne = _find_new_event(temp.predecessor.key, temp.successor.key, event_point.key, q)
            if plot_process and ne:
                plt.scatter(ne.x, ne.y, label='new event', c='k')
        status.delete(temp)
    else:
        for line_segment in uc:
            status.put(line_segment, None)
        s1 = status.get(uc[0])
        sl = s1.predecessor
        if sl:
            ne = _find_new_event(sl.key, s1.key, event_point.key, q)
            if plot_process and ne:
                plt.scatter(ne.x, ne.y, label='new event', c='k')
        s2 = status.get(uc[-1])
        sr = s2.successor
        if sr:
            ne = _find_new_event(sr.key, s2.key, event_point.key, q)
            if plot_process and ne:
                plt.scatter(ne.x, ne.y, label='new event', c='k')
    if plot_process:
        plt_line_segments([ls.key for ls in status], label="status", c='sandybrown', lw=.3)
        plt.legend()
        plt.title(f"Event point {event_point.key}")
        plt.show()
    print("SWEEP LINE STATUS:")
    print(status)
    print()

    del q[event_point.key]

plt_line_segments(line_segments)
plt.scatter([p.x for p in result], [p.y for p in result], c='k')
plt.title("Sweep line algorithm")
plt.show()

print("SLOW ALGORITHM")
print("Number of intersections:", len(intersections))
print(intersections)

print("\nSWEEP LINE ALGORITHM")
print("Number of intersections:", len(result))
print(result)

print("\nSWEEP LINE ALGORITHM (SOURCE)")
fi = find_intersections(line_segments)
print("Number of intersections:", len(fi))
print(fi)

# the current result and result from the slow algorithm and result from imported algorithm
assert sorted(result) == sorted([Point.from_iter(i) for i in intersections]) == sorted(fi)
