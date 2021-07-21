#!/usr/bin/env python3
""" async  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ async with sleep waiting """
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
