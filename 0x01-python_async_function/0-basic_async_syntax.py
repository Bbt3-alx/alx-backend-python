#!/usr/bin/env python3
"""The basics of async"""


import random
import asyncio


async def wait_random(max_delay=10):
    """
    an asynchronous coroutine  that waits for a random delay between 0 and
    max_delay (included and float value) seconds and eventually returns it
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)

    return rand
