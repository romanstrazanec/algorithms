from typing import List

from objects.linesegment import LineSegment
from objects.point import Point
from structures.avltree import AVLTree
from structures.treenode import TreeNode


def _point_order(p1: Point, p2: Point):
    if p1.y == p2.y:
        return p1.x < p2.x  # smaller point is more left
    return p1.y > p2.y  # smaller point is higher


# define order for points
Point.__lt__ = _point_order


def intersection(sl: LineSegment, sr: LineSegment, p: Point):
    """Returns intersection point of segments sl, sr below point p"""
    p1, p2 = sl.endpoints
    p3, p4 = sr.endpoints
    t1 = (p1.x - p3.x) * (p3.y - p4.y) - (p1.y - p3.y) * (p3.x - p4.x)
    t2 = (p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x)
    if t1 > t2 or t1 * t2 < 0:
        return None
    t = t1 / t2
    ip = Point(p1.x + t * (p2.x - p1.x), p1.y + t * (p2.y - p1.y))
    return ip if p < ip else None


def in_order(points):
    """Defines the order of points
    whereas the upmost leftmost point is the smallest
    returns true if given points are in order
    """
    p1, p2 = points[:2]
    return p2 > p1


def sortedep(ls: LineSegment):
    """Returns sorted endpoints of a given line segment"""
    if not in_order(ls.endpoints):
        return list(reversed(ls.endpoints))
    return ls.endpoints


def find_new_event(sl: LineSegment, sr: LineSegment, p: Point, q):
    ip = intersection(sl, sr, p)
    if ip:
        for ep, ls in q:
            if ep == ip:
                return
        q.add([ip, None])


def _handle_event_point(event_point: TreeNode) -> None:
    # U is the set of line segments whose upper endpoint is the event point
    # given end point is TreeNode where key is the actual point and the value is a list of line segments
    U = event_point.value


def find_intersections(line_segments: List[LineSegment]) -> List[Point]:
    q = AVLTree()  # event queue

    for line_segment in line_segments:
        # save upper endpoint with corresponding line segment
        if line_segment.endpoints[0] in q:
            # append line segment to the list
            # these line_segments start at the same point
            q[line_segment.endpoints[0]].append(line_segment)
        else:
            # create new entry
            q.put(line_segment.endpoints[0], [line_segment])

        # save lower endpoint
        if line_segment.endpoints[1] not in q:
            # create new entry if does not already exist
            q.put(line_segment.endpoints[1], [])

    t = AVLTree()  # status structure
    while q.length() > 0:
        point_to_handle = q.root.find_min()
        _handle_event_point()
        del q[q.root.key]
