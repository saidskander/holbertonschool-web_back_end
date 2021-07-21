#!/usr/bin/env python3
""" Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Running time comprehensions """
    async_run = []
    start = time.time()
    for x in range(4):
        async_run.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*async_run)
    end = time.time()
    return end - start
