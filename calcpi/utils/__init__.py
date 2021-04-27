from decimal import Decimal, ROUND_HALF_UP
import pprint
from typing import Any


def round(num: float, digits: int) -> float:
    minus_digits: float = - digits
    _digits: float = 10 ** minus_digits
    str_digits: str = str(_digits)
    return float(
        Decimal(str(num))
        .quantize(Decimal(str_digits), rounding=ROUND_HALF_UP)
    )


def display(v: Any) -> None:
    """Display var on STDOUT

    Args:
        v (Any): displayed arg
    """
    pprint.pprint(v)
