#!/usr/bin/env python3
""""6. Complex types - mixed list mandatory"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """[takes a list mxd_lst of integers and floats
        and returns their sum as a float.]

    Args:
        mxd_lst (List[Union[int, float]]): [List of integer and float]

    Returns:
        float: [sum as a float]
    """
    return sum(mxd_lst)
