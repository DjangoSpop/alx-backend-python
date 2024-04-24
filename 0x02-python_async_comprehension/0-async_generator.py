#!/usr/bin/env python3
"""
Module for practicing async comprehensions in Python.
"""
import asyncio
import random
from typing import List
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields
    10 random numbers between 0 and 10
    after waiting 1 second.

    Yields:
        float: A random number between 0 and 10.
    """
    # your function goes here
    for _ in range(10):
        # sleep for 1 second before yielding a value
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
