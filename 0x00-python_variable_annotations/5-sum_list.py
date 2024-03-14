#!/usr/bin/env python3
"""
takes a list of floats and add them up
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes a list of floats and add them up
    """
    total = 0
    for num in input_list:
        total += num
    return total
