#!/usr/bin/env python3
""" range simple """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """  page & Total size of the page +  tuple range  """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
