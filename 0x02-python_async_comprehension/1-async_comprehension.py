#!/usr/bin/env python3
import asyncio
import random
from types import list
async_generator = __import__('0-async_generator').async_generator



async def async_comprehension() -> list[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehensing over
    an async generator.
    """
  
    return [i async for i in async_generator()]
