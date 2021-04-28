#!/usr/bin/env python3
"""sumary_line"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description]
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = (end - start) / n
    return total_time
