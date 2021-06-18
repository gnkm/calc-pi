"""Functions for debugging."""


import pprint
import sys
from typing import Any


PPRINT_INDENT: int = 4


def print_prettify(v: Any, exit: bool = True) -> None:
    """Wrapper of pprint.PrettyPrinter().

    Args:
        v (Any): displayed variable
        exit (bool, optional): If True, call exit(). Defaults to True.
    """
    pp = pprint.PrettyPrinter(indent=PPRINT_INDENT)
    pp.pprint(v)

    if exit:
        sys.exit()
