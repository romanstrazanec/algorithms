from typing import List

from objects.linesegment import LineSegment
from objects.point import Point
from structures.avltree import AVLTree
from structures.treenode import TreeNode

# define order for points, where smaller point is higher and more left
Point.__lt__ = lambda p1, p2: p1.x < p2.x if p1.y == p2.y else p1.y > p2.y


def _find_new_event(sl: LineSegment, sr: LineSegment, p: Point, q: AVLTree) -> None:
    """Finds new event point below the sweep line (point p)"""
    ip = LineSegment.intersection(sl, sr)
    # ip > p => intersection point is below the sweep line or on it and to the right of the point p
    if ip and ip > p and ip not in q:
        q.put(ip, [])


def _handle_event_point(event_point: TreeNode, status: AVLTree) -> None:
    # u is the set of line segments whose upper endpoint is the event point
    # given end point is TreeNode where key is the actual point and the value is a list of line segments
    u = event_point.value
    l = []  # line segments whose lower endpoint is the event point
    c = []  # line segments which contain the event point in its interior
    for line_segment in status:
        if event_point.key == line_segment[1]:
            l.append(line_segment)
        elif event_point.key in line_segment:
            c.append(line_segment)

    if len(u) + len(l) + len(c) > 1:
        pass

    # remove line segments in l and c from status
    for line_segment in l + c:
        del status[line_segment]

    # add line segments in u and c to status
    for line_segment in u + c:
        sweep_line = LineSegment(
            [Point(line_segment[0].x, event_point.key.y), Point(line_segment[1].x, event_point.key.y)])
        status.put(LineSegment.intersection(sweep_line, line_segment).x, line_segment)

    if len(u) + len(c) == 0:
        pass


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

    t = AVLTree()  # status structure of the sweep line
    while q.length() > 0:
        # point_to_handle is a TreeNode with point as the key
        # and list of line segments starting in this point as the value
        point_to_handle = q.root.find_min()
        _handle_event_point(point_to_handle, t)
        del q[q.root.key]
