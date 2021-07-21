#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax and returns the Task. """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ task wait random """
    task_wait = asyncio.create_task(wait_random(max_delay))
    return task_wait
