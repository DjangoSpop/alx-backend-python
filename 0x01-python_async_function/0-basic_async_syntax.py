#!/usr/bin/env python3
import random
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous function that waits for a random amount of time.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
            Defaults to 10.

    Returns:
        float: The actual delay in seconds.
    """
    # Generate a random number between 0 and max_delay
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
