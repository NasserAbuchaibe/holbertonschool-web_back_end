#!/usr/bin/env python3
"""sumary_line"""


import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[summary]

    Returns:
        List[float]: [description]
    """

    return [num async for num in async_generator()]
