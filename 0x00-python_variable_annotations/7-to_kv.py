#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """[string and int/float to tuple]

    Args:
        k (str): [String]
        v (Union[int, float]): [Number float or integer]

    Returns:
        Tuple[str, float]: [Tupla]
    """
    return (k, v)
