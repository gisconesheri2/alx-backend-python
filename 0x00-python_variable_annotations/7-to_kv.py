#!/usr/bin/env python3
from typing import Union, Tuple
"""
takes a string and and int or float and return a tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string and and int or float and return a tuple
    """
    return (k, v * v)
