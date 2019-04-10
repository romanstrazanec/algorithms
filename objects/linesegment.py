from objects import Point


class LineSegment:
    def __init__(self, endpoints: list = None, start: Point = Point(), end: Point = Point()):
        if endpoints:  # two points given in a list
            self.endpoints = sorted(endpoints[:2])
        else:  # given start and end point
            self.endpoints = sorted([start, end])

    def __str__(self):
        return f"[{self.endpoints[0]}-{self.endpoints[1]}]"
