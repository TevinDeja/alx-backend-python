#!/usr/bin/env python3
"""
type-annotated function
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary-like object
    """
    if key in dct:
        return dct[key]
    else:
        return default
