#!/usr/bin/env python3
"""Writing a function for coroutine"""


import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Altering the function delay"""
    spawn_lists = []
    d_delays = []

    for index in range(n):
        spawn = task_wait_random(max_delay)
        spawn_lists.append(spawn)

    for spawn in asyncio.as_completed((spawn_lists)):
        d_delay = await spawn
        d_delays.append(d_delay)
    return d_delays
