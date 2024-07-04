#!/usr/bin/env python3
"""
type-annotated function
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples where each
    tuple contains a string from the input list and its lengt
    """
    return [(i, len(i)) for i in lst]
