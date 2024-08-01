#!/usr/bin/env python3
"""Type-annotated function that takes a float
as argument and returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that takes a float multiplier
    as argument and returns a function
    """
    return lambda i: i * multiplier
