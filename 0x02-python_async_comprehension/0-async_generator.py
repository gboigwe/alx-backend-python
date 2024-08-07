#!/usr/bin/env python3
"""Async await generator"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An asynchronously waits for each 1 second,
    yielding random numbers between 0 and 10
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
