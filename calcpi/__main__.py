"""Main script."""

import argparse
import sys
from typing import List

import mpmath

from calcpi.algorithms import actual  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import gauss_legendre  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import monte_carlo  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import regular_polygon as polygon  # noqa: F401  # pylint: disable=unused-import

from calcpi.subcommands import calc as sc_calc

from calcpi import print_prettify  # noqa: F401  # pylint: disable=unused-import
from calcpi import utils


ALGORITHMS: List[str] = [
    'actual',
    'gauss_legendre',
    'monte_carlo',
    'polygon',
]

ACTUAL_PI_DIGIT: int = 1_000
ERROR_ACCRACY: int = 2


def main():
    # pylint: disable=missing-function-docstring
    parser = argparse.ArgumentParser(
        description='Calcurates Pi',
        prog='python -m calcpi',
    )
    subparsers = parser.add_subparsers(prog='python -m calcpi')
    subparsers = sc_calc.define_args(subparsers)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

    sys.exit()


def subcommand_evaluate(args: argparse.Namespace) -> None:
    # pylint: disable=missing-function-docstring
    err: mpmath.mpf = evaluate(args.algorithm, args.accuracy)
    formated_err: str = utils.format_pi(err, args.accuracy)
    sys.stdout.write(formated_err)


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


def exec_subcommand() -> None:
    """Define command line args.
    """
    parser = argparse.ArgumentParser(description='Calcurate Pi')
    subparsers = parser.add_subparsers(
        prog='python -m calcpi',
    )

    # ===== evaluate subcommand =====
    parser_evaluate = subparsers.add_parser('evaluate')
    parser_evaluate.add_argument(
        'algorithm',
        help='Algorithm by which pi is calcurated',
        choices=ALGORITHMS,
    )
    parser_evaluate.add_argument(
        '--accuracy',
        default=10,
        type=int,
        help='accuracy',
    )
    parser_evaluate.set_defaults(handler=subcommand_evaluate)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
