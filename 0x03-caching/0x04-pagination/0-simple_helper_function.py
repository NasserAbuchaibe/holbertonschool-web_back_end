#!/usr/bin/env python3
""""sumary_line"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """[summary]

    Args:
        page (int): [description]
        page_size (int): [description]

    Returns:
        Tuple[int, int]: [description]
    """
    return (((page - 1) * page_size), (page * page_size))
