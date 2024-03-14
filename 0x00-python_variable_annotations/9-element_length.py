#!/usr/bin/env python3
"""
duck type annotations using Iterable and Sequence
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    duck type annotations using Iterable and Sequence
    """
    return [(i, len(i)) for i in lst]
