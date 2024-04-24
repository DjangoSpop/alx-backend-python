#!/usr/bin/env python3
"""
Module containing an async comprehension function.
"""
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [num async for num in async_generator()]