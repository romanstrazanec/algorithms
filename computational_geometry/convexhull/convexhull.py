from geometric_objects.point import Point
from sys import float_info


def _derivation(p1: Point, p2: Point):
    """Returns the derivation between two points"""
    dy = p2.y - p1.y  # difference between y values
    # dx = p2.x - p1.x # difference between x values
    try:
        return dy/(p2.x - p1.x)
    except ZeroDivisionError:  # x values could be the same resulting in 0 division
        return dy/float_info.epsilon  # divide by the smallest possible value


def _is_rightturn(points: list):
    """Checks if the first three given points list is a right turn"""
    return _derivation(points[0], points[1]) > _derivation(points[0], points[2])


def convexhull(ps: list):
    """For given list of points return its convex hull"""
    at = (tuple, list, Point)  # allowed types
    ps = [Point.from_iter(i) for i in ps if type(i) in at]

    ps.sort(key=lambda p: p.x)  # sort points by x axis
    Lupper = [ps[0], ps[1]]  # add two leftmost points to L(upper) set

    for i in range(2, len(ps)):  # for all other points
        Lupper.append(ps[i])  # add the next point to L set

        # test the last three points in L
        while len(Lupper) > 2 and not _is_rightturn(Lupper[-3:]):
            # remove the middle of tested three points when they don't make rightturn
            Lupper.pop(-2)

    Llower = [ps[-1], ps[-2]]  # L(lower) begins with the two rightmost points
    # apply the same algorithm for reversed values
    for i in reversed(range(len(ps) - 3)):
        Llower.append(ps[i])
        while len(Llower) > 2 and not _is_rightturn(Llower[-3:]):
            Llower.pop(-2)

    # remove the first from lower L as it is the same as the last in the upper L
    # append lower to upper L
    return Lupper + Llower[1:]
