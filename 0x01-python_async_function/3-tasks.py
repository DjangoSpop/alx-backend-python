import asyncio
from random import wait_random


def task_wait_random(max_dlay: int = 0):
    """_summary_

    Args:
        max_dlay (int, optional): Maximum delay. Defaults to 0.

    Returns:
        float: _description_
    """
    return asyncio.create_task(wait_random(max_dlay))
