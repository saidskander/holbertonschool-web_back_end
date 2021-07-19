#!/usr/bin/env python3
"""
    Duck typing sequence Any
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe eleement """
    if lst:
        return lst[0]
    else:
        return None
