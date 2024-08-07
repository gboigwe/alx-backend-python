#!/usr/bin/env python3
"""Writing a measure_runtime coroutine function"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executing async_comprehension function 4 times
    in parallel using asyncio.gather"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time
