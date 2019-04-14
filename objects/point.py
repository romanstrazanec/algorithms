from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        """Initialize point with default coords set to the origin"""
        self.x, self.y = x, y

    def __str__(self):
        """(x,y)"""
        return f"({self.x:g},{self.y:g})"

    def __getitem__(self, i):
        """Makes Point coords accessible by indexing"""
        return {0: self.x, 1: self.y}.get(i, None)

    def __eq__(self, other):
        """Equality of points"""
        return self[0] == other[0] and self[1] == other[1]

    def __lt__(self, other):
        """Smaller point is closer to the origin"""
        return sqrt(self.x * self.x + self.y * self.y) < sqrt(other.x * other.x + other.y * other.y)

    @staticmethod
    def distance(a, b) -> float:
        return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    @classmethod
    def from_iter(cls, tpl):
        """Create instance of point out of list, tuple or map with keys 0, 1"""
        return tpl if type(tpl) is cls else cls(tpl[0], tpl[1])

    def is_between(self, a, b):
        return Point.distance(a, self) + Point.distance(self, b) == Point.distance(a, b)
