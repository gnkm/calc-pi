"""Find the pi using the perimeter of a regular polygon inscribed in a circle.
"""
import math


def pi(accuracy: int) -> float:
    return 1 / 2 * accuracy * math.sqrt(
        2 - 2 * math.cos(math.radians(360 / accuracy))
    )
