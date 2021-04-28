"""Calcurate pi with Gauss–Legendre algorithm.

cf. https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm
"""

import math
from typing import Tuple

# initial values
INIT_A: float = 1
INIT_B: float = 1 / math.sqrt(2)
INIT_T: float = 1 / 4
INIT_P: float = 1


def pi(accuracy: int) -> float:
    iter_num: int = int(math.log2(accuracy))
    a, b, t, _, _ = _variables(INIT_A, INIT_B, INIT_T, INIT_P, iter_num)
    return (a + b) ** 2 / (4 * t)


def _variables(a_n: float, b_n: float, t_n: float, p_n: float, iter_num: int) -> Tuple[float]:
    if iter_num <= 0:
        return a_n, b_n, t_n, p_n, iter_num

    a_n_plus_1: float = (a_n + b_n) / 2
    b_n_plus_1: float = math.sqrt(a_n * b_n)
    t_n_plus_1: float = t_n - p_n * (a_n - a_n_plus_1) ** 2
    p_n_plus_1: float = 2 * p_n

    return _variables(a_n_plus_1, b_n_plus_1, t_n_plus_1, p_n_plus_1, iter_num - 1)
