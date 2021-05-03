import mpmath


def pi(accuracy: int) -> float:
    mpmath.mp.dps = accuracy
    return +mpmath.pi
