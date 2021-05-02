import argparse
import sys
from typing import List

from calcpi import gauss_legendre
from calcpi import regular_polygon
from calcpi import utils
from calcpi import value


ALGORITHMS: List[str] = [
    'value',
    'gauss_legendre',
    'polygon',
]


def main():
    args: argparse.Namespace = _get_args()
    if args.algorithm == 'value':
        pi: float = value.pi(args.accuracy)
    elif args.algorithm == 'gauss_legendre':
        pi: float = gauss_legendre.pi(args.accuracy)
    elif args.algorithm == 'polygon':
        pi: float = regular_polygon.pi(args.accuracy)

    utils.display(pi)


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
        utils.display(ALGORITHMS)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
