#!/usr/bin/env python3
""""8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[summary]

    Args:
        multiplier (float): [description]

    Returns:
        Callable[[float], float]: [description]
    """
    return lambda x: multiplier * x
