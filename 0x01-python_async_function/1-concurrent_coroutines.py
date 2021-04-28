#!/usr/bin/env python3
"""sumary_line"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        typing.List[float]: [description]
    """
    list_e = []
    for i in range(n):
        list_e.append(asyncio.create_task(wait_random(max_delay)))

    list_delay = []
    for task in asyncio.as_completed(list_e):
        task_delay: float = await task
        list_delay.append(task_delay)

    return list_delay
