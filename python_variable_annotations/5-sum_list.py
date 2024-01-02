#!/usr/bin/env python3
""" sixth basic annotation """

from typing import List


def sum_list(input_list: List[float] ) -> float:
    """return the sum of number in a list"""
    sum: float = 0.0
    for element in input_list:
        sum += element
    return float(sum)
