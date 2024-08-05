#!/usr/bin/env python3
"""Executing multiple coroutines"""


import asyncio
import random
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function that awaits delay
    and returns list of all delays
    """
    spawn_lists = []
    d_delays = []

    for i in range(n):
        spawn = wait_random(max_delay)
        spawn_lists.append(spawn)

    for spawn in asyncio.as_completed((spawn_lists)):
        d_delay = await spawn
        d_delays.append(d_delay)
    return d_delays
