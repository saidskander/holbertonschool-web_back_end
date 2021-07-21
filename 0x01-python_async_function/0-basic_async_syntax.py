#!/usr/bin/env python3
""" async  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ async with sleep waiting """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
