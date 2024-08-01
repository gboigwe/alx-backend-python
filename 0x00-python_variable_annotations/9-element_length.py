#!/usr/bin/env python3
"""Annotating the function’s parameters
and return values with the appropriate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function's parameter annotated
    and returning values with appropriate types
    """
    return [(i, len(i)) for i in lst]
