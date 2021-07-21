#!/usr/bin/env python3
""" Import wait_random from previous python3 file. """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ multiple coroutines """
    delay_list: List[float] = []
    multi_delay: List[float] = []
    for i in range(n):
        delay_list.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delay_list):
        earliest_result = await delay
        multi_delay.append(earliest_result)
    return multi_delay
