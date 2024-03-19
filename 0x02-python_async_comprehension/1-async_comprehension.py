#!/usr/bin/env python3
"""
use an async genrator inside an async list comprehession
"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    use an async genrator inside an async list comprehession
    """
    return [num async for num in async_generator()]
