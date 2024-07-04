#!/usr/bin/env python3
"""
type-annotated function using TypeVar
"""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Safely gets a value from a dictionary-like object
    returning a default if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
