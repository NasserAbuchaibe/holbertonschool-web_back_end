#!/usr/bin/env python3
"""sumary_line"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """[summary]

    Yields:
        Generator[float, None, None]: [description]
    """

    for count in range(10):
        yield random.random()
        await asyncio.sleep(1)
