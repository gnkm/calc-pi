"""Main script."""

import argparse
import sys
from typing import List

import mpmath

from calcpi.algorithms import actual  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import gauss_legendre  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import monte_carlo  # noqa: F401  # pylint: disable=unused-import
from calcpi.algorithms import regular_polygon as polygon  # noqa: F401  # pylint: disable=unused-import

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
    exec_subcommand()
    sys.exit()


def subcommand_calc(args: argparse.Namespace) -> None:
    # pylint: disable=missing-function-docstring
    pi: mpmath.mpf = calc(args.algorithm,  args.accuracy)  # pylint: disable=invalid-name
    formated_pi: str = utils.format_pi(pi, args.accuracy, args.separated)
    sys.stdout.write(formated_pi)


def subcommand_evaluate(args: argparse.Namespace) -> None:
    # pylint: disable=missing-function-docstring
    err: mpmath.mpf = evaluate(args.algorithm, args.accuracy)
    formated_err: str = utils.format_pi(err, args.accuracy)
    sys.stdout.write(formated_err)


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

    # ===== calc subcommand =====
    parser_calc = subparsers.add_parser('calc')
    parser_calc.add_argument(
        'algorithm',
        help='Algorithm by which pi is calcurated',
        choices=ALGORITHMS,
    )
    parser_calc.add_argument(
        '--accuracy',
        default=10,
        type=int,
        help='accuracy',
    )
    parser_calc.add_argument(
        '-l',
        '--list',
        help='show algorithms list',
    )
    parser_calc.add_argument(
        '-s',
        '--separated',
        action='store_true',
        help='show separated number',
    )
    parser_calc.add_argument(
        '--grouped_digit',
        default=10,
        type=int,
        help='number of digits to be summarized when displaying',
    )
    parser_calc.set_defaults(handler=subcommand_calc)

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
