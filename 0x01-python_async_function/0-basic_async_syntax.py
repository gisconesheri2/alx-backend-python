#!/usr/bin/env python3
"""
async function that takes an integer argument( max_delay)
waits for a random delay between 0 and max_delay
 seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async function that takes an integer argument( max_delay)
    waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
