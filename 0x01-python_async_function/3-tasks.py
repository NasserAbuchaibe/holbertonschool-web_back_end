#!/usr/bin/env python3
"""sumary_line"""


import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """[summary]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        asyncio.Task: [description]
    """
    return asyncio.create_task(wait_random(max_delay))
