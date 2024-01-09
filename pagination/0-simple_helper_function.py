#!/usr/bin/env python3
"""
function should return a tuple of size two
containing a start index and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    return tuple (index 0 of page given and
    the number of element at the end of the page)
    """
    index = page - 1
    return index * page_size, page_size * page
