import argparse
import sys
from typing import Dict, List

import mpmath

from calcpi import gauss_legendre
from calcpi import regular_polygon
import calcpi.utils as utils
from calcpi import value_decimal
from calcpi import actual


ALGORITHMS: List[str] = [
    'actual',
    'gauss_legendre',
    'polygon',
]


def main():
    args: argparse.Namespace = _get_args()
    if args.algorithm == 'actual':
        pi: mpmath.mpf = actual.pi(args.accuracy)
    elif args.algorithm == 'gauss_legendre':
        pi: mpmath.mpf = gauss_legendre.pi(args.accuracy)
    elif args.algorithm == 'polygon':
        pi: mpmath.mpf = regular_polygon.pi(args.accuracy)

    formated_pi: str = utils.format_pi(pi, args.accuracy, args.separated)
    utils.display(formated_pi)


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
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    elif sys.argv[1] in ['-l', '--list']:
        utils.display(ALGORITHMS)
        sys.exit()

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
