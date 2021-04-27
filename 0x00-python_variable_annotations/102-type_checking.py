
#!/usr/bin/env python3
""""sumary_line"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """[summary]

    Args:
        lst (Tuple): [description]
        factor (int, optional): [description]. Defaults to 2.

    Returns:
        List: [description]
    """
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))
