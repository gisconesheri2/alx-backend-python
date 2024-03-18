#!/usr/bin/env python3
"""
group several async coroutines together
"""
import asyncio
from typing import List

wait_delay = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    group several async coroutines together
    and return a sorted list of the return values
    for each coroutine
    """
    res = await asyncio.gather(*(wait_delay(max_delay)
                                 for _ in range(n)))
    return sorted(res)
