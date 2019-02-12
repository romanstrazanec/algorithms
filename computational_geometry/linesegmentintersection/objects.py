class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x},{self.y})"

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  @staticmethod
  def distance(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

  def is_between(self, a, b):
    return Point.distance(a, self) + Point.distance(self, b) == Point.distance(a, b)


class LineSegment:
  def __init__(self, endpoints: list=None, start: Point=Point(), end: Point=Point()):
    if endpoints:
      self.endpoints = endpoints
    else:
      self.endpoints = [start, end]

  def __str__(self):
    return f"[{self.endpoints[0]}-{self.endpoints[1]}]"
    