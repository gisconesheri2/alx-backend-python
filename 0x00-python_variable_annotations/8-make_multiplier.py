#!/usr/bin/env python3
"""
a function that returns another function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function that returns another function
    """
    return lambda num: multiplier * num
