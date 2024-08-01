#!/usr/bin/env python
"""Type-annotated function which takes a list of
integers and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function which takes a list of integers and 
    floats and returns their sum as a float
    """
    a: float = 0.0
    for index in mxd_lst:
        a += index
    return a
