#!/usr/bin/env python3
"""4 Task"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function altered"""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    list_delay: List[float] = await asyncio.gather(*tasks)
    return sorted(list_delay)
