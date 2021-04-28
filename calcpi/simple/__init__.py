import math

import calcpi.utils as utils


def pi(accuracy: int) -> float:
    return utils.round(math.pi, accuracy)
