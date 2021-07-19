#!/usr/bin/env python3
""" float annotations """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum of the list  """

    result: float = 0

    for x in input_list:
        result += x

    return result
