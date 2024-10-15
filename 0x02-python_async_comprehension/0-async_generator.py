#!/usr/bin/env python3
"""Async generator"""


from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """a coroutine that takes no arguments."""
    for n in range(10):
        rand = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand
