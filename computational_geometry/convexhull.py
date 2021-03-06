from typing import List, Union, Tuple

from objects.point import Point


def _is_right_turn(p_start: Point, p_middle: Point, p_end: Point) -> bool:
    """Checks if the given points make a right turn"""
    return (p_start.x * (p_end.y - p_middle.y) + p_middle.x * (p_start.y - p_end.y)
            + p_end.x * (p_middle.y - p_start.y)) > 0


def convex_hull(points: List[Union[Tuple[float, float], List[float], Point]]) -> List[Point]:
    """For given list of points return its convex hull"""
    _at = (tuple, list, Point)  # allowed types
    points = [Point.from_iter(i) for i in points if type(i) in _at]  # converts to points

    points.sort(key=lambda p: p.x)  # sort points by x axis
    l_upper = [points[0], points[1]]  # add two leftmost points to L(upper) set

    for i in range(2, len(points)):  # for all other points
        l_upper.append(points[i])  # add the next point to L set

        # test the last three points in L
        while len(l_upper) > 2 and not _is_right_turn(l_upper[-3], l_upper[-2], l_upper[-1]):
            # remove the middle of tested three points when they don't make right turn
            l_upper.pop(-2)

    l_lower = [points[-1], points[-2]]  # L(lower) begins with the two rightmost points
    # apply the same algorithm for reversed values
    for i in reversed(range(len(points) - 3)):
        l_lower.append(points[i])
        while len(l_lower) > 2 and not _is_right_turn(l_lower[-3], l_lower[-2], l_lower[-1]):
            l_lower.pop(-2)

    # remove the first from lower L as it is the same as the last in the upper L
    # append lower to upper L
    return l_upper + l_lower[1:]
