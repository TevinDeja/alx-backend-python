#!/usr/bin/env python3
"""
async_comprehension coroutine
"""
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.
    Returns the list of 10 random numbers.
    """
    return [num async for num in async_generator()]
