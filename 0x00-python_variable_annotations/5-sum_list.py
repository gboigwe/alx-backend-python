#!/usr/bin/rnv python3
"""Type-annotaion function for list of sum of float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Funcion that takes list of float and return as float"""
    a: float = 0.0
    for index in input_list:
        a += index
    return a
