#!/usr/bin/env python3
"""sumary_line"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """[summary]

    Args:
        lst (Iterable[Sequence]): [description]

    Returns:
        List[Tuple[Sequence, int]]: [description]
    """
    return [(i, len(i)) for i in lst]
