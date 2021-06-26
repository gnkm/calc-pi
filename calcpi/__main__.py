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
from calcpi.subcommands import eval as sc_eval

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
    subparsers = sc_eval.define_args(subparsers)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

    sys.exit()


if __name__ == '__main__':
    main()
