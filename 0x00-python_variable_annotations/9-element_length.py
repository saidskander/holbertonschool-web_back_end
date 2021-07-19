#!/usr/bin/env python3
""" length """
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """ length elements"""
    return [(i, len(i)) for i in lst]
