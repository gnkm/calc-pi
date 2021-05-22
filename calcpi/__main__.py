import argparse
import sys
from typing import List

import mpmath

from calcpi import gauss_legendre
from calcpi import regular_polygon
from calcpi.utils import display
from calcpi import value_decimal
from calcpi import value_mpmath


ALGORITHMS: List[str] = [
    'value_mpmath',
    'value_decimal',
    'gauss_legendre',
    'polygon',
]


def main():
    args: argparse.Namespace = _get_args()
    if args.algorithm == 'value_mpmath':
        pi: mpmath.mpf = value_mpmath.pi(args.accuracy)
    elif args.algorithm == 'value_decimal':
        pi = value_decimal.pi(args.accuracy)
    elif args.algorithm == 'gauss_legendre':
        pi: mpmath.mpf = gauss_legendre.pi(args.accuracy)
    elif args.algorithm == 'polygon':
        pi: mpmath.mpf = regular_polygon.pi(args.accuracy)

    mpmath.nprint(pi, args.accuracy)


def _get_args():
    parser = argparse.ArgumentParser(description='Display Pi')
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

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    elif sys.argv[1] in ['-l', '--list']:
        display(ALGORITHMS)
        sys.exit()

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
