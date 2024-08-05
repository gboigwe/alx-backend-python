#!/usr/bin/env python3
"""Function that perform asynchronous await concurrent"""


import asyncio
import random


async def wait_random(max_delay=10):
    """Creating a delay function that await async"""
    d_delay = random.uniform(0, max_delay)
    await asyncio.sleep(d_delay)
    return d_delay
