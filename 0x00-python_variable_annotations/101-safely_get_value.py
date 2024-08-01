#!/usr/bin/env python3
"""Type-annotated function in advanced way"""
from typing import Mapping, Any, Union, Typevar
T = Typevar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
        = None) -> Union[Any, T]:
    """Function haddling the type-annotated"""
    if key in dct:
        return dct[key]
    else:
        return default
