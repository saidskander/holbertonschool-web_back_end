#!/usr/bin/env python3
""" Alter the code into a new function """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ multiple coroutines """
    delay_list: List[float] = []
    multi_delay: List[float] = []
    for i in range(n):
        delay_list.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delay_list):
        start_result = await delay
        multi_delay.append(start_result)
    return multi_delay
