#!/usr/bin/env python3
"""
ducktype a function accepting unknown elements
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    ducktype a function accepting unknown elements
    """
    if lst:
        return lst[0]
    else:
        return None
