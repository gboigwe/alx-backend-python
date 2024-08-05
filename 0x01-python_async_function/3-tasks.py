#!/usr/bin/env python3
"""Writing a function using a regular"""


import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returning an async function without await"""
    return asyncio.create_task(wait_random(max_delay))
