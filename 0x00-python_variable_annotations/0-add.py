#!/usr/bin/env python3
"""function add typed-annotation"""


def add(a: float, b: float) -> float:
    """Function that adds two numbers together"""
    if type(a) and type(b) != float:
        print("Not a float, use float number")
    return float(a) + float(b)
