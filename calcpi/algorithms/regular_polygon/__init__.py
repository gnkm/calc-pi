"""Find the pi using the perimeter of a regular polygon inscribed in a circle.
"""
import math
from mpmath import (
    cos,
    mp,
    mpf,
    sqrt,
    radians,
)


def pi(accuracy: int) -> mpf:  # pylint: disable=invalid-name
    """Return Pi gotten by Monte Carlo method.

    Args:
        accuracy (int): accuracy

    Returns:
        mpf: Pi
    """
    mp.dps = max(5, round(math.sqrt(accuracy)))

    return 1 / 2 * accuracy * sqrt(
        2 - 2 * cos(radians(360 / accuracy))
    )
