from typing import List, Optional

from objects.linesegment import LineSegment
from objects.point import Point
from structures.avltree import AVLTree


def find_intersections_slow(line_segments: List[LineSegment]) -> List[Point]:
    result = set()
    for i in range(len(line_segments)):
        for ls in line_segments[i + 1:]:
            intersection = LineSegment.intersection(ls, line_segments[i])
            if intersection:
                result.add((intersection.x, intersection.y))
    return [Point.from_iter(i) for i in result]


def _sweep_line_x_intersection(y, ls: LineSegment):
    """x = (x1*(y2-y) + x2*(y-y1)) / (y2-y1)"""
    y1 = ls.endpoints[0].y
    y2 = ls.endpoints[1].y
    x1 = ls.endpoints[0].x
    if y1 == y2:
        return x1
    x2 = ls.endpoints[1].x
    return (x1 * (y2 - y) + x2 * (y - y1)) / (y2 - y1)


def _rot90ccw(ls: LineSegment) -> LineSegment:
    """Rotate line segment counter clockwise"""
    p1, p2 = ls.endpoints
    return LineSegment([Point(-p1.y, p1.x), Point(-p2.y, p2.x)])


def _ls_lt(l1: LineSegment, l2: LineSegment, y) -> bool:
    """__lt__ for line segments where y is the position of the sweep line"""
    x1 = _sweep_line_x_intersection(y, l1)
    x2 = _sweep_line_x_intersection(y, l2)
    if x1 == x2:
        # rotate the line segments counter clockwise and compare the slopes
        return _rot90ccw(l1).slope < _rot90ccw(l2).slope
    return x1 < x2


def _find_new_event(sl: LineSegment, sr: LineSegment, p: Point, q: AVLTree) -> Optional[Point]:
    """Finds new event point below the sweep line (point p)"""
    ip = LineSegment.intersection(sl, sr)
    # ip > p => intersection point is below the sweep line or on it and to the right of the point p
    if ip and ip > p and ip not in q:
        q.put(ip, [])
        return ip


def find_intersections(line_segments: List[LineSegment]) -> List[Point]:
    # save these functions so they can be returned back at the end
    p_lt, ls_lt = Point.__lt__, LineSegment.__lt__

    # define order for points, where smaller point is higher and more left
    Point.__lt__ = lambda p1, p2: p1.x < p2.x if p1.y == p2.y else p1.y > p2.y

    q = AVLTree()  # event queue where event points are stored and the first one is the smallest one
    result = []  # where the result intersection points go

    for line_segment in line_segments:
        line_segment.endpoints.sort()  # sort the endpoints so the first is always upper
        q.append(line_segment.endpoints[0], line_segment)  # store line segment with its upper point

        # save lower endpoint
        if line_segment.endpoints[1] not in q:
            q.put(line_segment.endpoints[1], [])  # create new entry if does not already exist

    status = AVLTree()  # status structure of the sweep line
    while len(q) > 0:
        event_point = q.min  # a TreeNode with point as the key

        u = event_point.value  # list of line segments starting at the event point
        l = []  # line segments whose lower endpoint is the event point
        c = []  # line segments which contain the event point in its interior
        for elem in status:  # yield the TreeNode element with line segment as the key
            if event_point.key == elem.key.endpoints[1]:
                l.append(elem)
            elif event_point.key in elem.key:
                c.append(elem)

        # if more than one of these line segments contain this event point, it belongs to the result
        if len(u) + len(l) + len(c) > 1:
            result.append(event_point.key)

        # delete the l and c line_segments from status
        for line_segment in (node.key for node in l + c):
            status.delete(line_segment)

        # every time the event point is updated, set __lt__ method to the current sweep line position
        LineSegment.__lt__ = lambda l1, l2: _ls_lt(l1, l2, event_point.key.y)

        # sorted u and c, if any then the first line segment in the list will be the leftmost line segment in status,
        # and the last will be the rightmost line segment in the status
        uc = sorted(u + [i.key for i in c])
        if len(uc) == 0:  # if it's only lower point
            # create a temporary LineSegment in the status with the event point as both endpoints
            # so it can check and then access left and right neighbour of the point
            temp = status.put(LineSegment(start=event_point.key, end=event_point.key), None)
            if temp.predecessor and temp.successor:
                # check whether its neighbours intersect
                _find_new_event(temp.predecessor.key, temp.successor.key, event_point.key, q)
            status.delete(temp)  # delete the temporary node
        else:
            # add new u segments and segments containing the event point back to the status
            for line_segment in uc:
                status.put(line_segment, None)

            s1 = status.get(uc[0])  # get the node pointer from the status of the leftmost segment
            sl = s1.predecessor
            if sl:  # if it has left neighbour
                # check whether the new leftmost segment and its left neighbour intersect
                _find_new_event(sl.key, s1.key, event_point.key, q)
            s2 = status.get(uc[-1])  # get the node pointer from the status of the rightmost segment
            sr = s2.successor
            if sr:  # if it has right neighbour
                # check whether the new rightmost segment and its right neighbour intersect
                _find_new_event(sr.key, s2.key, event_point.key, q)

        q.delete(event_point)  # delete the event point from event queue and continue the process

    # don't forget to return the __lt__ functions back to the classes
    Point.__lt__ = p_lt
    LineSegment.__lt__ = p_lt
    return result
