"""Get pi with Monte Carlo simulation."""

import mpmath
import numpy as np

from calcpi import print_prettify  # noqa: F401  # pylint: disable=unused-import


def pi(accuracy: int) -> mpmath.mpf:  # pylint: disable=invalid-name
    """Return Pi gotten by Monte Carlo simulation.

    Args:
        accuracy (int): [description]

    Returns:
        mpmath.mpf: Pi
    """
    mpmath.mp.dps = accuracy
    points = np.random.uniform(size=(accuracy, 2))
    point_count = points.shape[0]
    distances = np.power(points[:, 0], 2) + np.power(points[:, 1], 2)
    inner_circle_point_count = np.count_nonzero(distances <= 1)
    return mpmath.mpf(4) * inner_circle_point_count / point_count
