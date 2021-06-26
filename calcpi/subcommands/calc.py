"""Define args of calc subcommand.
"""


import argparse
import sys
from typing import List

import mpmath

from calcpi.algorithms import actual  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import gauss_legendre  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import monte_carlo  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import regular_polygon as polygon  # noqa: F401  # pylint: disable=unused-import

from calcpi import ALGORITHMS

from calcpi import print_prettify  # noqa: F401  # pylint: disable=unused-import
from calcpi import utils


SUBCOMMAND_NAME: str = 'calc'
ALIASES: List[str] = []


def define_args(subparsers):
    """Define subcommand args.

    Args:
        subparsers not set args

    Returns:
        subparsers set args
    """
    parser = subparsers.add_parser(SUBCOMMAND_NAME, aliases=ALIASES)
    parser.add_argument(
        'algorithm',
        help='Algorithm by which pi is calcurated',
        choices=ALGORITHMS,
    )
    parser.add_argument(
        '--accuracy',
        default=10,
        type=int,
        help='accuracy',
    )
    parser.add_argument(
        '-l',
        '--list',
        help='show algorithms list',
    )
    parser.add_argument(
        '-s',
        '--separated',
        action='store_true',
        help='show separated number',
    )
    parser.add_argument(
        '--grouped_digit',
        default=10,
        type=int,
        help='number of digits to be summarized when displaying',
    )
    parser.set_defaults(handler=subcommand)

    return subparsers


def calc(algorithm: str, accuracy: int) -> mpmath.mpf:
    """Return Pi.

    Args:
        accuracy (int): accuracy
        algorithm (str): algorithm by which pi is calcurated

    Returns:
        mpmath.mpf: Pi value
    """
    pi: mpmath.mpf = globals()[algorithm].pi(accuracy)  # pylint: disable=invalid-name
    return pi


def subcommand(args: argparse.Namespace) -> None:
    # pylint: disable=missing-function-docstring
    pi: mpmath.mpf = calc(args.algorithm,  args.accuracy)  # pylint: disable=invalid-name
    formated_pi: str = utils.format_pi(pi, args.accuracy, args.separated)
    sys.stdout.write(formated_pi)
