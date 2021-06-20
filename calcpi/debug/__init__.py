"""Functions for debugging."""


import pprint
import sys
from typing import Any


PPRINT_INDENT: int = 4


def print_prettify(v: Any, is_exited: bool = True) -> None:  # pylint: disable=invalid-name
    """Wrapper of pprint.PrettyPrinter().

    Args:
        v (Any): displayed variable
        is_exited (bool, optional): If True, call exit(). Defaults to True.
    """
    pp = pprint.PrettyPrinter(indent=PPRINT_INDENT)  # pylint: disable=invalid-name
    pp.pprint(v)

    if is_exited:
        sys.exit()
