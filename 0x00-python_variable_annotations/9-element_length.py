#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Iterable, List, Tuple

def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples where each tuple contains a string from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
