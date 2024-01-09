#!/usr/bin/env python3
"""
function should return a tuple of size two
containing a start index and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    index = page - 1
    return index * page_size, page_size * page
