#!/usr/bin/env python3
""" sixth basic annotation """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of number in a list"""
    sum: float = 0.0
    for element in mxd_lst:
        sum += element
    return sum
