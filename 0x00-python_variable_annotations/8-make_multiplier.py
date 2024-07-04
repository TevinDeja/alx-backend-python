#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies
    """
    return lambda x: x * multiplier
