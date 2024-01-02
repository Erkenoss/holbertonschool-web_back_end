#!/usr/bin/env python3
"""annote some element here"""

from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annote some element"""
    return [(i, len(i)) for i in lst]
