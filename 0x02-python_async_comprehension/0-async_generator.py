#!/usr/bin/env python3
"""
Module for practicing async comprehensions in Python.
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
Asynchronous generator that yields
10 random numbers between 0 and 10
after waiting 1 second.

    Yields:
        float: A random number between 0 and 10.
    """
    # your function goes here
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
