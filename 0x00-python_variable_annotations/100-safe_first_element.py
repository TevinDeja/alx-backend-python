#!/usr/bin/env python3
"""
duck-typed annotated function
"""
from typing import Sequence, Any, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns the first element of a sequence if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
