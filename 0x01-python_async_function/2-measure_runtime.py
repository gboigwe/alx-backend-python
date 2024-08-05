#!/usr/bin/env python3
"""Measuring the runtime of the delay"""


import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function to return the total time taken"""
    begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    time_taken = end - begin
    return (time_taken/n)
