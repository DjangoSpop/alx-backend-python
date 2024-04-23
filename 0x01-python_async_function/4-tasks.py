import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times in parallel using asyncio.
    Returns a list of the delays in ascending order.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))
