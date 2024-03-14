#!/usr/bin/env python3
"""
takes a list of floats and ints and add them up
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    takes a list of floatsand ints and add them up
    """
    total = 0
    for num in mxd_lst:
        total += num
    return total
