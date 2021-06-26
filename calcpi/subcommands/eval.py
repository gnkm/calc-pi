"""Define args of eval subcommand.
"""


import argparse
import sys
from typing import List

import mpmath

from calcpi.subcommands.calc import calc

from calcpi import ALGORITHMS
from calcpi import print_prettify  # noqa: F401  # pylint: disable=unused-import
from calcpi import utils


SUBCOMMAND_NAME: str = 'eval'
ALIASES: List[str] = ['evaluate']

ACTUAL_PI_DIGIT: int = 1_000
ERROR_ACCRACY: int = 2


def define_args(subparsers):
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

    parser.set_defaults(handler=subcommand)

    return parser


def evaluate(algorithm: str, accuracy: int) -> mpmath.mpf:
    """Retrun Logarithm of the error between calculated pi and actural one.

    Args:
        algorithm (str): algorithm by which pi is calcurated
        accuracy (int): accuracy of calculated pi

    Returns:
        mpmath.mpf: logarithms or error of calculated pi and actual one
    """
    actual_pi: mpmath.mpf = calc('actual', ACTUAL_PI_DIGIT)
    compared_pi: mpmath.mpf = calc(algorithm, accuracy)
    subtraction: mpmath.mpf = mpmath.fsub(actual_pi, compared_pi)
    mpmath.mp.dps = ERROR_ACCRACY
    return - mpmath.log10(subtraction)


def subcommand(args: argparse.Namespace) -> None:
    # pylint: disable=missing-function-docstring
    err: mpmath.mpf = evaluate(args.algorithm, args.accuracy)
    formated_err: str = utils.format_pi(err, args.accuracy)
    sys.stdout.write(formated_err)
