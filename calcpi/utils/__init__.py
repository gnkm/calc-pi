from decimal import Decimal, ROUND_HALF_UP
import textwrap
from typing import Any, List

from mpmath import (
    mpf,
    nstr,
)


def round(num: float, digits: int) -> float:
    """Round the number to the digits decimal place.

    Args:
        num (float): rounded number
        digits (int): digits

    Returns:
        float: rounded number
    """
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
    print(v)


def format_pi(pi: mpf, accuracy: int, is_separated: bool = False, grouped_digit: int = 10, sep: str = ' ') -> str:
    """Return formated string.

    Args:
        pi (mpf): Pi
        accuracy (int): displayed digit
        is_separated (bool, optional): if True, return separated str. Defaults to False.
        grouped_digit (int, optional): grouped_digit. Defaults to 10.
        sep (str, optional): separator string. Defaults to ' '.

    Returns:
        str: formated string
    """
    pi_str: str = nstr(pi, n=accuracy)

    if not is_separated:
        return pi_str

    integer_and_fractional: List[str] = pi_str.split('.')
    integer: str = integer_and_fractional[0]
    fractional: str = integer_and_fractional[1]

    separated_fractional: str = ''
    for i, letter in enumerate(fractional):
        if i == 0:
            separated_fractional += letter
        elif i % grouped_digit == 0:
            separated_fractional += sep + letter
        else:
            separated_fractional += letter

    return textwrap.dedent(
        f'''\
        {integer}.
        {separated_fractional}\
        '''
    ).strip(' ')
