"""Calcurate pi with Gauss–Legendre algorithm.

cf. https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm
"""

import math
from mpmath import (
    mp,
    mpf,
    sqrt,
)
from typing import Tuple

# initial values
INIT_A: float = 1
INIT_B: float = 1 / math.sqrt(2)
INIT_T: float = 1 / 4
INIT_P: float = 1


def pi(accuracy: int) -> float:
    mp.dps = accuracy
    iter_num: int = int(math.log2(accuracy))
    a, b, t, _, _ = _variables(
        mpf(INIT_A),
        mpf(INIT_B),
        mpf(INIT_T),
        mpf(INIT_P),
        iter_num
    )
    return (a + b) ** 2 / (4 * t)


def _variables(a_n: mpf, b_n: mpf, t_n: mpf, p_n: mpf, iter_num: int) -> Tuple[mpf]:
    if iter_num <= 0:
        return a_n, b_n, t_n, p_n, iter_num

    a_n_plus_1: mpf = (a_n + b_n) / 2
    b_n_plus_1: mpf = sqrt(a_n * b_n)
    t_n_plus_1: mpf = t_n - p_n * (a_n - a_n_plus_1) ** 2
    p_n_plus_1: mpf = 2 * p_n

    return _variables(a_n_plus_1, b_n_plus_1, t_n_plus_1, p_n_plus_1, iter_num - 1)
