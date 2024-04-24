
#!/usr/bin/env python3
"""
Module for practicing async comprehensions in Python.
"""
import asyncio
import random
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four times in
    parallel.
    Returns:
        float: The total runtime in seconds.
    """
    # function starts from here
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
