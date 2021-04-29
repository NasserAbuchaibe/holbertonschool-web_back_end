#!/usr/bin/env python3
"""sumary_line"""


import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """[summary]

    Returns:
        float: [description]
    """

    start_t = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    final_t = time()
    return final_t - start_t
