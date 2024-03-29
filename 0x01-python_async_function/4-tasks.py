#!/usr/bin/env python3
"""
group several async coroutines together
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    group several async coroutines together
    and return a sorted list of the return values
    for each coroutine
    """
    res = await asyncio.gather(*(task_wait_random(max_delay)
                                 for _ in range(n)))
    return sorted(res)
