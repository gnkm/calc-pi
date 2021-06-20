"""Utility functions.
"""


import textwrap
from typing import List

from mpmath import (
    mpf,
    nstr,
)


def format_pi(pi: mpf, accuracy: int, is_separated: bool = False, grouped_digit: int = 10, sep: str = ' ') -> str:  # pylint: disable=invalid-name,line-too-long
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
    pi_str: str = nstr(pi, n=accuracy)  # pylint: disable=invalid-name

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
