#!/usr/bin/env python3
from typing import List
from random import uniform
import asyncio


async def wait_random(max_delay: int) -> float:
    """_summary_
    Args:
        max_delay (int): _description_

    Returns:
        float: _description_
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_
    Args:
        n (int): _description_
        max_delay (int): _description_
    Returns:
        List[float]: _description_
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
