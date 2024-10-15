#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time with async"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    list_delay: List[float] = await asyncio.gather(*tasks)
    return list_delay