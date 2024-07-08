#!/usr/bin/env python3
"""
Module defines an asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.
    Returns:
        float: The actual time delayed.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
