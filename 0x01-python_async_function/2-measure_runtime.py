#!/usr/bin/env python3
"""
Module for measuring the runtime of the wait_n coroutine
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Computes the average runtime of wait_n.
    
    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for wait_random.
    
    Returns:
        float: The average runtime of wait_n over n calls.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
