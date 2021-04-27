import pprint
from typing import Any


def display(v: Any) -> None:
    """Display var on STDOUT

    Args:
        v (Any): displayed arg
    """
    pprint.pprint(v)
