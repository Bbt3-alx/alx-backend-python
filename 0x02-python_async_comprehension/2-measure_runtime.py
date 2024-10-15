#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""


import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    start_time = time.time()
    mesure = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*mesure)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time
