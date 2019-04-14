from typing import List, Union

from objects.point import Point


class LineSegment:
    def __init__(self, endpoints: List[Point] = None, start: Point = Point(), end: Point = Point()):
        if endpoints:  # two points given in a list
            self.endpoints = sorted(endpoints[:2])
        else:  # given start and end point
            self.endpoints = sorted([start, end])

    def __str__(self):
        return f"[{self.endpoints[0]}-{self.endpoints[1]}]"

    def __contains__(self, point: Point):
        return point.is_between(*self.endpoints)

    def __eq__(self, other):
        return self.endpoints == other.endpoints

    def __lt__(self, other):
        return self.length() < other.length()

    def length(self) -> float:
        return Point.distance(*self.endpoints)

    @staticmethod
    def intersection(l1, l2) -> Union[Point, None]:
        p1, p2 = l1.endpoints
        p3, p4 = l2.endpoints
        t1 = (p1.x - p3.x) * (p3.y - p4.y) - (p1.y - p3.y) * (p3.x - p4.x)
        t2 = (p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x)
        if t1 > t2 or t1 * t2 < 0:
            return None
        t = t1 / t2
        return Point(p1.x + t * (p2.x - p1.x), p1.y + t * (p2.y - p1.y))
