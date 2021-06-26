"""Package for calcurating pi.
"""

from typing import List

from icecream import install

from calcpi.debug import print_prettify  # noqa: F401  # pylint: disable=unused-import


ALGORITHMS: List[str] = [
    'actual',
    'gauss_legendre',
    'monte_carlo',
    'polygon',
]

install()
