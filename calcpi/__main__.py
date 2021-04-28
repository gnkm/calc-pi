import argparse
import sys
from typing import List

from calcpi import simple
from calcpi import utils


ALGORITHMS: List[str] = [
    'simple'
]


def main():
    args: argparse.Namespace = _get_args()
    if args.algorithm == 'simple':
        pi: float = simple.pi(args.accuracy)

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
