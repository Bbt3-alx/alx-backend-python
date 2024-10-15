#!/usr/bin/env python3
"""1. Async Comprehensions"""


import random
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """A coroute that take no args and return 10 random numbers"""
    rand_num = [x async for x in async_generator()]
    return rand_num
