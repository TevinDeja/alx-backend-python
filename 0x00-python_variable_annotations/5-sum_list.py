#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point numbers.
    """
    return sum(input_list)
