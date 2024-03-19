#!/usr/bin/env python3
"""
write a asynchronous float generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    write a asynchronous float generator
    """
    for _ in range(10):
        yield (random.uniform(0, 10))
        await asyncio.sleep(1)
