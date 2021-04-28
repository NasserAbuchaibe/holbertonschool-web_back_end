#!/usr/bin/env python3
"""sumary_line"""


import asyncio
import random
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        typing.List[float]: [description]
    """
    list_del = []
    for i in range(n):
        list_del.append(task_wait_random(max_delay))

    list_delay = []
    for task in asyncio.as_completed(list_del):
        task_delay: float = await task
        list_delay.append(task_delay)

    return list_delay
