#!/usr/bin/env python3
""" multiplier function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ float  """

    def x(f: float) -> float:
        """ secont comp """
        return float(f * multiplier)

    return x
