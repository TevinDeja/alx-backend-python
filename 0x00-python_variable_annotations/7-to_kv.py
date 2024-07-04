#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float, returns a tuple with the string and the square of the number.
    """
    return (k, float(v ** 2))
