import mpmath


def pi(accuracy: int) -> mpmath.mpf:
    mpmath.mp.dps = accuracy
    return +mpmath.pi
