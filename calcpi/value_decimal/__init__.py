from decimal import (
    Decimal,
    getcontext,
)
import math


def pi(accuracy: int) -> Decimal:
    """Return Pi.

    It's not good function.

    python -m calcpi value_decimal --accuracy 30
    => Decimal('3.141592653589793')
    => Expected output is 30 digits float

    python -m calcpi value_decimal --accuracy 3
    => Decimal('3.141592653589793')
    => Expected output is Decimal('3.14')

    Args:
        accuracy (int): accuracy

    Returns:
        Decimal: Pi
    """
    getcontext().prec = accuracy
    return Decimal(
        str(math.pi)
    )
