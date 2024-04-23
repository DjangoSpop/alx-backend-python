#!/usr/bin/env python3
"""
Module for concurrent coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns the
    list of all the delays (float values) in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value for each spawned coroutine.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = []
    coroutines = [wait_random(max_delay) for _ in range(n)]

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return sorted(delays)
