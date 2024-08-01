#!/usr/bin/env python3
"""Type-annotated function that takes a string
and int OR float v as arguments and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that takes a string and int OR float
    v as arguments and returns a tuple
    """
    index = v ** 2
    return (k, index)
