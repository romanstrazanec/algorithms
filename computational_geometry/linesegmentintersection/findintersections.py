from objects.point import Point
from objects.linesegment import LineSegment
from structures.avltree import AVLTree


def intersection(sl: LineSegment, sr: LineSegment, p: Point):
    """Returns intersection point of segments sl, sr below point p"""
    p1, p2 = sl.endpoints
    p3, p4 = sr.endpoints
    t1 = (p1.x-p3.x)*(p3.y-p4.y)-(p1.y-p3.y)*(p3.x-p4.x)
    t2 = (p1.x-p2.x)*(p3.y-p4.y)-(p1.y-p2.y)*(p3.x-p4.x)
    if t1 > t2 or t1*t2 < 0:
        return None
    t = t1/t2
    ip = Point(p1.x + t*(p2.x-p1.x), p1.y + t*(p2.y-p1.y))
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


def find_new_event(sl: LineSegment, sr: LineSegment, p: Point, q: Queue):
    ip = intersection(sl, sr, p)
    if ip:
        for ep, ls in q:
            if ep == ip:
                return
        q.add([ip, None])


def handle_event_point(point: Point):
    # set of segments whose upper endpoint is given point
    U = set(ls for p, ls in q if p == point)


def find_intersections(linesegments):
    q = AVLTree()  # event queue

    for i, linesegment in enumerate(linesegments):
        # save upper endpoint with corresponding line segment
        q.put(linesegment.endpoints[0], linesegment)
        # save lower endpoint
        q.put(linesegment.endpoints[1], None)

    t = AVLTree()  # status structure
    while q.length() > 0:
        handle_event_point(q.root)
        q.remove(q.root)
