#!/usr/bin/env python3
"""Defining the duck-typed annotations"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck-typed annotations function"""
    if lst:
        return lst[0]
    else:
        return None
