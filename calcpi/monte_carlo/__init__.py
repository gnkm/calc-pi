"""Get pi with Monte Carlo simulation."""

from mpmath import (
    mp,
    mpf,
)
import numpy as np

from calcpi import print_prettify  # noqa: F401  # pylint: disable=unused-import


def pi(accuracy: int) -> float:  # pylint: disable=invalid-name
    mp.dps = accuracy
    points = np.random.uniform(size=(accuracy, 2))
    point_count = points.shape[0]
    distances = np.power(points[:, 0], 2) + np.power(points[:, 1], 2)
    inner_circle_point_count = np.count_nonzero(distances <= 1)

    return mpf(4) * inner_circle_point_count / point_count
