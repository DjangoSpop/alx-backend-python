
#!/usr/bin/env python3
from . import async_generator


async def async_comprehensiosn():
    """
    Summary of the function.
s
    Returns:
        List[int]: List of numbers generated asynchronously.
    """
    # your function goes here
    return [num async for num in async_generator()]
