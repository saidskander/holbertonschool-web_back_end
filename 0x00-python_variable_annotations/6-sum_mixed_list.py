#!/usr/bin/env python3
""" lists """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ float numbers mixt """

    result: float = 0

    for x in mxd_lst:
        result += x

    return result
