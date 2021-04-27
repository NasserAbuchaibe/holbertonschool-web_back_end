#!/usr/bin/env python3
""""5. Complex types - list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """[ takes a list of floats as argument
        and returns their sum as a float.]

    Args:
        input_list (List[float]): [list of float]

    Returns:
        float: [Sum of all items in the list]
    """
    return sum(input_list)
