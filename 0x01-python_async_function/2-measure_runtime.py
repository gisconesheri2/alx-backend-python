#!/usr/bin/env python3
"""
Measure how long it takes to run wait_n:
an asynchronous function
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure how long it takes to run wait_n:
    an asynchronous function
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
