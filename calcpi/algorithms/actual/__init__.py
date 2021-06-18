"""Return actual Pi value."""


import mpmath


def pi(accuracy: int) -> mpmath.mpf:
    """Return actual Pi value.

    Args:
        accuracy (int): number of digits

    Returns:
        mpmath.mpf: Pi value
    """
    mpmath.mp.dps = accuracy
    return +mpmath.pi
