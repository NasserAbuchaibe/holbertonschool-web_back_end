#!/usr/bin/env python3
"""sumary_line"""

from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[Any, None]) -> Union[None, Any]:
    """[summary]

    Args:
        dct (Mapping): [description]
        key (Any): [description]
        default (Union[Any, None]): [description]

    Returns:
        Union[None, Any]: [description]
    """
    if key in dct:
        return dct[key]
    else:
        return default
