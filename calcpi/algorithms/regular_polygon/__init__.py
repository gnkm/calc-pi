"""Find the pi using the perimeter of a regular polygon inscribed in a circle.
"""
import math
from mpmath import (
    cos,
    mp,
    sqrt,
    radians,
)


def pi(accuracy: int) -> float:
    mp.dps = max(5, round(math.sqrt(accuracy)))

    return 1 / 2 * accuracy * sqrt(
        2 - 2 * cos(radians(360 / accuracy))
    )
