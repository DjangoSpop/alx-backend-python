
#!/usr/bin/env python3
"""
Module for practicing async comprehensions in Python.
"""
import asyncio
import random
from typing import List


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [num async for num in async_generator()]
