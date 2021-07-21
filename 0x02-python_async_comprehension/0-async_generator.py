#!/usr/bin/env python3
""" No coroutine arguments will takes. """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ Generator """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
