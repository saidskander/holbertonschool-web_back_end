#!/usr/bin/env python3
"""safety get"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]=None)\
                     -> Union[Any, T]:
    """ safely_get_value  """
    if key in dct:
        return dct[key]
    else:
        return default
