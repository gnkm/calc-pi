import argparse
import sys
from typing import List

import mpmath

from calcpi import (
    actual,
    gauss_legendre,
    regular_polygon,
    utils,
)

ALGORITHMS: List[str] = [
    'actual',
    'gauss_legendre',
    'polygon',
]


def main():
    exec_subcommand()
    sys.exit()


def calc(args: argparse.Namespace) -> None:
    if args.algorithm == 'actual':
        pi: mpmath.mpf = actual.pi(args.accuracy)
    elif args.algorithm == 'gauss_legendre':
        pi = gauss_legendre.pi(args.accuracy)
    elif args.algorithm == 'polygon':
        pi = regular_polygon.pi(args.accuracy)

    formated_pi: str = utils.format_pi(pi, args.accuracy, args.separated)
    sys.stdout.write(formated_pi)


def error(args):
    print('error')


def exec_subcommand() -> None:
    global parser
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
    parser_calc.set_defaults(handler=calc)

    # ===== error subcommand =====
    parser_error = subparsers.add_parser('error')
    parser_error.add_argument(
        'algorithm',
        help='Algorithm by which pi is calcurated',
        choices=ALGORITHMS,
    )
    parser_error.add_argument(
        '--accuracy',
        default=10,
        type=int,
        help='accuracy',
    )
    parser_error.set_defaults(handler=error)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
