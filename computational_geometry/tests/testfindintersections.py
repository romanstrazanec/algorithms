from random import random, randint

import matplotlib.pyplot as plt

from findintersections import _ls_lt, _find_new_event, find_intersections
from objects.linesegment import LineSegment
from objects.point import Point
from structures.avltree import AVLTree


def plt_line_segment(_ls, **kwargs):
    x = [p.x for p in _ls.endpoints]
    y = [p.y for p in _ls.endpoints]
    if 'label' not in kwargs:
        plt.scatter(x, y, **kwargs)
        plt.plot(x, y, label=str(_ls), **kwargs)
    else:
        plt.scatter(x, y, **kwargs)
        plt.plot(x, y, **kwargs)


def plt_line_segments(_lss, **kwargs):
    for _ls in _lss:
        plt_line_segment(_ls, **kwargs)


def sweep_line(x1, x2, y):
    return LineSegment([Point(x1, y), Point(x2, y)])


def random_point(_r):
    return Point(random() * _r - _r / 2, random() * _r - _r / 2)


def randint_point(_r):
    return Point(randint(-_r, _r), randint(-_r, _r))


legend = False
plot_process = False
r = 1  # range from -r to r
n = 20  # number of random segments

# test line segments
# line_segments = [LineSegment([Point(1, 5), Point(2, 3)]), LineSegment([Point(3, 4), Point(2, 2)]),
#                  LineSegment([Point(2, 4), Point(3, 2)]), LineSegment([Point(3, 6), Point(3, 4)]),
#                  LineSegment([Point(2, 4), Point(1, 1)])]

# failed tests
line_segments = [
    LineSegment([Point(-0.479532, 0.479277), Point(0.0329766, -0.320124)]),
    LineSegment([Point(-0.419874, 0.323043), Point(-0.0474568, 0.0768236)]),
    LineSegment([Point(-0.14408, 0.165792), Point(-0.0238416, -0.40193)]),
    LineSegment([Point(-0.0428549, 0.144741), Point(0.329162, 0.0863071)]),
    LineSegment([Point(0.444422, 0.119511), Point(-0.215631, -0.0739168)]),
    LineSegment([Point(0.0722771, 0.0903832), Point(0.319375, -0.308218)]),
]

# random line segments
# line_segments = [LineSegment([random_point(r), random_point(r)]) for _ in range(n)]

# random int line segments
# line_segments = [LineSegment([randint_point(r), randint_point(r)]) for _ in range(n)]

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
plt.axis([-r, r, -r, r])
if legend:
    plt.legend(fancybox=True, framealpha=0.3)
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
step = 1
while len(q) > 0:
    event_point = q.min
    if plot_process:
        plt_line_segments([sweep_line(-r, r, event_point.key.y)], label="sweep line", c='lightgray')
    print("=" * 30)
    print(step, "EVENT POINT ", event_point.key)

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
    # if plot_process:
    #     plt_line_segments(u, label="U", c='maroon', lw=.3)
    #     plt_line_segments([i.key for i in l], label="L", c='lightgreen', lw=.3)
    #     plt_line_segments([i.key for i in c], label="C", c='steelblue', lw=.3)
    #     if legend:
    #         plt.legend(fancybox=True, framealpha=0.3)
    #     plt.show()

    if len(u) + len(l) + len(c) > 1:
        result.append(event_point.key)
        print(event_point.key, " IS INTERSECTION <--------------")

    for line_segment_node in l + c:
        status.delete(line_segment_node)

    LineSegment.__lt__ = lambda l1, l2: _ls_lt(l1, l2, event_point.key.y)

    uc = sorted(u + c)
    if len(uc) == 0:
        temp = status.put(LineSegment(start=event_point.key, end=event_point.key), None)
        if temp.predecessor and temp.successor:
            ne = _find_new_event(temp.predecessor.key, temp.successor.key, event_point.key, q)
            if ne:
                print(ne, "added to Q <------")
                print("Event Q:")
                print(q)
                print()
                if plot_process:
                    plt.scatter(ne.x, ne.y, label='new event', c='k')
        status.delete(temp)
    else:
        for line_segment in uc:
            status.put(line_segment, None)
        s1 = status.get(uc[0])
        sl = s1.predecessor
        if sl:
            ne = _find_new_event(sl.key, s1.key, event_point.key, q)
            if ne:
                print(ne, "added to Q <------")
                print("Event Q:")
                print(q)
                print()
                if plot_process:
                    plt.scatter(ne.x, ne.y, label='new event', c='k')
        s2 = status.get(uc[-1])
        sr = s2.successor
        if sr:
            ne = _find_new_event(sr.key, s2.key, event_point.key, q)
            if ne:
                print(ne, "added to Q <------")
                print("Event Q:")
                print(q)
                print()
                if plot_process:
                    plt.scatter(ne.x, ne.y, label='new event', c='k')
    if plot_process:
        for i, ls in enumerate(status):
            plt_line_segment(ls.key, label=i, lw=.3)
        for elem in q:
            if elem.key == event_point.key:
                plt.scatter(event_point.key.x, event_point.key.y, c='b')
            else:
                plt.scatter(elem.key.x, elem.key.y, c='r', alpha=.5)
            plt_line_segments(elem.value, c='k', label='not in T yet', alpha=0.2)
        if legend:
            plt.legend(fancybox=True, framealpha=0.3)
        plt.title(f"{step} Event point {event_point.key}")
        plt.axis([-r, r, -r, r])
        plt.show()
    print("SWEEP LINE STATUS:")
    print("Size:", len(status))
    print(status)
    print()

    del q[event_point.key]
    step += 1

plt_line_segments(line_segments)
plt.scatter([p.x for p in result], [p.y for p in result], c='k')
plt.title("Sweep line algorithm")
plt.axis([-r, r, -r, r])
if legend:
    plt.legend(fancybox=True, framealpha=0.3)
plt.show()

print("=============\nSLOW ALGORITHM")
intersections = [Point.from_iter(i) for i in intersections]
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
assert sorted(result) == sorted(intersections) == sorted(fi)
