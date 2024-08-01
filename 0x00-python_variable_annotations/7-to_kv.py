#!/usr/bin/env python3
"""Type-annotated function that takes a string
and int OR float v as arguments and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that takes a string and int OR float
    v as arguments and returns a tuple
    """
    index = k ** 2
    return (v, index)
